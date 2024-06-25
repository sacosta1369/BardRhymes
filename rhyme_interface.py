import kivy
import random

from kivy.app import App
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.uix.button import Button

red = [1, 0, 0, 1]  
green = [0, 1, 0, 1]  
blue = [0, 0, 1, 1]  
purple = [1, 0, 1, 1]  

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        title = MDLabel(text='Bardic Rhymes', pos_hint={'center_x':0.9, 'center_y':0.95},
                        theme_text_color="Custom",
                        text_color=(0.5, 0, 0.5, 1),
                        font_style='H3')
        
        cantrips = Button(text = "Cantrips",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (100, 1000),
                    background_color = red)
        
        first = Button(text = "Level 1",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (500, 1000),
                    background_color = green)
        
        second = Button(text = "Level 2",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (900, 1000),
                    background_color = blue)
        
        third = Button(text = "Level 3",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (1300, 1000),
                    background_color = purple)
        
        fourth = Button(text = "Level 4",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (1700, 1000),
                    background_color = red)
        
        fith = Button(text = "Level 5",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (2100, 1000),
                    background_color = green)
        
        sixth = Button(text = "Level 6",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (500, 700),
                    background_color = blue)
        
        seventh = Button(text = "Level 7",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (900, 700),
                    background_color = purple)
        
        eighth = Button(text = "Level 8",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (1300, 700),
                    background_color = red)
        
        nineth = Button(text = "Level 9",
                    font_size="20sp",
                    color = (1, 1, 1, 1),
                    size = (50, 50),
                    size_hint = (.1, .1),
                    pos= (1700, 700),
                    background_color = green)
        
        screen.add_widget(title)
        screen.add_widget(cantrips)
        screen.add_widget(first)
        screen.add_widget(second)
        screen.add_widget(third)
        screen.add_widget(fourth)
        screen.add_widget(fith)
        screen.add_widget(sixth)
        screen.add_widget(seventh)
        screen.add_widget(eighth)
        screen.add_widget(nineth)
        
        return screen
        
    

if __name__ == "__main__":
    
    app = MainApp()
    app.run()