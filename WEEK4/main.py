from termcolor import colored
from data_loader import load_data
from analyzer import (
    get_average_salary,
    get_highest_salary,
    get_lowest_salary,
    get_department_count,
    filter_high_salary,
)
from visualizer import (
    plot_department_count,
    plot_salary_distribution
)
from exporter import (
    export_high_salary,
    export_department_summary,
    export_summary
)
#print loaded data 

df = load_data("data/employees.csv")
#data
print (colored("\nData","green"))
print (df)

#display first 5 rows

print (colored("\nFirst 5 employees ","green"))
print (df.head(5))

#display last 5 rows

print (colored("\nLast 5 employees ","green"))
print (df.tail(5))

#display dataset info

print (colored("\nDataset Information ","green"))
print (df.info())

#Statistical summary

print (colored("\nStatistical Summary ","green"))
print (df.describe())

#no of rows and columns

print (colored("\nShape of dataset ","green"))
print (df.shape)

#column names

print (colored("\nColumn ","green"))
print (df.columns)

#average

print (colored("\nAverage salary ","green"))
print (get_average_salary(df))

#Highest salary

print (colored("\nHighest Salary ","green"))
print (get_highest_salary(df))

#lowest salary

print (colored("\nLowest Salary ","green"))
print (get_lowest_salary(df))

#department count

print (colored("\nDepartment count ","green"))
print (get_department_count(df))

#Employees earning above

print (colored("\nEmployees earning above 100000 ","green"))
print (filter_high_salary(df,100000))

#visualization
plot_department_count(df)

plot_salary_distribution(df)

#reports
export_high_salary(df)

export_department_summary(df)

export_summary(df)
