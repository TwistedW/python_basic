import pandas as pd #import module

#read csv
data = pd.read_pickle('student.pickle')

#print data
print(data)

#save the file to pickle
data.to_csv('students.csv')