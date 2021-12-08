import pandas as pd
data =pd.read_csv(r"C:\Users\hp\Downloads\3. Police Data.csv")
print(data)
#removing the column having all null values
print(data.isnull().sum())
data.drop(columns = 'country_name' ,inplace= True)
print(data.info())

#How many men and women are stopped for violation of speeding
print(data[data.violation=="Speeding"].driver_gender.value_counts())

#how many males and females are searched after stopping

#so for this groupby command is used so that the groups on the basis of the male and female get formed
print(data.groupby("driver_gender").search_conducted.sum())

#getting the records of the male driver having age less than the 22
print(data[(data.driver_gender=='M')& (data.driver_age<22.0)])

#how many less than 22 year old people are stopped for violation
print(data[data.driver_age<=22.0].violation.value_counts())

#How many instances  the female has been arrested
print(data[(data.driver_gender =='F')&(data.stop_outcome == "Arrest Driver")])

#How many times the driver less than 22 years of has been arrested
print(data[data.driver_age<22.0].is_arrested.value_counts())

#how may times the female driver less than 22 years of age is arrested for speeding
print(data[(data.driver_gender =='F')&(data.driver_age<22.0)&(data.violation=="Speeding")].is_arrested.sum())

#calculating the mean of stop duration
data["stop_duration"]=data["stop_duration"].map({'0-15 Min':7.5,'16-30 Min':24, '30+ Min':45})
print(data.stop_duration.mean())

#age distribution for each violation
print(data.groupby("violation").driver_age.describe())
