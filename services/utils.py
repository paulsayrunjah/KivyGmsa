def replace_widget(self, current_view, main_container):
        main_container.clear_widgets()
        main_container.add_widget(current_view)

def get_selected_row(self, total_count, index):
        rem = index % total_count
        times = (index-rem) / total_count
        if index < total_count:
                col = 0
        else:
                col = index-rem
        positions = []
        for x in range(total_count):
                positions.append(col+x)
        return positions
def rv_get_selected_row(total_count, index):
        rem = index % total_count
        times = (index-rem) / total_count
        if index < total_count:
                row = 0
        else:
                row = times
        return int(row)

                
