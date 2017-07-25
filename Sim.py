print "Starting"

file = open("compile.txt", "r") 
filename = file.read()
file.close()

filename_start = filename.split('.')[0]
file = open(filename, "r") 
data = file.read()
file.close()
       
