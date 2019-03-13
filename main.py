from os import listdir
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from controller.LoginController import Login
from controller.DashboardController import Dashboard

kv_path = './screen/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)



class RootContainer(BoxLayout):
    main_container = ObjectProperty()

    def replace_widget(self, widget="Login"):
        if widget == "Login":
            current_view = Factory.Login()
        else:
            current_view = Factory.Dashboard()

        self.main_container.clear_widgets()
        self.main_container.add_widget(current_view)

    def onLogin(self):
        self.replace_widget("Dashboard")
            

    def onLogout(self):
        self.replace_widget("Login")
        pass


class GmsApp(App):
    def build(self):
        container = RootContainer()
        container.replace_widget()
        return container


if __name__ == "__main__":
    GmsApp().run()
