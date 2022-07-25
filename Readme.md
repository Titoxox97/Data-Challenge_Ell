 # Data Challenge: Ellevation Education
 
# Instructions
<p>
Process the “sample-mcas.csv” file once so it aligns with the data format
found in “sample-mcas-processed.csv”. Then modify your workflow to support an imagined volume of
20 similar files a day. How would you change the processing to accommodate this rate (20 files a day)?
What about for 100 files a day? 1000? 
</p>


# Scenario

<p>
The Ellevation platform can automatically bulk import student data from a school district’s School
Information System (SIS), an extensive operational database. This allows a teacher to view a student
record in the Ellevation platform without having to manually enter information already housed in the SIS.
In this scenario, Ellevation needs to process annual assessment scores for a client. “sample-mcas.csv”
is an MCAS CSV file in the source format determined by the state of Massachusetts. Before our
application can import the data, it needs to be manipulated in accordance with our internal canonical
template.
“sample-mcas-processed.csv” is an example of a transformed output file and there are further
specifications on the next page. For this scenario, the only pertinent tests are MCAS ELA, MCAS Math,
and MCAS Science.
</p>

# Specifics

NCESID: District unique identifier; Default to 373737</p>
StudentLocalID: Not found in the MCAS format; Default to missing</p>
StudentTestID: SASID field of the MCAS format</p>
StudentGradeLevel: Stugrade field of the MCAS format; Grade level when student originally took the
test</p>
TestDate: Date test was administered; Not found in the MCAS format; Default to April 1 for MCAS ELA;
Default to May 1 for MCAS Math; Default to June 1 for MCAS Science</p>
TestName: Test cluster; Default to MCAS</p>
TestTypeName: Test name within cluster; Default to MCAS ELA, MCAS Math, or MCAS Science</p>
In the source file, each record associates a student with 1 to 3 test results. For the processed file, each
record should associate a student to exactly one test result. In other words, for each student, there
should be a record for each existing test result (MCAS ELA, MCAS Math, MCAS Science).</p>
TestSubjectName: Test subject associated with name; Default to ELA, Math, or Science</p>
TestGradeLevel: Grade level for which the test was intended; Default to Stugrade field of the MCAS</p>
format</p>
ScoreLabel: Score type associated with each subject; Default to Performance Level, Scaled Score, or
CPI</p>
ScoreType: Default to Level for Performance Level; Default to Scale for Scaled Score; Default to Scale
for CPI</p>
ScoreValue: Value of a score type</p>
Performance Level values can be found in fields “eperf2”, “mperf2”, and “sperf2” for ELA, Math, and
Science, respectively.</p>
Scaled Score values can be found in “escaleds”, “mscaleds”, and “sscaleds” for ELA, Math, and
Science, respectively. CPI values can be found in “ecpi”, “mcpi”, and “scpi” for ELA, Math, and Science,
respectively.</p>
CPI and Scaled values can be brought in directly, but Performance Level values need to be mapped
according to the code reference below.</p>

<p>F >> 1-F</p>
W >> 2-W</p>
NI >> 3-NI</p>
P >> 4-P</p>
A >> 5-A</p>
P+ >> 6-P</p>

# Author 

Matias David Arce Ahrensdorf