from Tkinter import *

def save():
    data = text_area.get("1.0",END)
    result.set('Lines: '+str(len(data.split('\n'))-1))
    print data,
    filename = data.split('\n', 1)[0]
    filename = filename.split(" ", 1)[1]
    print filename
def open():
    print "Open"
    
window = Tk()

frame=Frame(window)
frame.pack()

text_area = Text(frame)
text_area.pack()

result = StringVar()
result.set('')
label=Label(window,textvariable=result)
label.pack()

button=Button(window,text="Open", command=open)
button.pack()
button=Button(window,text="Save", command=save)
button.pack()

window.mainloop()
