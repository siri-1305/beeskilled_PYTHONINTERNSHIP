def clean_data(df):
	df = df.drop_duplicates() #remove duplicates
	#remove extra spaces from text columns
	df["Name"]=df["Name"].str.strip()
	df["Department"] = df["Department]
	
	#standard dept names
	df["Department"]=df["Department"].str.title()
	return df
	
