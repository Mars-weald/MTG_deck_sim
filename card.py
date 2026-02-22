class Card:
    def __init__(self, name, is_marked=False):
        self.name = name
        self.is_marked = is_marked
    
    def mark(self):
        self.is_marked = True
