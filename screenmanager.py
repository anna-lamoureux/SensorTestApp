import kivy
import random
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.progressbar import ProgressBar
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock

class LoginScreen(Screen):
    pass

class TestScreen(Screen):
    pass

class UserScreen(Screen):
    pass

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
        self.add_widget(Button(text='Run Current Test', on_release=self.pop,
            size_hint=[.4, .05], pos_hint={'x':.3, 'y':.1}))

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

class ScreenManagement(ScreenManager):
    pass

app = Builder.load_file("tests.kv")

class TestApp(App):
    def build(self):
        return app

if __name__ == '__main__':
    TestApp().run()