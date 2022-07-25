# Process and support 100-1000 files of volume

from main import filetransformer
from multiprocessing.pool import ThreadPool

# Define Variables
inputfile_path_ = "C:/Users/User/FilePath"


inputfile_name_ = ['Filename1', 'Filename2', 'Filename3', ...]


outputfile_path_ = "C:/Users/User/FileFolder"

#### For 100 - 1000 files ####

# Declare the number of threads to use for running function in parallel

pool = ThreadPool(processes=4)

inputlist_ = []
for i in inputfile_name_:
    fileinput = [inputfile_path_, i, outputfile_path_]
    inputlist_.append(fileinput)

# Run the transformer function across multiple threads in parallel
pool.map(filetransformer, inputlist_)
pool.close()
pool.join()
