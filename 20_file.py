# Process and support 20 or less files of volume

from main import filetransformer

# Define variables for :

# Where files are coming from
inputfile_path = "C:/Users/matia/OneDrive/Desktop/Ellevation-Data-Question" # path for input files

# What they are called
inputfile_name = ['Filename1', 'Filename2', 'Filename 3', ...] # Create list of file names

# Where the new manipulated files will go
outputfile_path = "C:/Users/matia/function_output" # path where output files will be stored


#### For 20 files or under ####

for i in inputfile_name:
    filetransformer(inputfile_path, i, outputfile_path)



