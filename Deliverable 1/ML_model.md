Provisional Machine Learning Model Outline

![](https://blogs.sas.com/content/subconsciousmusings/files/2017/04/machine-learning-cheet-sheet-2.png)

[img src](https://blogs.sas.com/content/subconsciousmusings/2020/12/09/machine-learning-algorithm-use)

•	Which model did you choose and why?

We changed our choice from logisitc regression model to random forest model due to the complexity of the data and accuracy that we want to predict future vaccination rates/COVID rates. The data most likely will not be linear, and the otucomes are not binary. 

•	How are you training your model?

This model is trained using CSV datasets which include sociodemographic barriers, vaccinations administered, per capita income, vaccination data from every county and healthcare access barriers retrieved from governmental data sites. 

•	What is the model's accuracy?

It will predict COVID vaccine effectiveness in counties across the US. 
This model will predict the tendency of people getting vaccinated and those that are not based on different datasets, so that a system can be developed to know in what US counties vaccination rates are lowest. Tt will predict output with high accuracy for a large set of data.

•	How does this model work?

Based on the datasets, this model will predict the trend of people that are getting vaccinated. This prediction will be based on different CSV files including counties, demographics and different barriers. The model will be using data from the database in pgAdmin (SQL) called "COVID_Vaccination_Study".
				
