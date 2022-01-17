# Measuring the Impact of the COVID Epidemic

## Overview:

## Reason for Selecting Topic: 

The aim of our analysis is to determine how demographic factors including location, age-range, sex, race, and ethncity, contribute to the likelihood of developing severe responses to COVID-19? The team chose this topic since the COVID pandemic has dominated life in the United States over the past two years. As vaccines and medications have been developed, we wanted to explore and see which communities in the United States were most at risk for negative outcomes. 

## Source of Data: 

 We utilized sources provided by the CDC website which examined: 
  * Demographics of Patients withg COVID-19 in 2021 
  * Population Vaccination Data in 2021
  * Hospitalization and Mortality in Patients with COVID-19 in 2021

## Questions We Hope to Answer:

* How many deaths have been caused by COVID-19 in each state in the United States?
* How many cases have occurred in 2021?
* How many people have received the COVID-19 vaccine in each state?
* What demographic and economic factors might lead to vaccine hesitancy?
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


**Steps Taken
* Removed features so the model was not so crowded. 
* Trained with a large dataset to help the algorithm. 
* Limited n estimators.

**Limitations of Our Model**
* May overfit if data is messy due to adding more decision trees to the algorithm for the best result.

**Our Model at Work**
![Image](Resources/Image.png)

## Challenges and Recommendations

* Many of our datasets were difficult to clean and did not merge properly with other datasets. Next time, we would use datasets that were more clean to start with. 
* When it came to creating our dashboard, some of our files were too large to work with when building the html page. In the future, we would decrease the size of the file and pare down the data prior to building the html page.
* We had such a large breadth of data from the CDC, so it was hard to tell what was really relevant to our predictive model. In the future, we would try to have a clearer vision of what data is necessary.

## Technology Used:
We used an array of software and analytic tools to complete our project. These resources are depicted and elaborated upon in the link below:

https://github.com/li-emily/Final_Project/blob/main/planning/technology.md

## Visualizations:

The Tableau visuals that range from population, COVID-19 cases, deaths and vaccinations can be seen in the link below:

https://public.tableau.com/app/profile/zina.shah/viz/Dashboard_COVID_16424202837860/Dashboard2?publish=yes

## Dashboard:

* Code utilized to build Dashboard can be found here:
* Conceptualization of Dashboard can be found in the link below: https://docs.google.com/presentation/d/1ALpovgediQ_bLdq4W2oY2uJnHIKJHVdTsb4E91iFyhw/edit#slide=id.p 
* The link to our Heroku Dashboard can be found here: 


## Presentation:

* Our Google Slide Presentation can be found in the link below:

https://docs.google.com/presentation/d/1PIXc8MoQCyhf88awjZfFVZ0AFq4j6_KTh0REr4ba3PE/edit?usp=drive_web&ouid=102424223461130273036


