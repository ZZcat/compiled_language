filename = "a.txt"
file = open(filename, "r") 
data = file.read()
file.close()
line_number = -1
constants = []
variables = []
for line in data.split('\n'):
    line_number = line_number+1
    if line_number > 1:
        line_parts = line.split(' ')
        command,values = line_parts
        for value in values.split(','):
            print value
            try:
                int(value)+1
                print "int"
                constants.extend([value])
            except:
                if value.isalpha() == True:
                    print "Var"
                    variables.extend([value])
                else:
                    print "Command"
print list(set(constants)
print list(set(variables)
