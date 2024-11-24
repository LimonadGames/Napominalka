##############################
#                            #
#          Developer:        #
#        Limonad_Games       #
#    limonad-games@mail.ru   #
#       version: 1.2.0       #
#                            #
##############################

from kivy.config import Config
Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 500)
Config.set("graphics", "height", 900)
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
import time
    
Window.clearcolor = (100/255, 100/255, 100/255, 1)
Window.icon = 'icon.ico'

class Container(FloatLayout):
    
    def btn1_pressed(self, *args):
        data = self.ti.text
        tim = int(self.timer.text)
        if (data != ''):
            with open("dd.txt", "a+") as file:
                file.write('Задача: ' + data + '\n')
                file.write('Таймер на: ' + self.timer.text + ' секунд\n')
                file.write('\n') 
        timing = time.time()
        while True:
            if time.time() - timing > tim:
                timing = time.time()
                break
        sound = SoundLoader.load('20th Century Fox.mp3')
        sound.play()
       
    def btn2_pressed(self, *args):
        self.ti.text = ''
        self.timer.text = ''         

    def btn3_pressed(self, *args):
        with open("dd.txt", 'r') as file:
            line_count = sum(1 for line in file)
        with open("dd.txt", "r") as file:
            line = file.readlines()[line_count-3]
            self.ti.text = line
        with open("dd.txt", "r") as file:    
            line = file.readlines()[line_count-2]
            self.timer.text = line
                   
    def btn4_pressed(self, *args):
        with open("dd.txt", "w") as file:
            file.write('')
        self.ti.text = '' 
                
class MyApp(App):
        
    def build(self):
        self.icon = 'icon1.png'
        self.title = 'Напоминалка'
        return Container()


if __name__ == '__main__':
    MyApp().run()
    