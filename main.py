import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.progressbar import ProgressBar

class LoginScreen(Screen):
    pass

class InstructionScreen(Screen):
    pass

class ProgressScreen(Screen):
    pass

class ResultsScreen(Screen):
    pass

class ProgressBarScreen(Screen):
		pass

class ScreenManagement(ScreenManager):
    pass

app = Builder.load_file("screens.kv")

class ScreensApp(App):
    def build(self):
        return app

ScreensApp().run()
