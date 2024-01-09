import os
from tkinter import *
from khayyam import *
from tkinter import  Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
from database import *
from tkinter.font import Font
from main import Main
from reciept import Receipt
from main_edit_product import Main_edit_product
from add_product import Add_product
from database import Database

OUTPUT_PATH = os.path.abspath(__file__)
ASSETS_PATH = os.path.join(OUTPUT_PATH, r"C:\Users\ahmad\OneDrive\Desktop\git_pro\restaurant_pro\assets\frame0")

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


        #self.db=Database()
        
        
        self.kalame_font = Font(family="Kalame Regular", size=25)
        
        
        #self.main_edit_product=Main_edit_product(self)
        
        #self.receipt = Receipt(self)


        self.main=Main(self)
        #self.main.tkraise

        
        self.resizable(False, False)
        self.mainloop()

        



App()

