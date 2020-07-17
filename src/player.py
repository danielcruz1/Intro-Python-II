# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

# need list items, pickup items, drop items

    def inventory(self):
        print('Inventory:')
        for item in self.items:
            print(item)

    
 