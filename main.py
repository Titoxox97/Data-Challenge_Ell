import pandas as pd
import csv

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

# Create data set out of dictionaries that will be used to loop through the data and apply conditions

testds = [{'TestType': 'MCAS ELA', 'Date': '04-01', 'Subject': 'Ela', 'Performance': i['eperf2'], 'Scaled Score': i['escaleds'], 'CPI': i['ecpi']},
          {'TestType': 'MCAS Math', 'Date': '05-01', 'Subject': 'Math', 'Performance': i['mperf2'], 'Scaled Score': i['mscaleds'], 'CPI': i['mcpi']},
          {'TestType': 'MCAS Science', 'Date': '06-01', 'Subject': 'Science', 'Performance': i['sperf2'], 'Scaled Score': i['sscaleds'], 'CPI': i['scpi']}]

# Create loop within a loop to filter through conditions and grab the data we are calling

for i in File1:
    for j in testds:
        newrow = {}
        newrow["NCESID"] = 373737
        newrow['StudentLocalId'] = None
        newrow['StudentTestId'] = i['sasid']
        newrow['StudentGradeLevel'] = i['stugrade']
        newrow['TestDate'] = j['Date']
        newrow['TestName'] = 'Macs'
        newrow['TestTypeName'] = j['Name']
        newrow['TestSubjectName'] = j['Subject']
        newrow['TestGradeLevel'] = i['stugrade']
        newrow['Score1Label'] = 'Performance Level'
        newrow['Score1Type'] = 'Level'

        # Performance score value conditions

        if j['Performance'] == 'F':
            newrow['Score1Value'] = '1-F'
        elif j['Performance'] == 'W':
            newrow['Score1Value'] = '2-W'
        elif j['Performance'] == 'NI':
            newrow['Score1Value'] = '3-NI'
        elif j['Performance'] == 'P':
            newrow['Score1Value'] = '4-P'
        elif j['Performance'] == 'A':
            newrow['Score1Value'] = '5-A'
        elif j['Performance'] == 'P+':
            newrow['Score1Value'] = '6-P+'
        else:
            newrow['Score1Value'] = None
        newrow['Score2Label'] = 'Scaled Score'
        newrow['Score2Type'] = 'Scale'
        if j['ScaledScore'] ==' ':
            newrow['Score2Value'] = None
        else:
            newrow['Score2Value'] = j['ScaledScore']
        newrow['Score3Label'] = 'CPI'
        newrow['Score3Type'] = 'Scale'
        if j['CPI'] == ' ':
            newrow['Score3Value'] = None
        else:
            newrow['Score3Value'] = j['CPI']











