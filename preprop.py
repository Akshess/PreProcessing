import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# Load the dataset
data = pd.read_csv('student.csv')
# printing original dataset
print(data)
# Data cleaning
data = data.dropna() # Remove rows with missing values
# Remove duplicate names
data = data.drop_duplicates(subset='Name')
# print the dataset after cleaning
print("\n",data)
# Data transformation ie, Scale numerical features
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data[['Age', 'GPA']])
data[['Age', 'GPA']] = scaled_data
# Data integration
# Combining columns 'Name' and 'Grade' into a new column 'Student_Info'
data['Student_Info'] = data['Name'] + ' (' + data['Grade'] + ')'
# Print the preprocessed data
print("\n",data.head())
