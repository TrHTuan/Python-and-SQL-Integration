import pandas as pd
import pymysql
import numpy as np

#Note: need to clean up column name to integrate to MySQL server (i.e: remove space between words, drop unusable columns)
country_info = pd.read_csv(r"[File path]\Country and country code.csv")
female_population = pd.read_csv(r"[File path]\Female population.csv")
male_population = pd.read_csv(r"[File path]\Male population.csv")
gdp_data = pd.read_csv(r"[File path]\GDP listing by year and country.csv")

#Set pandas display option
pd.set_option('display.max_columns',None,'display.max_rows',10)

#Clean up
country_info = country_info.rename(columns = {'Country Name':'country_name','Country Code':'country_code'})
female_population = female_population.drop(['Unnamed: 5','2020'], axis = 1).drop(264).replace({'..':None})
female_population = female_population.rename(columns = {' ':'country_name'})
male_population = male_population.drop(['Unnamed: 5','2020'], axis = 1).drop(264).replace({'..':None})
male_population = male_population.rename(columns = {' ':'country_name'})
gdp_data = gdp_data.drop(['Unnamed: 4','2020'], axis =1).drop(264).replace({'..':None})
gdp_data = gdp_data.rename(columns = {' ':'country_name'})

#Create total_population table:
total_population = pd.DataFrame(columns = female_population.columns)
total_population['country_name'] = female_population['country_name']
for i in (female_population.drop('country_name', axis = 1).columns):
    for j in range(female_population.shape[0]):
        total_population[i][j] = float(female_population[i][j].replace(',','')) + float(male_population[i][j].replace(',',''))

#Create gender_ratio table:
gender_ratio_f2m = pd.DataFrame(columns = female_population.columns)
gender_ratio_f2m['country_name'] = female_population['country_name']
for i in (female_population.drop('country_name', axis = 1).columns):
    for j in range(female_population.shape[0]):
        gender_ratio_f2m[i][j] = float(female_population[i][j].replace(',',''))/float(male_population[i][j].replace(',',''))

#Create connection to MySQL server:
con_sql = pymysql.connect(database = 'short_gdp_analysis', user = [SQL server name], password = [SQL server password])
csr = con_sql.cursor()

def data_transfer(table_name):
    name = [x for x in globals() if globals()[x] is table_name][0]
    insert_data = 'Insert into `%s' %name +'` values'
    for i in range(table_name.shape[0]):
        insert_data += '("'
        for j in range(table_name.shape[1]):
            insert_data += str(table_name.iloc[i][j]) + '","'
        insert_data = insert_data[:-2] + "),"
    insert_data = insert_data[:-1] + ';'
    csr.execute(insert_data)
    con_sql.commit()

data_transfer(country_info)
data_transfer(female_population)
data_transfer(male_population)
data_transfer(gdp_data)
data_transfer(total_population)
data_transfer(gender_ratio_f2m)

#Close connection:
con_sql.close()
