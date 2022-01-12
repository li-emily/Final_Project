# -*- coding: utf-8 -*-
"""pyspark_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H9kNhPIJ5EG9il9FeK1A_yn4osyIgxmS
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
cr.execute('SELECT * FROM no_booster;')
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

df['Death_Pct'] = round(df.deaths / df.cases,3)
df['Risk'] = np.where((df['Death_Pct'] >0.017), 1, 0)

df.head(5)

# convert the 'Date' column to datetime format
df.date= pd.to_datetime(df.date)
df.drop('County Name', axis=1, inplace=True)
df

df['series_complete_yes'] = df['series_complete_yes'].astype(float, errors = 'raise')
df['series_complete_pop_pct'] = df['series_complete_pop_pct'].astype(float, errors = 'raise')
df['administered_dose1_pop_pct'] = df['administered_dose1_pop_pct'].astype(float, errors = 'raise')

print(df.dtypes)

filtered_df = df.loc[(df['date'] >= '2021-12-15')]
filtered_df.reset_index(drop=True, inplace=True)
filtered_df

# Generate the categorical variable list
cat = ['state']

# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False)

# Fit and transform the OneHotEncoder using the categorical variable list
encode_df = pd.DataFrame(enc.fit_transform(filtered_df[cat]))

# Add the encoded variable names to the dataframe
encode_df.columns = enc.get_feature_names(cat)
encode_df.head()

# Merge one-hot encoded features and drop the originals
df2 = filtered_df.merge(encode_df, left_index=True, right_index=True).drop(columns=cat, axis=1)
df2.head()

# Split our preprocessed data into our features and target arrays
y = df2["Risk"]
X = df2.drop(["Risk", "date", "Death_Pct"], axis =1)

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