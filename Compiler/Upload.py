        #! /usr/bin/python

while 1:
    try:
        print "Loading..."
        import serial , time, os
        from time import sleep
        print "Done.\n"

        write_wait = 0.5
        signal_wait = 0.1

        print "Connecting to Device"
        bluetoothSerial = serial.Serial("/dev/tty.zz-DevB", baudrate=9600 )
        def b(write_data_def):
            bluetoothSerial.write(str(write_data_def))
            time.sleep(signal_wait)
            print write_data_def
        print "Done.\n"
        print "Setting output to low"
        b(str("acegikn"))
        print "Done.\n"
        time.sleep(20)
        #0 1

        #a b  data_clk
        #c d  data_data
        #e f  address_clk
        #g h  address_data
        #i j  cA
        #k l  cB
        #m n  write signal
        #o p  address_en

        # 1 Write program
        # 2 Write memeory
        # 3 Write instructions

        #   cA cB 
        # 1  0  1
        # 2  1  0
        # 3  1  1


        ## Program
        b("il")

        file = open("compile.txt", "r") 
        filename = file.read()
        file.close()
        filename_start = filename.split('.')[0]
        asm = filename_start+"_asm.txt"
        file = open(asm, "r") 
        data = file.read()
        file.close()
        bit = 0
        address = 0
        for line_bit in data:
            try:
                if int(line_bit) == 1:
                    b("d") # Change data
                    b("b") # Data Clock rise
                    b("a") # Data Clock fall
                else:
                    b("c") # Change data
                    b("b") # Data Clock rise
                    b("a") # Data Clock fall
                bit = bit + 1
            except:
                pass
            if bit == 8:
                print address
                b("m") # Enable data
                time.sleep(write_wait)
                b("n") # Disable data
                bit = 0
                address_bits = ("{0:b}".format(address)).zfill(8)
                print address_bits
                if int(address_bits[0])==0:
                    b("g")
                    b("f")
                    b("e")
                else:
                    b("h")
                    b("f")
                    b("e")
                if int(address_bits[1])==0:
                    b("g")
                    b("f")
                    b("e")
                else:
                    b("h")
                    b("f")
                    b("e")
                if int(address_bits[2])==0:
                    b("g")
                    b("f")
                    b("e")
                else:
                    b("h")
                    b("f")
                    b("e")
                if int(address_bits[3])==0:
                    b("g")
                    b("f")
                    b("e")
                else:
                    b("h")
                    b("f")
                    b("e")
                if int(address_bits[4])==0:
                    b("g")
                    b("f")
                    b("e")
                else:
                    b("h")
                    b("f")
                    b("e")
                if int(address_bits[5])==0:
                    b("g")
                    b("f")
                    b("e")
                else:
                    b("h")
                    b("f")
                    b("e")
                if int(address_bits[6])==0:
                    b("g")
                    b("f")
                    b("e")
                else:
                    b("h")
                    b("f")
                    b("e")
                if int(address_bits[7])==0:
                    b("g")
                    b("f")
                    b("e")
                else:
                    b("h")
                    b("f")
                    b("e")
                print str(address_bits)+"\n"
                address = address + 1
                    
        ## Memory
        b("jk")

        ## Instructions
        b("jl")

        ## Done
        b("ik")
         
        while 1:
            bluetoothSeractal.write(str(raw_input(">")))
    except:
        time.sleep(1)
        print "\n\n"
