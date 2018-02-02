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
            conn = Client(address, authkey='iLikeFatCats! bc8719873v4yb9c8yc8n2b98c927b618v7c8')
            global conn
            conn.send('test')
            conn.send('test2')
        else:
            pass
            conn.send('close')
            conn.close()




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
        
        a = ToggleButton(text="0")
        a.bind(on_press=press_callback)
        b = ToggleButton(text="1")
        b.bind(on_press=press_callback)
        c = ToggleButton(text="2")
        c.bind(on_press=press_callback)
        d = ToggleButton(text="3")
        d.bind(on_press=press_callback)
        e = ToggleButton(text="4")
        e.bind(on_press=press_callback)
        f = ToggleButton(text="5")
        f.bind(on_press=press_callback)
        g = ToggleButton(text="6")
        g.bind(on_press=press_callback)
        h = ToggleButton(text="7")
        h.bind(on_press=press_callback)
        
        
    
#        timeSlider = Slider(orientation='vertical', min=1, max=30, value=speed)
#        timeSlider.bind(on_touch_down=update_speed, on_touch_move=update_speed)

        buttons = [connB,a,b,c,d,e,f,g,h]
        for b in buttons:
            layout.add_widget(b)
        
        return layout

if __name__ == '__main__':
    MyApp().run()
