import pandas as pd
import csv

# initialize data frames
df = pd.read_csv("C:/Users/matia/OneDrive/Desktop/Ellevation-Data-Question/sample-mcas-processed.csv")
df2 = pd.read_csv("C:/Users/matia/OneDrive/Desktop/Ellevation-Data-Question/sample-mcas.csv")

# open file for reading and establish parameters
list = []
with open("C:/Users/matia/OneDrive/Desktop/Ellevation-Data-Question/sample-mcas.csv", 'r') as read_file:
    data = csv.reader(read_file, delimiter=',')
    for row in range(len(data)):
        if row > 0:
            mydict = {}
            mydict[list[0][0]] = row[0]

for i in range(len(list[0])):
    if i > 0:
        for j in range(len(list[0])):
            mydict = {}
            mydict[list[0][0]] = list[i][0]
            mydict[list[0][0]] = list[i][1]
            mydict[list[0][0]] = list[i][2]

