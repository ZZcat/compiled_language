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
        if 1 == 0:
            pass
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
memery = constants
memery.extend(variables)
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
        if command.lower() == "setv":
            file = open(filename_start+"_mem.txt", "r+") 
            data = file.read()
            data_new=""
            for data_replace in data.split('\n'):

                if data_replace == values[0]:
                    data_new = data_new + values[2]
                else:
                    data_new = data_new + data_replace
                data_new = data_new + "\n"
            file.seek(0)
            file.truncate()
            file.write(data_new)
            file.close()
        else:
            program = program + command
            program = program + " "
            for value in values.split(','):
                try:
                    int(value)+1
                    program = program + ("{0:b}".format((memery.index(value))))
                except:
                    if value.isalpha() == True:
                        program = program + ("{0:b}".format(memery.index(value)))
                    else:
                        program = program + value
                program = program + ","
            program = program + "\n"
file = open(filename_start+"_mem.txt", "r+") 
data = file.read()
data_new = ""
for data_line in data.split('\n'):
    if not data_line == "":
        try:
            int(data_line)
            data_new = data_new + str(int(data_line))
        except:
            data_new = data_new + str(0)
        data_new = data_new + "\n"
file.seek(0)
file.truncate()
file.write(data_new)
file.close()


program_new = ""
for program_line in program.split('\n'):
    program_new = program_new+program_line[:-1]+"\n"

line_number = -1
for line in program_new.split('\n'):
    line_number = line_number+1
    address = "{0:b}".format(line_number)
    print address.zfill(4)+": ",
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
                while_values = values.split(',')
                while_address = address
            elif command == "whileend":
                if while_value[1] == "=":
                    if while_values[2].isalpha()==True:
                        pass # var
                    else:
                        if while_values[2] == 0:
                            print "0010 ", while_values[0].zfill(4)
                            print "1000 ", while_address
                        else:
                            pass # int
                if while_value[1] == "=!":
                    pass
                if while_value[1] == ">":
                    pass
                if while_value[1] == "<":
                    pass
                
            elif command == "forever":
                pass
            elif command == "if":
                pass
            elif command == "out":
                for value in values.split(','):
                    print "0010 ",value.zfill(4)
                print "0111 0000"
            elif command == "clear":
                print "0111 0011"
            elif command == "set":
                pass
            else:
                print "----UNKNOWN----"
        except:
            pass #empty line
        
        
