import kivy
import random
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.progressbar import ProgressBar
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.textinput import TextInput

class LoginScreen(Screen):
    pass

class TestScreen(Screen):
    def saveTest(self, testname):
        print('Selected Test: {test}'.format(test=testname))

class UserScreen(Screen):
    def saveUser(self, username):
        print('Selected User: {user}'.format(user=username))

class ProgressBarScreen(Screen):
    progress_bar = ObjectProperty()

    def __init__(self, **kwa):
        super(ProgressBarScreen, self).__init__(**kwa)

        self.progress_bar = ProgressBar()
        self.popup = Popup(
            title='Instructions',
            content=self.progress_bar
        )
        self.popup.bind(on_open=self.puopen)
        self.add_widget(Label(text='Here are the directions as to how to set up the test equipment.',
                              size_hint=[.8, .9], pos_hint_x={'x':.1}))
        self.add_widget(Button(text='Run Test', on_release=self.pop, size_hint=[.4, .05], pos_hint={'x':.3, 'y':.1}))

    def pop(self, instance):
        self.progress_bar.value = 1
        self.popup.open()

    def next(self, dt):
        if self.progress_bar.value>=100:
            return False
        self.progress_bar.value += 1

    def puopen(self, instance):
        Clock.schedule_interval(self.next, 1/25)

class CreateNewUserScreen(Screen):

    def createNewUser(self, string):
        print('Newly Created User: {}'.format(string))


class ScreenManagement(ScreenManager):
    pass

app = Builder.load_file("tests.kv")

class TestApp(App):
    def build(self):
        return app

if __name__ == '__main__':
    TestApp().run()