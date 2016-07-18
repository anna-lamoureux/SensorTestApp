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
from kivy.uix.boxlayout import BoxLayout
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

class ResultsScreen(Popup):
    def __init__(self, **kwa):
        super(ResultsScreen, self).__init__(**kwa)
        layout = BoxLayout(orientation='vertical')
        l = Label(text='Here are the results')
        b = Button(text='Close', size_hint=[.2, .075],
            pos_hint={'x':.4, 'y':.5})
        layout.add_widget(l)
        layout.add_widget(b)
        self.popup = Popup(title='Results', content=layout)
        b.bind(on_press=self.popup.dismiss)

    def show(self):
        self.popup.open()

class ProgressBarScreen(Screen):
    progress_bar = ObjectProperty()

    def __init__(self, **kwa):
        super(ProgressBarScreen, self).__init__(**kwa)

        self.progress_bar = ProgressBar()
        self.popup = Popup(
            title='Running, Do Not Exit',
            content=self.progress_bar
        )
        self.popup.bind(on_open=self.puopen)
        layout = BoxLayout(orientation='horizontal', size_hint=[.5, .1],
            pos_hint={'x':.5, 'y':0})
        layout.add_widget(Button(text='Run Current Test', on_release=self.pop))
        self.add_widget(layout)

    def pop(self, instance):
        self.progress_bar.value = 1
        self.popup.open()

    def next(self, dt):
        self.progress_bar.value += 1

    def puopen(self, instance):
        while self.progress_bar.value<100:
            Clock.schedule_once(self.next, 5)
            self.progress_bar.value += 1
        if self.progress_bar.value>=100:
            self.popup.dismiss()
            ResultsScreen().show()

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