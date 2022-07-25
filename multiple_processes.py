import pandas as pd
from main import filetransformer
from multiprocessing.pool import ThreadPool

# Define variables for :

# Where files are coming from
inputfile_path = "C:/Users/matia/Downloads" # path for input files

# What they are called
inputfile_name = ['Filename1', 'Filename2', 'Filename3', ...] # Create list of file names

# Where the new manipulated files will go
outputfile_path = "C:/Users/matia/function_output" # path where output files will be stored


#### For 20 files or under ####

for i in inputfile_name:
    filetransformer(inputfile_path, i, outputfile_path)


#### For 100 - 1000 files ####

# Declare the number of threads to use for running function in parallel

pool = ThreadPool(processes=8)

inputlist = []
for i in inputfile_name:
    fileinput = [inputfile_path, i, outputfile_path]
    inputlist.append(fileinput)

# Run the transformer function across multiple threads in parallel

