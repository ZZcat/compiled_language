#qpy:kivy
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from multiprocessing.connection import Client

# This callback will be bound to the LED toggle and Beep button:
def press_callback(obj):
    print("Button pressed,", obj.text)
    if obj.text == 'Open connection':
        if obj.state == "down":
            address = ('192.168.253.101', 6001)
            global conn
            global conn_open
            conn_open = 1
            conn = Client(address, authkey='iLikeFatCats! bc8719873v4yb9c8yc8n2b98c927b618v7c8')
            global conn
            global conn_open
            conn.send('open')
        else:
            conn_open = 0
            conn.send('close')
            conn.close()
    elif obj.text == 'Blue':
        if obj.state == "down":
            pass
        else:
            pass
    if 1:
        try:
            if conn_open == 1:
                global conn_open
                global conn
                if obj.state == "down":
                    conn.send(obj.text+str(0))
                else:
                    conn.send(obj.text+str(1))
        except:
            pass


# This is called when the slider is updated:
def update_speed(obj, value):
    print "update"
class MyApp(App):
    
    def build(self):
        # Set up the layout:
        layout = GridLayout(cols=5, spacing=30, padding=30, row_default_height=150)
        
        # Make the background gray:
        with layout.canvas.before:
            Color(.2,.2,.2,1)
            self.rect = Rectangle(size=(800,600), pos=layout.pos)
        

        connB = ToggleButton(text="Open connection")
        connB.bind(on_press=press_callback)
        
        
        a = ToggleButton(text="D0")
        a.bind(on_press=press_callback)
        b = ToggleButton(text="D1")
        b.bind(on_press=press_callback)
        c = ToggleButton(text="D2")
        c.bind(on_press=press_callback)
        d = ToggleButton(text="D3")
        d.bind(on_press=press_callback)
        e = ToggleButton(text="D4")
        e.bind(on_press=press_callback)
        f = ToggleButton(text="D5")
        f.bind(on_press=press_callback)
        g = ToggleButton(text="D6")
        g.bind(on_press=press_callback)
        h = ToggleButton(text="D7")
        h.bind(on_press=press_callback)
        i = ToggleButton(text="A0")
        i.bind(on_press=press_callback)
        j = ToggleButton(text="A1")
        j.bind(on_press=press_callback)
        k = ToggleButton(text="A2")
        k.bind(on_press=press_callback)
        l = ToggleButton(text="A3")
        l.bind(on_press=press_callback)
        m = ToggleButton(text="A4")
        m.bind(on_press=press_callback)
        n = ToggleButton(text="A5")
        n.bind(on_press=press_callback)
        o = ToggleButton(text="A6")
        o.bind(on_press=press_callback)
        p = ToggleButton(text="A7")
        p.bind(on_press=press_callback)
        q = ToggleButton(text="CE")
        q.bind(on_press=press_callback)
        r = ToggleButton(text="OW")
        r.bind(on_press=press_callback)
        s = ToggleButton(text="WE")
        s.bind(on_press=press_callback)
        ard = ToggleButton(text="Blue")
        ard.bind(on_press=press_callback)
##        u = ToggleButton(text="D4")
##        u.bind(on_press=press_callback)
##        v = ToggleButton(text="D5")
##        v.bind(on_press=press_callback)
##        w = ToggleButton(text="D6")
##        w.bind(on_press=press_callback)
##        x = ToggleButton(text="D7")
##        x.bind(on_press=press_callback)
        
    
#        timeSlider = Slider(orientation='vertical', min=1, max=30, value=speed)
#        timeSlider.bind(on_touch_down=update_speed, on_touch_move=update_speed)

        buttons = [connB,ard,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s]
        for b in buttons:
            layout.add_widget(b)
        
        return layout

if __name__ == '__main__':
    MyApp().run()
