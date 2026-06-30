def get_average_salary(df):
	return df["Salary"].mean()

def get_highest_salary(df):
	return df["Salary"].max()

def get_lowest_salary(df):
	return df["Salary"].min()

def get_department_count(df):
	return df["Department"].value_counts()

def filter_high_salary(df,salary):
	return df[df["Salary"] > salary]


