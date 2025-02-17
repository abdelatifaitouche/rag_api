from os import listdir
from os.path import isfile, join




onlyfiles = [f for f in listdir("docs") if isfile(join("docs", f))]



for file in onlyfiles : 
    print(file)