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