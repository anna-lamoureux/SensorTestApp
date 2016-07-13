from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown

Builder.load_string("""
<Phone>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, 1
            id: _screen_manager
            Screen:
                name: 'welcome'
                Label:
                    markup: True
                    text: '[size=24]Welcome to [color=dd88ff]THE APP[/color][/size]'

                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'bottom'

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint: 1, .1
                        Button:
                            text: 'Exit'
                            on_press: _screen_manager.current = 'welcome'
                        Button:
                            text: 'Login'
                            on_press: _screen_manager.current = 'login'

            Screen:
                name: 'tests'
                FloatLayout:
                    size: 300, 300
                    padding: 50
                    TestDropDown:
                        id: tests
                        text: "Select Test"
                        pos_hint: {'x':.3, 'y':.5}
                        size_hint: .4, .1

                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'bottom'

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint: 1, .1
                        Button:
                            text: 'Back to Login'
                            on_press: _screen_manager.current = 'login'
                        Button:
                            text: 'Start Test'
                            on_press: _screen_manager.current = 'tests'

            Screen:
                name: 'login'
                FloatLayout:
                    size: 300, 300
                    padding: 50
                    UserDropDown:
                        id: users
                        text: "Select User"
                        pos_hint: {'x':.3, 'y':.5}
                        size_hint: .4, .1

                    Button:
                        text: "Create New User"
                        on_press: _screen_manager.current = 'welcome'
                        pos_hint: {'x':.5, 'y':.45}
                        size_hint: .2, .05

                AnchorLayout:
                    anchor_x: 'center'
                    anchor_y: 'bottom'

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint: 1, .1
                        Button:
                            text: 'Exit'
                            on_press: _screen_manager.current = 'welcome'
                        Button:
                            text: 'Choose Test'
                            on_press: _screen_manager.current = 'tests'

<UserDropDown>:
    Button:
        id: btn1
        text: 'Select User'
        on_press: userdropdown.open(self)
        size_hint_y: None
        height: '48dp'

    DropDown:
        id: userdropdown
        on_parent: self.dismiss()
        on_select: btn1.text = '{}'.format(args[1])

        Button:
            text: 'User 1'
            size_hint_y: None
            height: '48dp'
            on_press: userdropdown.select('User 1')

        Button:
            text: 'User 2'
            size_hint_y: None
            height: '48dp'
            on_press: userdropdown.select('User 2')

<TestDropDown>:
    Button:
        id: btn2
        text: 'Select Test'
        on_press: testdropdown.open(self)
        size_hint_y: None
        height: '48dp'

    DropDown:
        id: testdropdown
        on_parent: self.dismiss()
        on_select: btn2.text = '{}'.format(args[1])

        Button:
            text: 'Test 1'
            size_hint_y: None
            height: '48dp'
            on_press: testdropdown.select('Test 1')

        Button:
            text: 'Test 2'
            size_hint_y: None
            height: '48dp'
            on_press: testdropdown.select('Test 2')

""")


class Phone(FloatLayout):
    pass


class UserDropDown(DropDown):
    pass


class TestDropDown(DropDown):
    pass


class TestApp(App):
    def build(self):
        return Phone()

if __name__ == '__main__':
    TestApp().run()