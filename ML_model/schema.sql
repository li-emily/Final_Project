CREATE TABLE total
("County Name" varchar,
 State varchar,
 Date date,
 Cases int,
 Deaths int,
 Series_Complete_Yes numeric,
 Series_Complete_Pop_Pct numeric,
 Administered_Dose1_Pop_Pct	numeric,
 Booster_Doses_Vax_Pct numeric)
;
CREATE TABLE booster
("County Name" varchar,
 State varchar,
 Date	 date,
 Cases	int,
 Deaths	int,
 Series_Complete_Yes	numeric,
 Series_Complete_Pop_Pct	numeric,
 Administered_Dose1_Pop_Pct	numeric,
 Booster_Doses_Vax_Pct numeric)
;
CREATE TABLE no_booster
("County Name" varchar,
 State varchar,
 Date	 date,
 Cases	int,
 Deaths	int,
 Series_Complete_Yes	numeric,
 Series_Complete_Pop_Pct	numeric,
 Administered_Dose1_Pop_Pct	numeric)
;