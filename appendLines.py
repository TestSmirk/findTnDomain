
import os,sys
fileName = str(sys.argv[1]).upper()
file = open("modif.txt", "a")
with open(fileName)  as f:
    for i in  f.readlines():
        file.writelines(str(i).strip()+".cc")
        file.write("\n")