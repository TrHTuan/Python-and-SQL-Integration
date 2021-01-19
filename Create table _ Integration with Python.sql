drop database if exists short_gdp_analysis;
create database if not exists short_gdp_analysis;
use short_gdp_analysis;

drop table if exists country_info;
create table country_info
(	country_name varchar(500) not null,
	country_code varchar(4) not null
    );

drop table if exists female_population;
create table female_population
(	country_name varchar(500),
	`1990` varchar(50),
    `2000` varchar(50),
    `2011` varchar(50),
    `2012` varchar(50),
    `2013` varchar(50),
    `2014` varchar(50),
    `2015` varchar(50),
    `2016` varchar(50),
    `2017` varchar(50),
    `2018` varchar(50),
    `2019` varchar(50),
    primary key (country_name)
    );
    
drop table if exists male_population;
create table male_population
(	country_name varchar(500),
	`1990` varchar(50),
    `2000` varchar(50),
    `2011` varchar(50),
    `2012` varchar(50),
    `2013` varchar(50),
    `2014` varchar(50),
    `2015` varchar(50),
    `2016` varchar(50),
    `2017` varchar(50),
    `2018` varchar(50),
    `2019` varchar(50),
    primary key (country_name)
    );

drop table if exists gdp_data;
create table gdp_data
(	country_name varchar(500),
	`1990` varchar(50),
    `2000` varchar(50),
    `2011` varchar(50),
    `2012` varchar(50),
    `2013` varchar(50),
    `2014` varchar(50),
    `2015` varchar(50),
    `2016` varchar(50),
    `2017` varchar(50),
    `2018` varchar(50),
    `2019` varchar(50),
    primary key (country_name)
    );


