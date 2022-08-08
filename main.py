####### Function that will loop through data and apply the  #######
####### applicable parameters #######

import pandas as pd
import csv

# Create function using only local variables
def filetransformer(file):
    filepath = file[0]
    filename = file[1]
    newfilepath = file[2]
    print('File starting')
    filep_filen = filepath + '/' + filename
    file1 = pd.read_csv(filep_filen)
    file1 = file1.to_dict('records')

# Create data set out of dictionaries that will be used to loop through the data and apply conditions

    dataset = []
    for i in file1:
        testds = [{'TestType': 'MCAS ELA', 'Date': '04-01', 'Subject': 'Ela', 'Performance': i['eperf2'], 'ScaledScore': i['escaleds'], 'CPI': i['ecpi']},
                  {'TestType': 'MCAS Math', 'Date': '05-01', 'Subject': 'Math', 'Performance': i['mperf2'], 'ScaledScore': i['mscaleds'], 'CPI': i['mcpi']},
                  {'TestType': 'MCAS Science', 'Date': '06-01', 'Subject': 'Science', 'Performance': i['sperf2'], 'ScaledScore': i['sscaleds'], 'CPI': i['scpi']}]

# Create loop within a loop to filter through conditions and grab the data we are calling

        for j in testds:
            newrow = {}
            newrow["NCESID"] = 373737
            newrow['StudentLocalId'] = None
            newrow['StudentTestId'] = i['sasid']
            newrow['StudentGradeLevel'] = i['stugrade']
            newrow['TestDate'] = j['Date']
            newrow['TestName'] = 'MCAS'
            newrow['TestTypeName'] = j['TestType']
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
            if j['ScaledScore'] == ' ':
                newrow['Score2Value'] = None
            else:
                newrow['Score2Value'] = j['ScaledScore']
            newrow['Score3Label'] = 'CPI'
            newrow['Score3Type'] = 'Scale'
            if j['CPI'] == ' ':
                newrow['Score3Value'] = None
            else:
                newrow['Score3Value'] = j['CPI']
            dataset.append(newrow)

    df = pd.DataFrame(dataset)
    df.to_csv(newfilepath + '/' + filename[:-4] + '-processed.csv')
    print('File finished')
    return df










