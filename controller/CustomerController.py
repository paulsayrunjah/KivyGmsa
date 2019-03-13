from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from services.utils import get_selected_row, rv_get_selected_row
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    selected_row_data = []

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            self.selected_row_data = []
            for x in get_selected_row(self, 4, self.index):
                self.selected_row_data.append(rv.data[x]["text"])
            # print(self.selected_row_data)
            data = CustomerTable().my_data[rv_get_selected_row(4, self.index)]
            print(data)

    def on_press(self):
        pass


class CustomerTable(BoxLayout):
    my_data = []
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(CustomerTable, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):
        self.my_data = [
            {"name": "pauuz", "age": "25",
                "team": "Manchester united", "id": 1, "un": "mon"},
            {"name": "pauuz", "age": "25",
                "team": "Manchester united", "id": 2, "un": "tue"},
            {"name": "pauuz", "age": "25",
                "team": "Manchester united", "id": 3, "un": "wed"},
            {"name": "pauuz", "age": "25",
                "team": "Manchester united", "id": 4, "un": "thur"}
        ]
        prefred_order = ["id", "name", "age", "team"]
        for row in self.my_data:
            for x in prefred_order:
                self.data_items.append(row[x])
        # create data_items
        # for i in range(100):
        #     index = i + 1
        #     self.data_items.append(index)
        #     for row in my_data:
        #         for x in prefred_order:
        #             self.data_items.append(row[x]+"-"+str(index))

        return self.data_items

    def onItemListSelected(self):
        print("Clicked")
        pass


class Customer(BoxLayout):
    pass
