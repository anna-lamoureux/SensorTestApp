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
                Button:
                    id: btn
                    text: 'Select Test'
                    on_release: dropdown.open(self)
                    size_hint: .4, .05
                    pos_hint: {'x':.3, 'y':.5}

                Widget

                DropDown:
                    id: dropdown
                    on_parent: self.dismiss()
                    on_select: btn.text = '{}'.format(args[1])

                    Button:
                        text: 'Test A'
                        size_hint_y: None
                        height: '40dp'
                        on_release: dropdown.select('Test A')

                    Button:
                        text: 'Test B'
                        size_hint_y: None
                        height: '40dp'
                        on_release: dropdown.select('Test B')

                    Button:
                        text: 'Test C'
                        size_hint_y: None
                        height: '40dp'
                        on_release: dropdown.select('Test C')

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
                Button:
                    id: btn2
                    text: 'Select User'
                    on_release: dropdown2.open(self)
                    size_hint: .4, .05
                    pos_hint: {'x':.3, 'y':.5}

                Widget

                DropDown:
                    id: dropdown2
                    on_parent: self.dismiss()
                    on_select: btn2.text = '{}'.format(args[1])

                    Button:
                        text: 'User 1'
                        size_hint_y: None
                        height: '40dp'
                        on_release: dropdown2.select('User 1')

                    Button:
                        text: 'User 2'
                        size_hint_y: None
                        height: '40dp'
                        on_release: dropdown2.select('User 2')

                    Button:
                        text: 'User 3'
                        size_hint_y: None
                        height: '40dp'
                        3on_release: dropdown2.select('User 3')

                Button:
                    text: "Create New User"
                    on_press: _screen_manager.current = 'welcome'
                    pos_hint: {'x':.5, 'y':.44}
                    size_hint: .2, .04

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

""")


class Phone(FloatLayout):
    pass


class UserDropDown(DropDown):
    pass



class TestApp(App):
    def build(self):
        return Phone()

if __name__ == '__main__':
    TestApp().run()