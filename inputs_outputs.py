#### Pass function through input data ####

from main import filetransformer


inputfile_path = "C:/Users/matia/OneDrive/Desktop/Ellevation-Data-Question" # path for input files
inputfile_name = "sample-mcas.csv" # Create list of file names
outputfile_path = "C:/Users/matia/function_output" # path where output files will be stored

list = [inputfile_path, inputfile_name, outputfile_path]

dataset = filetransformer(list)