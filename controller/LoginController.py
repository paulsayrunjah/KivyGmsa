from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Login(BoxLayout):
    btn_login = ObjectProperty()
    name = ObjectProperty()
    password = ObjectProperty()

    def onLogin(self):
        print("Heloooooo")
