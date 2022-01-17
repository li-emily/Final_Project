# -*- coding: utf-8 -*-
"""new_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a2lw1nLT_1v0Zg78KkWxrF_lvkY1SK0z
"""

# Import our dependencies
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import os
from psycopg2 import sql, connect
import pyspark

spark_version = 'spark-3.2.0'
os.environ['SPARK_VERSION']=spark_version

# Install Spark and Java
!apt-get update
!apt-get install openjdk-11-jdk-headless -qq > /dev/null
!wget -q http://www.apache.org/dist/spark/$SPARK_VERSION/$SPARK_VERSION-bin-hadoop2.7.tgz
!tar xf $SPARK_VERSION-bin-hadoop2.7.tgz
!pip install -q findspark

# Set Environment Variables
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = f"/content/{spark_version}-bin-hadoop2.7"

# Start a SparkSession
import findspark
findspark.init()

!wget https://jdbc.postgresql.org/download/postgresql-42.2.16.jar

# Store environmental variable
from getpass import getpass
password = getpass('Enter database password')

try:
    # declare a new PostgreSQL connection object
    conn = connect(
        dbname = "data_final_project",
        user = "root",
        host = "finalproject.c0f9uvcdenwr.us-east-2.rds.amazonaws.com",
        port = "5433",
        password = password
    )

    # print the connection if successful
    print ("psycopg2 connection:", conn)

except Exception as err:
    print ("psycopg2 connect() ERROR:", err)
    conn = None

cr = conn.cursor()
cr.execute('SELECT * FROM covid_surv;')
tmp = cr.fetchall()

# Extract the column names
col_names = []
for elt in cr.description:
    col_names.append(elt[0])

# Create the dataframe from list of col_names
df = pd.DataFrame(tmp, columns=col_names)

df.head()

# iterating the columns 
for col in df.columns: 
    print(col)

"""Cleaning Data"""

#drop unused columns
df.drop(['county', 'current_status', 'Month'], axis=1, inplace=True)

#standardize missing
df = df.replace(['Unknown', 'Missing', 'NA'], 'NaN')

#give variables numerical values
#gender
df = df.replace({'Male': 1, 'Female': 2})

#age
df = df.replace({'0 - 17 years': 1, '18 to 49 years': 2, '50 to 64 years': 3, '65+ years': 4})
#race
df = df.replace({'American Indian/Alaska Native': 1, 'Asian': 2, 'Black': 3, 
                 'Multiple/Other': 4, 'Native Hawaiian/Other Pacific Islander': 5, 'White': 6})
#ethnicity
df = df.replace({'Hispanic/Latino': 1, 'Non-Hispanic/Latino':2})

#yes and no to 1/0
df = df.replace({'Yes': 1, 'No':0})

print(df.dtypes)

#Convert columns from object to float
df['age_range'] = df['age_range'].astype(float, errors = 'raise')
df['sex'] = df['sex'].astype(float, errors = 'raise')
df['race'] = df['race'].astype(float, errors = 'raise')
df['ethnicity'] = df['ethnicity'].astype(float, errors = 'raise')
df['hospitalized'] = df['hospitalized'].astype(float, errors = 'raise')
df['died'] = df['died'].astype(float, errors = 'raise')

#Drop all NaN values
df = df.dropna(axis=0, how='any')
df

#Convert pandas DF to pyspark DF
from pyspark.sql import SparkSession
#Create PySpark SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("convert").config("spark.driver.extraClassPath","/content/postgresql-42.2.16.jar").getOrCreate()
    
#Create PySpark DataFrame from Pandas
clean_df=spark.createDataFrame(df) 
clean_df.printSchema()
clean_df.show()

#download file to RDS
mode = "append"
jdbc_url="jdbc:postgresql://finalproject.c0f9uvcdenwr.us-east-2.rds.amazonaws.com:5433/data_final_project"
config = {"user":"root",
          "password": password,
          "driver":"org.postgresql.Driver"}

# Write DataFrame to clean_covid table in RDS
clean_df.write.jdbc(url=jdbc_url, table='clean_covid', mode=mode, properties=config)

# Generate the categorical variable list
cat = ['State']

# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False)

# Fit and transform the OneHotEncoder using the categorical variable list
encode_df = pd.DataFrame(enc.fit_transform(df[cat]))

# Add the encoded variable names to the dataframe
encode_df.columns = enc.get_feature_names(cat)
encode_df.head()

# Merge one-hot encoded features and drop the originals
df2 = df.merge(encode_df, left_index=True, right_index=True).drop(columns=cat, axis=1)
df2.head()

#Create PySpark DataFrame from Pandas
states_df=spark.createDataFrame(df2) 
states_df.show()

#download encoded dataset into clean_states
states_df.write.jdbc(url=jdbc_url, table='clean_states', mode=mode, properties=config)

"""Splitting and scaling"""

# Split our preprocessed data into our features and target arrays
y = df2["died"]
X = df2.drop(["died"], axis =1)

# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, stratify=y)

# Create a StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

"""Neural Network Model"""

import tensorflow as tf

# Define the model - deep neural net, i.e., the number of input features and hidden nodes for each layer.
number_input_features = len(X_train_scaled[0])
hidden_nodes_layer1 = 80
hidden_nodes_layer2 = 30

nn = tf.keras.models.Sequential()

# First hidden layer
nn.add(
    tf.keras.layers.Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu")
)
# Second hidden layer
nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer2, activation="relu"))


# Output layer
nn.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

# Check the structure of the model
nn.summary()

# Compile the model
nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train the model
fit_model = nn.fit(X_train_scaled, y_train, epochs=20)

# Evaluate the model using the test data
model_loss, model_accuracy = nn.evaluate(X_test_scaled,y_test,verbose=2)
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")

"""Oversampling"""

#Oversampling Model
from collections import Counter
from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=1)
X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

Counter(y_resampled)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='sag', random_state=1)
model.fit(X_resampled, y_resampled)

from sklearn.metrics import confusion_matrix
y_pred = model.predict(X_test)

# Calculating the confusion matrix.
cm = confusion_matrix(y_test, y_pred)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

cm_df

from sklearn.metrics import balanced_accuracy_score
balanced_accuracy_score(y_test, y_pred)

from imblearn.metrics import classification_report_imbalanced
print(classification_report_imbalanced(y_test, y_pred))

"""SMOTE"""

#SMOTE
from imblearn.over_sampling import SMOTE
X_resampled, y_resampled = SMOTE(random_state=1,
sampling_strategy='auto').fit_resample(
   X_train, y_train)

model = LogisticRegression(solver='sag', random_state=1)
model.fit(X_resampled, y_resampled)

y_pred = model.predict(X_test)
balanced_accuracy_score(y_test, y_pred)

# Calculating the confusion matrix.
cm = confusion_matrix(y_test, y_pred)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

cm_df

print(classification_report_imbalanced(y_test, y_pred))

"""Undersampling"""

# Undersampling
from imblearn.under_sampling import RandomUnderSampler
ros = RandomUnderSampler(random_state=1)
X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='sag', random_state=1)
model.fit(X_resampled, y_resampled)

y_pred = model.predict(X_test)
balanced_accuracy_score(y_test, y_pred)

# Calculating the confusion matrix.
cm = confusion_matrix(y_test, y_pred)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

cm_df

print(classification_report_imbalanced(y_test, y_pred))

"""SMOTEEN"""

# SMOTEEN
from imblearn.combine import SMOTEENN
smote_enn = SMOTEENN(random_state=0)
X_resampled, y_resampled = smote_enn.fit_resample(X, y)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='sag', random_state=1)
model.fit(X_resampled, y_resampled)

# Making predictions using the testing data.
y_pred = model.predict(X_test)

# Calculating the confusion matrix.
cm = confusion_matrix(y_test, y_pred)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

cm_df

balanced_accuracy_score(y_test, y_pred)

from imblearn.metrics import classification_report_imbalanced
print(classification_report_imbalanced(y_test, y_pred))

"""Decision Tree"""

# Decision Tree
# Import Dependencies
from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
# Creating the decision tree classifier instance.
model = tree.DecisionTreeClassifier()
# Fitting the model.
model = model.fit(X_train_scaled, y_train)

# Making predictions using the testing data.
predictions = model.predict(X_test_scaled)

# Calculating the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

cm_df

accuracy_score(y_test, predictions)

print(classification_report_imbalanced(y_test, y_pred))

"""Random Forest

"""

# Random Forest
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=128, random_state=78)

# Fitting the model
rf_model = rf_model.fit(X_train_scaled, y_train)

# Making predictions using the testing data.
predictions = rf_model.predict(X_test_scaled)

# Calculating the confusion matrix.
cm = confusion_matrix(y_test, predictions)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

cm_df

accuracy_score(y_test, predictions)

print(classification_report_imbalanced(y_test, y_pred))