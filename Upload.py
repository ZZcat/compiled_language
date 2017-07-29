#! /usr/bin/python

print "Loading..."
import serial
from time import sleep
print "Done.\n"

print "Connecting to Device"
bluetoothSerial = serial.Serial( "/dev/tty.zz-DevB", baudrate=9600 )
def b(write_data_def):
    bluetoothSerial.write(str(write_data_def))
print "Done.\n"
print "Setting output to low"
b(str("acegikm"))
print "Done.\n"
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
        pass # Non-int
    if bit == 8:
        b("n") # Enable data
        b("m") # Disable data
        address = address + 1
        bit = 0
        address_bits = ("{0:b}".format(address)).zfill(8)
        if address_bit[0]==0:
            b("g")
            b("f")
            b("e")
        else:
            b("h")
            b("f")
            b("e")
        if address_bit[1]==0:
            b("g")
            b("f")
            b("e")
        else:
            b("h")
            b("f")
            b("e")
        if address_bit[2]==0:
            b("g")
            b("f")
            b("e")
        else:
            b("h")
            b("f")
            b("e")
        if address_bit[3]==0:
            b("g")
            b("f")
            b("e")
        else:
            b("h")
            b("f")
            b("e")
        if address_bit[4]==0:
            b("g")
            b("f")
            b("e")
        else:
            b("h")
            b("f")
            b("e")
        if address_bit[5]==0:
            b("g")
            b("f")
            b("e")
        else:
            b("h")
            b("f")
            b("e")
        if address_bit[6]==0:
            b("g")
            b("f")
            b("e")
        else:
            b("h")
            b("f")
            b("e")
        if address_bit[7]==0:
            b("g")
            b("f")
            b("e")
        else:
            b("h")
            b("f")
            b("e")
        pass
        
            
## Memory
b("jk")

## Instructions
b("jl")

## Done
b("ik")
 
while 1:
    bluetoothSerial.write(str(raw_input(">")))
