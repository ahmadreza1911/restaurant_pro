import os
from tkinter import *
from khayyam import *
from khayyam import jalali_date
from tkinter import  Tk, Canvas, Entry, Text, Button, PhotoImage,ttk
from database import *
from tkinter.font import Font
from datetime import date
#from main import Main


OUTPUT_PATH = os.path.abspath(__file__)
ASSETS_PATH = os.path.join(OUTPUT_PATH, r"C:\Users\ahmad\OneDrive\Desktop\restaurant_pro\assets\frame0")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Reports(ttk.Notebook):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x = 0, y = 0)
        
        #self.canvas=Canvas(self,bg = "black",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")
        #self.canvas.pack()
        style = ttk.Style()
        self.main_receipt_bg = PhotoImage(file=relative_to_assets("Main_1_bg.png"))
        # configure the style for the notebook
        style.configure('TNotebook', background='black',image=self.main_receipt_bg)

        # apply the style to the notebook
        self.style = style
        
        self.daily_reports = self.Daily_reports(self)
        
        
        self.monthly_reports = self.Monthly_reports(self)
        
        self.home_img = PhotoImage(file=relative_to_assets("Home_btn.png"))
        self.add(self.daily_reports, text="گزارش روزانه",image=self.home_img,)
        self.add(self.monthly_reports, text="گزارش ماهانه")

    class Daily_reports(Frame):
        def __init__(self,parent):
            super().__init__(parent)
            self.place(x = 0, y = 0)
            self.canvas=Canvas(self,bg = "black",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")
            self.canvas.pack()

            self.layout()


            
        def layout(self):
            self.kalame_font = Font(family="Kalame Regular", size=20)
        
            self.main_receipt_bg = PhotoImage(file=relative_to_assets("Main_1_bg.png"))
            self.canvas.create_image(960.0,540.0,image=self.main_receipt_bg)

            self.listbox_foods = Listbox(self.canvas,background='#B9B9B9', exportselection=False) # Create a listbox
            self.canvas.create_window(1636.0,570.0, window=self.listbox_foods, width=470, height=780) 
            self.listbox_foods.configure(justify=RIGHT)



    class Monthly_reports(Frame):
        def __init__(self,parent):
            super().__init__(parent)
            self.place(x = 0, y = 0)
            self.canvas=Canvas(self,bg = "black",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")
            self.canvas.pack()

            self.layout1()


            
        def layout1(self):
            self.kalame_font = Font(family="Kalame Regular", size=20)
        
            self.main_receipt_bg = PhotoImage(file=relative_to_assets("Main_1_bg.png"))
            self.canvas.create_image(960.0,540.0,image=self.main_receipt_bg)

            self.listbox_foods = Listbox(self.canvas,background='#B9B9B9', exportselection=False) # Create a listbox
            self.canvas.create_window(1636.0,570.0, window=self.listbox_foods, width=470, height=780) 
            self.listbox_foods.configure(justify=RIGHT)