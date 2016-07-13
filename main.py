import kivy
import random
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class LoginScreen(Screen):
    pass
class InstructionScreen(Screen):
    pass

class ProgressScreen(Screen):
    pass

class ResultsScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

app = ScreenManager()

class ScreensApp(App):
    def build(self):
        return app

ScreensApp().run()