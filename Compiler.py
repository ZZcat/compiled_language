filename = "a.txt"
filename_start,trash = filename.split('.')
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
            #print value
            try:
                int(value)+1
                # "int"
                constants.extend([value])
            except:
                if value.isalpha() == True:
                    # "Var"
                    variables.extend([value])
                else:
                    pass
                    # "Command"
constants = list(set(constants))
variables = list(set(variables))
memery = constants
memery.extend(variables)
print memery
with open(filename_start+"_mem.txt", "w") as file:
    for memery_part in memery:
        file.write(memery_part+"\n")
    file.close()


line_number = -1
program = ""
for line in data.split('\n'):
    line_number = line_number+1
    if line_number > 1:
        line_parts = line.split(' ')
        command,values = line_parts
        program = program + command,
        for value in values.split(','):
            try:
                int(value)+1
                program = program + str(bin(memery.index(value))),
            except:
                if value.isalpha() == True:
                    program = program + str(bin(memery.index(value))),
                else:
                    program = program + value,
            program = program + ",",
        program = program + ""
print program
