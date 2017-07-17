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
        if command.lower() == "set":
            print line_parts
            print values
        else:
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
memery = variables
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
        if command.lower() == "set":
            print line_parts
        else:
            program = program + command
            program = program + " "
            for value in values.split(','):
                try:
                    int(value)+1
                    program = program + value
                except:
                    if value.isalpha() == True:
                        program = program + value
                        #program = program + ("{0:b}".format(memery.index(value)))
                    else:
                        program = program + value
                program = program + ","
            program = program + "\n"
program_new = ""
for program_line in program.split('\n'):
    program_new = program_new+program_line[:-1]+"\n"


line_number = 1
for line in program_new.split('\n'):
    line_number = line_number+1
    if line_number > 1:
        try:
            line_parts = line.split(' ')
            command,values = line_parts
            command = command.lower()
            if command == "set":
                print "set",values # Fix in compiler var define
 #               newcontents = contents.replace('a','e')
                file = open(filename_start+"_mem.txt", "r+") 
                data = file.read()
                print "aaaaa"
                print (values.split(',')[0])
                print (values.split(',')[1])
                data = data.replace((values.split(',')[0]),(values.split(',')[1]))
                file.close()
        except:
            pass
line_number = 1
for line in program_new.split('\n'):
    line_number = line_number+1
    if line_number > 1:
        try:
            line_parts = line.split(' ')
            command,values = line_parts
            command = command.lower()
            if command == "add":
                print "0110 0000"
                print "0010", (values.split(',')[0]).zfill(4) 
                abc= (values.split(',')[0])
                print "0011", (values.split(',')[1]).zfill(4)
                print "0100", (values.split(',')[2]).zfill(4)
            elif command == "sub":
                print "0110 0001"
                print "0010", (values.split(',')[0]).zfill(4) 
                abc= (values.split(',')[0])
                print "0011", (values.split(',')[1]).zfill(4)
                print "0100", (values.split(',')[2]).zfill(4)
            elif command == "stop":
                print "0000 0000"
            elif command == "while":
                pass
            elif command == "forever":
                pass
            elif command == "if":
                pass
            elif command == "out":
                for value in values.split(','):
                    print "0010 ",
                    print value.zfill(4)
                print "0111 0000"
            elif command == "clear":
                print "0111 0011"
            elif command == "set--":
                print "set",values # Fix in compiler var define
 #               newcontents = contents.replace('a','e')
                file = open(filename_start+"_mem.txt", "r+") 
                data = file.read()
                print "aaaaa"
                print (values.split(',')[0])
                print (values.split(',')[1])
                data = data.replace((values.split(',')[0]),(values.split(',')[1]))
                file.close()
        except:
            pass #empty line
        
        
