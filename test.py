# Native python method used to import dataframes, open and read csv file


# initialize data frames
df = pd.read_csv("C:/Users/matia/OneDrive/Desktop/Ellevation-Data-Question/sample-mcas-processed.csv")
df2 = pd.read_csv("C:/Users/matia/OneDrive/Desktop/Ellevation-Data-Question/sample-mcas.csv")

# open file for reading and establish parameters
list = []
with open("C:/Users/matia/OneDrive/Desktop/Ellevation-Data-Question/sample-mcas.csv", 'r') as read_file:
    data = csv.reader(read_file, delimiter=',')
    for row in data:
        list.append(row)

list2 = []
for i in range(len(list)):
    if i > 0:
        mydict = {}
        for j in range(len(list[0])):
            mydict[list[0][j]] = list[i][j]
    list2.append(mydict)


File1 = list2