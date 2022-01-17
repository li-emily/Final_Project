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

Most of our datasets came from various CDC sources. Due to the vast amount of data, we had to do some significant cleaning before we were able to use it for our machine learning model. There was a lot of data that we had to remove since it did not correlate to our project's main focus. There were missing and null values. We had to merge various CSV files by date, state and county. Overall, we managed to get a clean dataset to proceed with our analysis.
 
## Machine Learning Model

**Benefits of our Model**
* Collection of prediction trees helps estimate variable importance and can handle big data with multiple variables quickly.

**Steps Taken
* Removed features so the model was not so crowded. 
* Trained with a large dataset to help the algorithm. 
* Limited n estimators.

**Limitations of Our Model**
* May overfit if data is messy due to adding more decision trees to the algorithm for the best result.

**Why We Chose Our Model
* Our final question based on our available data was to predict a binary outcome: would these certain factors cause death from COVID-19. Thus random forest was a good model to choose.

**Our Model at Work**
[!Image](Resources/Image.png)

## Technology Used:
We used a variety of technologies to complete our project, which are shown in the link below:

https://github.com/li-emily/Final_Project/blob/main/planning/technology.md

## Visualizations:
The tableau visuals that range from population, COVID-19 cases, deaths and vaccinations can be seen in the link below:

* https://github.com/li-emily/Final_Project/blob/main/Visuals/visualizations.md

## Dashboard:

* Code utilized to build Dashboard can be found under the Flask folder of the repository.
* Conceptualization of Dashboard can be found in the link below:
Hosted at https://docs.google.com/presentation/d/1ALpovgediQ_bLdq4W2oY2uJnHIKJHVdTsb4E91iFyhw/edit#slide=id.p 

## Presentation:

* Our Google Slide Presentation can be found in the link below:

**Challenges and Recommendations**

* Many of our datasets were difficult to clean and did not merge properly with other datasets. Next time, we would use datasets that were more clean to start with. 
* When it came to creating out dashboard, some of our files were too large to work with when building the html page. In the future, we would decrease the size of the file and pare down the data prior to building the html page.
* We had such a large breadth of data from the CDC, so it was hard to tell what was really relevant to our predictive model. In the future, we would try to have a clearer vision of what data is necessary.


**Conclusion**
