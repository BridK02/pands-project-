# Analysis of Fisher’s Iris data set
# Author Brid Kennedy


#first thing to is test that I can manipulate the data as a csv file

import csv

#filename = "iris.csv"

#with open(filename, "rt") as csvFile:
   #csvReader = csv.reader(csvFile, delimiter=",")
   #for line in csvReader:
   #print (line[2]) #that works

csv_file = "iris.csv"
txt_file = "Iris.txt"
text_list = []

with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",", 5) #This CSV file contains five 
        #fields: sepallength sepalwidth petallength,petalwidth,class which are delimited by commas. 
        text_list.append(" ".join(line))

with open(txt_file, "w") as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(text_list), 5))
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')

#The above has created a text file that has removed the commas

#All resources seem to point to pandas to group or summarise the variables. I take the variables to mean sepal length, width etc
    


#because I am working with tabular data in Python I will use (import) the Python Data Analysis Library  
#ref https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/
import pandas as pd
#creating a dataframe of the iris csv
iris_df=pd.read_csv("iris.csv")
#testing how the df looks
print (iris_df)

print (iris_df.columns)

print (iris_df.sepallength)
print (iris_df.sepalwidth)
print (iris_df.petallength)
print (iris_df.petalwidth)
print (iris_df['class'])# finding the right syntax to get around class was a half hour I won't get back in my life




