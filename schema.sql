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
    2018_income float, 
    2019_income float, 
    2020_income float
    );