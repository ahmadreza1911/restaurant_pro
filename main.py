import os
from tkinter import *
from tkinter import  Tk, Canvas, Button, PhotoImage,messagebox
from database import *
from reciept import Receipt
from main_edit_product import Main_edit_product
from edit_receipt import Edit_receipt
from reports import Reports
import sys

OUTPUT_PATH = os.path.abspath(__file__)
ASSETS_PATH = ASSETS_PATH = os.path.join(OUTPUT_PATH, r"C:\Users\ahmad\OneDrive\Desktop\restaurant_pro\assets\frame0")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Main(Frame):
    def __init__(self,parent):
        
        super().__init__(parent)
        self.place(x = 0, y = 0)
        self.canvas=Canvas(self,bg = "black",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.pack()

        self.layout()
        

    def layout(self):

        self.main_bg = PhotoImage(file=relative_to_assets("Main_bg.png"))
        self.canvas.create_image(960.0,540.0,image=self.main_bg)

        self.receipt_btn = PhotoImage(file=relative_to_assets("Receipt_btn.png"))
        self.button_receipt = Button(self,image=self.receipt_btn,borderwidth=0,highlightthickness=0,relief="flat",command=self.show_page_receipt)
        self.button_receipt.place(x=1495.0,y=179.0,width=332.0,height=90.0)

        self.edit_menu_btn = PhotoImage(file=relative_to_assets("Edit_menu_btn.png"))
        self.button_edit_menu = Button(self,image=self.edit_menu_btn,borderwidth=0,highlightthickness=0,command=self.show_page_main_edit_product,relief="flat")
        self.button_edit_menu.place(x=1495.0,y=487.0,width=332.0,height=90.0)
        
        self.edit_recept_btn = PhotoImage(file=relative_to_assets("Edit_receipt_btn.png"))
        self.button_edit_recipt = Button(self,image=self.edit_recept_btn,borderwidth=0,highlightthickness=0,command=self.show_page_edit_receipt,relief="flat")
        self.button_edit_recipt.place(x=1495.0,y=333.0,width=332.0,height=90.0)

        self.reports_btn = PhotoImage(file=relative_to_assets("Reports_btn.png"))
        self.button_reports = Button(self,image=self.reports_btn,borderwidth=0,highlightthickness=0,command=self.show_page_reports,relief="flat")
        self.button_reports.place(x=1495.0,y=641.0,width=332.0,height=90.0)

        def exit_program():
            message_box = messagebox.askquestion('خروج','آیا مطمئن به خروج هستید؟',icon='warning')
            if message_box == 'yes':
                self.destroy()  
                exit() 
            else:
                return

        
        self.exit_btn = PhotoImage(file=relative_to_assets("Exit_btn.png"))
        self.button_exit = Button(self,image=self.exit_btn,borderwidth=0,highlightthickness=0,command=exit_program,relief="flat")
        self.button_exit.place(x=1496.0,y=795.0,width=332.0,height=90.0)
    

    def show_page_receipt(self):
        self.destroy()
        self.receipt = Receipt(self.master)
        self.receipt.pack()
        
    def show_page_main_edit_product(self):
        self.destroy()
        self.main_edit_product = Main_edit_product(self.master)
        self.main_edit_product.pack()

    def show_page_edit_receipt(self):
        self.destroy()
        self.edit_receipt = Edit_receipt(self.master)
        self.edit_receipt.pack()

    def show_page_reports(self):
        self.destroy()
        self.reports = Reports(self.master)
        self.reports.pack()