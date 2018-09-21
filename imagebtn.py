from tkinter import *

class ImageButton(Button):    
    def __init__(self, parent = None, hidden_image = None, **kw):
        Button.__init__(self, parent, kw)
        self.hidden_image = hidden_image
        self.alphabet = kw['image']