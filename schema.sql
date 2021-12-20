-- Created Database
CREATE DATABASE COVID_Vaccination_Study

-- Created Table containing preliminary data for COVID Vaccination study

CREATE TABLE Vaccination_Data 
	(state_name varchar, 
	 county_name varchar,
	 num_vaccinations float, 
	 per_capita_income float, 
	 sociodemographic_barriers varchar, 
	 health_access_barriers varchar
	);

CREATE TABLE per_capita_income 
    (county_name varchar, 
    income_2018 float, 
    income_2019 float, 
    income_2020 float
    );

COPY per_capita_income_counties(county, income_2018, income_2019, income_2020)
FROM '/Users/zina/Desktop/Final Project Data/per_capita_income_counties.csv'
DELIMITER ','
CSV HEADER;    
