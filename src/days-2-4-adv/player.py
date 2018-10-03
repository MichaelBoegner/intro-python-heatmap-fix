# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, currentRoom, items=None):
        self.name = name
        self.health = 100
        self.mana = 50
        self.currentRoom = currentRoom
        self.badMove = '==You abruptly realize it is impossible to continue in this direction, turn around, and stride confidently back from whence you came.=='
        self.items = items

    def __str__(self):
        return f'\nPlayer Name: {self.name}\n Health: {self.health} - Mana: {self.mana} - Room: {self.currentRoom.name} - Items: {self.items}'

    def playerMove(self, direction):
        if direction == 'n':
            self.currentRoom = self.currentRoom.n_to
        elif direction == 's': 
            self.currentRoom = self.currentRoom.s_to
        elif direction == 'e': 
            self.currentRoom = self.currentRoom.e_to
        elif direction == 'w': 
            self.currentRoom = self.currentRoom.w_to
    
    def playerGet(self, item):
        self.items = item







