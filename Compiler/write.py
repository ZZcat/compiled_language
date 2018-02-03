from Tkinter import *
import os

def save():
    data = text_area.get("1.0",END)
    filename = data.split('\n', 1)[0]
    filename = filename.split(" ", 1)[1]
    print filename
    with open(filename, "w") as file:
        for line in data:
            file.write(line)
        file.close()
    result.set('Lines: '+str(len(data.split('\n'))-1)+" Filename: " + filename)
    file = open("compile.txt", "w") 
    file.write(filename)
    file.close()
    file = open("compile_done.txt", "w") 
    file.write("0")
    file.close()
    os.system("python Compiler.py")
    file = open("compile_done.txt", "r") 
    print file.read()
    file.close()
def fileopen():
    data = text_area.get("1.0",END)
    filename = data.split('\n', 1)[0]
    filename = filename.split(" ", 1)[1]
    file = open(filename, "r") 
    text_area.delete(1.0, END)
    text_area.insert(END, file.read())
    data = text_area.get("1.0",END)
    filename = data.split('\n', 1)[0]
    filename = filename.split(" ", 1)[1]
    result.set('Lines: '+str(len(data.split('\n'))-1)+" Filename: " + filename)

    
window = Tk()
window.wm_title("Program editor")

frame=Frame(window)
frame.pack()

text_area = Text(frame)
text_area.pack()

result = StringVar()
result.set('')
label=Label(window,textvariable=result)
label.pack()

button=Button(window,text="Open", command=fileopen)
button.pack()
button=Button(window,text="Save", command=save)
button.pack()

window.mainloop()
