import kivy
import random
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock

class LoginScreen(Screen):
    pass
class InstructionScreen(Screen):
    pass

class ProgressScreen(Screen):
    pass

class ResultsScreen(Screen):
    pass

class ProgressBarScreen(Screen):

    progress_bar = ObjectProperty()

    def __init__(self, **kwa):
        super(ProgressBarScreen, self).__init__(**kwa)

        self.progress_bar = ProgressBar()
        self.popup = Popup(
            title='Download',
            content=self.progress_bar
        )
        self.popup.bind(on_open=self.puopen)
        self.add_widget(Button(text='Download', on_release=self.pop))

    def pop(self, instance):
        self.progress_bar.value = 1
        self.popup.open()

    def next(self, dt):
        if self.progress_bar.value>=100:
            return False
        self.progress_bar.value += 1

    def puopen(self, instance):
        Clock.schedule_interval(self.next, 1/25)

class ScreenManagement(ScreenManager):
    pass

app = Builder.load_file("screens.kv")

class ScreensApp(App):
    def build(self):
        return app

ScreensApp().run()
