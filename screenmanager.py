import kivy
import codecs
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

u = codecs.open('users.txt', 'r', 'utf-8')
users = u.read().splitlines()
print users

u.close()

sel_user = ''
sel_test = ''

class LoginScreen(Screen):
    pass

class TestScreen(Screen):
    def recordTest(self, testname):
        sel_test = testname

#we are friends, and friendship is forever
class DemoDropDown(Screen):
    def __init__(self, **kwargs):
        super(DemoDropDown, self).__init__(**kwargs)
        d = DropDown()

        for user in users:
            btn = Button(text=str(user), size_hint_y=None, height=35)
            btn.bind(on_press=lambda btn: d.select(btn.text))
            d.add_widget(btn)

        self.mainbutton = Button(text="Select User", size_hint=[.4, .05], pos_hint={'x':.3, 'y':.5})
        self.mainbutton.bind(on_release=d.open)

        d.bind(on_select=lambda d, x: setattr(self.mainbutton, 'text', x))

        self.add_widget(self.mainbutton)
        self.add_widget(Label(text="If the user dropdown isn't appearing, try pressing the refresh button",
                              size_hint=[.4, .15], pos_hint={'x':.3, 'y':.6}))

    def recordUser(self, username):
        sel_user = username

    def refresh(self):
        self.__init__()

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
        self.add_widget(Button(text='Run {}'.format(sel_test), on_release=self.pop,
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

class CreateNewUserScreen(Screen):

    def createNewUser(self, string):
        users.append(string)
        u_w = codecs.open('users.txt', 'w', 'utf-8')
        for x in users:
            x = x + '\n'
            u_w.write(x)


class ScreenManagement(ScreenManager):
    pass

app = Builder.load_file("tests.kv")

class TestApp(App):
    def build(self):
        return app

if __name__ == '__main__':
    TestApp().run()