import os
from tkinter import *
from tkinter import  Tk
from database import *
from main import Main


OUTPUT_PATH = os.path.abspath(__file__)
ASSETS_PATH = os.path.join(OUTPUT_PATH, r"C:\Users\ahmad\OneDrive\Desktop\restaurant_pro\assets\frame0")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class App(Tk):
    def __init__(self):
        #main setup
        super().__init__()
        width=self.winfo_screenwidth()
        height=self.winfo_screenheight()
        self.geometry('%dx%d' %(width,height))
        self.state('zoomed')
        self.configure(bg = "#FFFFFF")
        self.title('مدیریت رستوران')
        self.main=Main(self)
        self.resizable(False, False)
        self.mainloop()


App()

