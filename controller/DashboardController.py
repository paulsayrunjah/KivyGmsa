from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from controller.CustomerController import Customer
from services.utils import replace_widget

class Dashboard(BoxLayout):
    dashboard_container = ObjectProperty()
    username = "admin"

    # def gotoHome(self):
    #     current_view = Factory.Home()
    #     self.view_swicth.replace_widget(current_view, self.dashboard_container)

    def gotoCustomerView(self):
        current_view = Factory.Customer()
        replace_widget(self, current_view,self.dashboard_container)
