#### Pass function through input data ####

from main import filetransformer

inputfile_path = "C:/Users/matia/OneDrive/Desktop/Ellevation-Data-Question" # path for input files
inputfile_name = "sample-mcas.csv" # Create list of file names
outputfile_path = "Users/matia/Desktop" # path where output files will be stored

dataset = filetransformer(inputfile_path, inputfile_name, outputfile_path)