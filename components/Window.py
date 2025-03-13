import tkinter as tk
#from SceneManager import SceneManager

class Window:
    def __init__(self):
        self.root = tk.Tk()
    
    def setTitle(self, name):
        self.root.title(name)
    
    def setDisplay(self, size):
        if size == 'fullscreen':
            self.root.attributes('-fullscreen', True)
        else:
            self.root.geometry(size)
        
        canvas = tk.Canvas(self.root, bg='lightcoral')
        canvas.pack(fill=tk.BOTH, expand=True)
            
    def start(self):
        #frame = Frame(self.root, bg='lightgreen')
        #frame.place(relwidth=1, relheight=1)
        
        self.root.mainloop()
    
    def setBackgroundColor(self, color):
        self.root.configure(bg = color)