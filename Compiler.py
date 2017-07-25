print "Starting"

file = open("compile.txt", "r") 
filename = file.read()
file.close()

filename_start = filename.split('.')[0]
file = open(filename, "r") 
data = file.read()
file.close()
line_number = -1
constants = []
variables = []
for line in data.split('\n'):
    try:
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
    except:
        pass
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
    try:
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
    except:
        pass
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
print program_new
print "\n\n"
linecount = 0
line_number = 1
file = open(filename_start+"_asm.txt", "w+") 
data = file.read()
file.seek(0)
file.truncate()

loop_values=[]
loop_addresses=[]

for line in program_new.split('\n'):
    line_number = line_number+1
    address = "{0:b}".format(line_number)
    if line_number > 1:
        try:
            line_parts = line.split(' ')
            command,values = line_parts
            command = command.lower()
            print command
            if command == "add":
                file.write("0110 0000")
                file.write("\n")
                print 2
                file.write("0010 "+ (values.split(',')[0]).zfill(4) )
                file.write("\n")
                print 3
                abc= (values.split(',')[0])
                print 99
                file.write("0011 "+ (values.split(',')[1]).zfill(4))
                print 88
                file.write("\n")
                print 4
                file.write("0100 "+ (values.split(',')[2]).zfill(4))
                file.write("\n")
                print 5
                linecount = linecount + 4
            elif command == "sub":
                file.write("0110 0001")
                file.write("\n")
                file.write("0010", (values.split(',')[0]).zfill(4) )
                file.write("\n")
                abc= (values.split(',')[0])
                file.write("0011", (values.split(',')[1]).zfill(4))
                file.write("\n")
                file.write("0100", (values.split(',')[2]).zfill(4))
                file.write("\n")
                linecount = linecount + 4
            elif command == "stop":
                file.write("0000 0000")
                file.write("\n")
                linecount = linecount + 1
            elif command == "while":
                loop_values = loop_values + [values.split(',')]
                loop_addresses = loop_addresses + ["{0:b}".format(linecount+1)]
                linecount = linecount + 0

            elif command == "whileend":
                if loop_values[-1][1] == "=":
                    if 1==1:
                        if loop_values[-1][2] == 0:
                            file.write("0010 "+ loop_values[-1][2].zfill(4))
                            file.write("\n")
                            file.write("1000 "+ loop_addresses[-1].zfill(4))
                            file.write("\n")
                        else:
                            file.write("0110 0001")
                            file.write("\n")
                            file.write("0010 "+ loop_values[-1][2].zfill(4))
                            file.write("\n")
                            file.write("0011 "+ loop_values[-1][0].zfill(4))
                            file.write("\n")
                            file.write("0101 0000")
                            file.write("\n")
                            file.write("1000 "+ loop_addresses[-1].zfill(4))
                            file.write("\n")
                if loop_values[-1][1] == "=!":
                    if 1==1:
                        if loop_values[-1][2] == 0:
                            file.write("0010 "+ loop_values[-1][2].zfill(4))
                            file.write("\n")
                            file.write("1001 "+ loop_addresses[-1].zfill(4))
                            file.write("\n")
                        else:
                            file.write("0110 0001")
                            file.write("\n")
                            file.write("0010 "+ loop_values[-1][2].zfill(4))
                            file.write("\n")
                            file.write("0011 "+ loop_values[-1][0].zfill(4))
                            file.write("\n")
                            file.write("0101 0000")
                            file.write("\n")
                            file.write("1001 "+ loop_addresses[-1].zfill(4))
                            file.write("\n")
                if loop_values[-1][1] == ">":
                    if 1==1:
                        if loop_values[-1][2] == 0:

                            file.write("\n")
                        else:
                            file.write("0110 0001")
                            file.write("\n")
                            file.write("0010 "+ loop_values[-1][2].zfill(4))
                            file.write("\n")
                            file.write("0011 "+ loop_values[-1][0].zfill(4))
                            file.write("\n")
                            file.write("0101 0000")
                            file.write("\n")
                            file.write("1010 "+ loop_addresses[-1].zfill(4))
                            file.write("\n")
                if loop_values[-1][1] == "<":
                    if 1==1:
                        if loop_values[-1][2] == 0:
                            file.write("0010 "+ loop_values[-1][2].zfill(4))
                            file.write("\n")
                            file.write("1011 "+ loop_addresses[-1].zfill(4))
                            file.write("\n")
                        else:
                            print "$$$$"
                            file.write("0110 0001")
                            file.write("\n")
                            file.write("0010 "+ loop_values[-1][2].zfill(4))
                            file.write("\n")
                            file.write("0011 "+ loop_values[-1][0].zfill(4))
                            file.write("\n")
                            file.write("0101 0000")
                            file.write("\n")
                            file.write("1011 "+ loop_addresses[-1].zfill(4))
                            file.write("\n")
                

            elif command == "forever":
                pass
                linecount = linecount + 0
            elif command == "if":
                pass
                linecount = linecount + 0
            elif command == "out":
                for value in values.split(','):
                    file.write("0010 "+value.zfill(4))
                    file.write("\n")
                file.write("0111 0000")
                file.write("\n")
                linecount = linecount + 2
            elif command == "clear":
                file.write("0111 0011")
                file.write("\n")
                linecount = linecount + 1
            elif command == "set":
                values = values.split(',')
                file.write("0100 "+values[1].zfill(4))
                file.write("\n")
                file.write("0010 "+values[0].zfill(4))
                file.write("\n")
                linecount = linecount + 2
            else:
                print "----UNKNOWN----"
        except:
            print "--"
            pass #empty line
file.close()

        
