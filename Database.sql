CREATE DATABASE python_test;

CREATE TABLE santa_list(
	"id" serial primary key,
	"name" VARCHAR(255),
	"is_nice" boolean
	);
	
INSERT INTO santa_list("name","is_nice")VALUES('Dave',TRUE);
INSERT INTO santa_list("name","is_nice")VALUES('Evan',TRUE);
INSERT INTO santa_list("name","is_nice")VALUES('Luke',FALSE);
INSERT INTO santa_list("name","is_nice")VALUES('Iris',TRUE);
INSERT INTO santa_list("name","is_nice")VALUES('Ayriel',FALSE);