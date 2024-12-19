##############################
#                            #
#          Developer:        #
#        Limonad_Games       #
#    limonad-games@mail.ru   #
#       version: 1.3.0       #
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
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import psycopg2
    
Window.clearcolor = (100/255, 100/255, 100/255, 1)
Window.icon = 'icon.ico'

red = (255 / 255, 67 / 255, 67 / 255)

class MainScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Main'  
        main_layout = FloatLayout()
        self.add_widget(main_layout)  
         

        
        #Функция кнопки "Регитрация"  
    def register_user(self, *arg):
        try:
            connection = psycopg2.connect(
                host = "127.0.0.1",
                user = "postgres",
                password = "20042006",
                database = "Napominalka"
            )
            cursor = connection.cursor()
            # Проверка существования пользователя  
            cursor.execute("SELECT * FROM users WHERE login = %s AND password = %s", (self.login.text, self.password.text))
            user = cursor.fetchone()
            if user:
                self.login.text = "Пользователь с таким логином и паролем уже зарегестрирован"
                self.password.text = ""
            else:
                cursor.execute("INSERT INTO users (login, password) VALUES (%s, %s)", (self.login.text, self.password.text))
                connection.commit()
                print("Пользователь зарегистрирован успешно.")
                self.manager.current = 'Second'
        except Exception as e:
            print("Ошибка:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение закрыто.")
    
    #Функция кнопки "Вход"              
    def login_user(self, *arg):
        try:
            connection = psycopg2.connect(
                host = "127.0.0.1",
                user = "postgres",
                password = "20042006",
                database = "Napominalka"
            )
            cursor = connection.cursor()      
            # Проверка существования пользователя
            cursor.execute("SELECT * FROM users WHERE login = %s AND password = %s", (self.login.text, self.password.text))
            user = cursor.fetchone()
            
            if user:
                print("Вход выполнен успешно.")
                self.manager.current = 'Second'
            else:
                self.login.text = "Неверный логин или пароль."
                self.password.text = ""
        except Exception as e:
            print("Ошибка:", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение закрыто.")
          
        return 0        


#Открывается файл my.kv
class Container(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Second'
        second_layout = FloatLayout()
        self.add_widget(second_layout)
    #Функция нажатия первой кнопки
    def btn1_pressed(self, *args):
        data = self.ti.text
        tim = self.timer.text
        if (data != ''):
            with open("dd.txt", "a+") as file:
                file.write('Задача: ' + data + '\n')
                file.write('Таймер на: ' + self.timer.text + '\n')
                file.write('\n') 
        t = time.strftime("%H:%M")
        while t != tim:
            t = time.strftime("%H:%M")
            time.sleep(0.1)
            if t == tim:
                break
        sound = SoundLoader.load('20th Century Fox.mp3')
        sound.play()
    
    #Функция нажатия второй кнопки   
    def btn2_pressed(self, *args):
        self.ti.text = ''
        self.timer.text = ''         

    #Функция нажатия третьей кнопки
    def btn3_pressed(self, *args):
        with open("dd.txt", 'r') as file:
            line_count = sum(1 for line in file)
        with open("dd.txt", "r") as file:
            line = file.readlines()[line_count-3]
            self.ti.text = line
        with open("dd.txt", "r") as file:    
            line = file.readlines()[line_count-2]
            self.timer.text = line
                   
    #Функция нажатия четвёртой кнопки
    def btn4_pressed(self, *args):
        with open("dd.txt", "w") as file:
            file.write('')
        self.ti.text = ''
        self.timer.text = ''  

#Создание окна                
class NapominalkaApp(App):
    def build(self):
        self.icon = 'icon1.png'
        sm.add_widget(MainScreen())
        sm.add_widget(Container())
        return sm
    
    def tick(self, *args):
        self.tim1 = time.strftime("%H:%M") 
    
sm = ScreenManager() 

#Запуск программы
if __name__ == '__main__':
    NapominalkaApp().run()
    
