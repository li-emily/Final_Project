# Measuring the Impact of the COVID Epidemic

## Overview:

## Topic:

The COVID-19 pandemic over 2021 & predicting COVID case severity. 

## Reason for Selecting Topic: 

The aim of our analysis is to determine how demographic factors including location, age-range, sex, race, and ethncity, contribute to the likelihood of developing severe responses to COVID-19. The team chose this topic since the COVID pandemic has dominated life in the United States over the past two years. We thought it would be interesting to predict how likely you are to have a severe case of COVID, if you were exposed to the virus. As vaccines and medications have been developed, we wanted to explore and see which communities in the United States were most at risk for negative outcomes.  

## Source of Data: 

 We utilized sources provided by the CDC website which examined: 
  * Demographics of Patients withg COVID-19 in 2021 
  * Population Vaccination Data in 2021
  * Hospitalization and Mortality in Patients with COVID-19 in 2021

## Questions We Hope to Answer:

* If I came into contact with COVID, how severe will my case be?
* How many deaths have been caused by COVID-19 in each state in the United States?
* How many cases have occurred in 2021?
* How many people have received the COVID-19 vaccine in each state?
* Have COVID-19 vaccines led to a decrease in deaths in the United States?

## Team Members
Team Role | Name
--- | ---
Square | Emily Li
Triangle | Valentina Osorio
Circle | Zina Shah
X | Arielle Greenspan

## Data Overview

**Data Exploration Phase**:

* Clean data to determine number of cases and deaths
* Examine vaccination rates per state and county
* Determine factors which would reduce vaccination rate
* Depict data findings in Tableau and Javascript models.
* Depict data findings in Tableau and Javascript models.

**ERD:**
* Below is an ERD demonstrating the relationships between each of these entities from the different datasets we used for the machine learning model and visualizations:
![ERD2](https://user-images.githubusercontent.com/88119288/150011141-fe51a33b-40ee-418a-814e-0b0a0214c865.PNG)

**Original Datasets:**

 **Vaccinations**
 
 ![Original_covid_vaccinations_1](https://user-images.githubusercontent.com/88119288/149823576-6a0939ff-ee65-464f-b43a-37c2a51ae93a.PNG)
 
**COVID Confirmed**

![Original_covid_confirmed1](https://user-images.githubusercontent.com/88119288/149825909-de0ea531-00c5-499f-a36b-85e4f15a01d7.png)

**COVID Deaths**

![Original_covid_deaths1](https://user-images.githubusercontent.com/88119288/149826009-41780e98-5c1c-4ab5-be66-b08df281d74d.png)
 
**Final Merged Dataset**

![Final_complete_dataset](https://user-images.githubusercontent.com/88119288/149824499-f26d0e29-2ee3-480f-980f-a6a8f05c317a.PNG)

Most of our datasets came from various CDC sources. Due to the vast amount of data, we had to do some significant cleaning before we were able to use it for our machine learning model. There was a lot of data that we had to remove since it did not correlate to our project's main focus. There were missing and null values. We had to merge various CSV files by date, state and county. Overall, we managed to get a clean dataset to proceed with our analysis.
 
## Machine Learning Model

**Benefits of our Model**
* Collection of prediction trees helps estimate variable importance and can handle big data with multiple variables quickly.
* Our final question based on our available data was: Would these certain factors predispose patients to mortality from COVID-19? The random forest model was chosen since it would fit the parameters needed to predict a binary outcome.


**Steps Taken**
* Removed features so the model was not so crowded. 
* Trained with a large dataset to help the algorithm. 
* Limited n estimators.

**Training and Testing of Model**

**Limitations of Our Model**
* May overfit if data is messy due to adding more decision trees to the algorithm for the best result.

**Our Model at Work**

![Image](Resources/Image.png)

## Challenges and Recommendations

* Many of our datasets were difficult to clean and did not merge properly with other datasets. Next time, we would use datasets that were more clean to start with. 
* When it came to creating our dashboard, some of our files were too large to work with when building the html page. In the future, we would decrease the size of the file and pare down the data prior to building the html page.
* We had such a large breadth of data from the CDC, so it was hard to tell what was really relevant to our predictive model. In the future, we would try to have a clearer vision of what data is necessary.
* Further exploration could also be implemented to include more demographic factors such as socioeconomic factors, political affiliations, income levels to provide an even more precise prediction that mimics real-world scenarios.

## Technology Used:
We used an array of software and analytic tools to complete our project. These resources are depicted and elaborated upon below:

* Data Cleaning/Analysis:
  * Python Pandas
  * Jupyter Notebook 
* Database Creation:
  * PostgreSQL
  * Amazon Web Services (AWS)
* Connecting to the Database:
  * Psycopg2
* Machine Learning:
  * Scikit-Learn
  * TensorFlow
  * Google Colab 
* Dashboard(s):
  * Visualization Dashboard:
    * Tableau
  * Interactive Web-page:
    * Javascript
    * Flask
    * HTML
    * Heroku 

## Visualizations:

A Preview of some of the Tableau visuals that range from COVID-19 cases, deaths and demographic data can be seen below:

* COVID cases per US county as of 1/1/2021

![Image](Resources/Case1.png)

* COVID cases per US county as of 12/1/2021

![Image](Resources/Case2.png)

* COVID deaths per US county as of 1/1/2021

![Image](Resources/Death1.png)

* COVID deaths per US county as of 12/1/2021 

![Image](Resources/Death2.png)

* US Hospitalizations over 2021

![Image](Resources/Hospital1.png)

* COVID Hospitalizations and Deaths per Racial Group

![Image](Resources/Race.png)

  ### Our comprehensive Tableau Data Dashboard can be found below, explaining our data story.

   [View Our Tableau Data Dashboard](https://public.tableau.com/app/profile/zina.shah/viz/ADeepDiveintoCOVID-19LetsSeetheData/Final_Dashboard)

## Dashboard:

* Code utilized to build Dashboard can be found [here.](https://github.com/ariellegreenspan/covid-severity2)
* Conceptualization of Dashboard can be found [here.](https://docs.google.com/presentation/d/1ALpovgediQ_bLdq4W2oY2uJnHIKJHVdTsb4E91iFyhw/edit#slide=id.p)
* The link to our Heroku Dashboard can be found [here.](https://covid-severity2.herokuapp.com/)
* The link to our Vaccination Summary table can be found [here.](https://covid-severity2.herokuapp.com/summary)
* The link to our comprehensive data sourced from our database can be found [here.](https://covid-severity2.herokuapp.com/booster_table)


## Watch Our Dashboards In Action! 

#### Tableau Dashboard:


## Presentation:

* An Overview of our Presentation can be found [here.](https://docs.google.com/presentation/d/1PIXc8MoQCyhf88awjZfFVZ0AFq4j6_KTh0REr4ba3PE/edit?usp=sharing)


