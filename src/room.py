# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room(Item):
    def __init__(self, name, description, item_name, item_description): 
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None