import os
from tkinter import *
#from khayyam import *
from tkinter import  Tk, Canvas, Entry, Text, Button, PhotoImage
from database import *
from tkinter.font import Font
from reciept import Receipt

OUTPUT_PATH = os.path.abspath(__file__)
ASSETS_PATH = ASSETS_PATH = os.path.join(OUTPUT_PATH, r"C:\Users\ahmad\OneDrive\Desktop\restaurant_pro\assets\frame0")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Main_edit_product(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x = 0, y = 0)
        self.canvas=Canvas(
            self,
            bg = "black",
            height = 1080,
            width = 1920,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.pack()
        self.layout()

    def layout(self):
        self.kalame_font = Font(family="Kalame Regular", size=25)

        self.main_receipt_bg = PhotoImage(file=relative_to_assets("Main_1_bg.png"))
        self.canvas.create_image(960.0,540.0,image=self.main_receipt_bg)

        #menu form
        self.menu_bg_image = PhotoImage(file=relative_to_assets("Menu_bg.png"))
        self.canvas.create_image(1381.0,540.0,image=self.menu_bg_image)


        self.canvas.create_rectangle(909.0,152.0,1852.0,153.0,fill="#000000",outline="")


        self.canvas.create_rectangle(1379.0,180.0,1381.0,957.0,fill="#000000",outline="")


        self.canvas.create_text(1692.0,73.0,anchor="nw",text="منوی غذاها",fill="#000000",font=("Kalameh Regular", 48 * -1))


        self.canvas.create_text(1101.0,73.0,anchor="nw",text="منوی نوشیدنی ها",fill="#000000",font=("Kalameh Regular", 48 * -1))


        self.listbox_drinks = Listbox(self.canvas,background='#B9B9B9', exportselection=False,font=self.kalame_font) # Create a listbox
        self.canvas.create_window(1125.0,569.0, window=self.listbox_drinks, width=470, height=780) 
        self.listbox_drinks.configure(justify=RIGHT)

        self.listbox_foods = Listbox(self.canvas,background='#B9B9B9', exportselection=False,font=self.kalame_font) # Create a listbox
        self.canvas.create_window(1636.0,570.0, window=self.listbox_foods, width=470, height=780) 
        self.listbox_foods.configure(justify=RIGHT)


        def load_listbox(self):
            drinks=db.get_menu_items(False)

            for drink in drinks:
                self.listbox_drinks.insert("end",drink[1])

            foods=db.get_menu_items(True)

            for food in foods:
                self.listbox_foods.insert("end",food[1])

        load_listbox(self)

        def delete_listbox(self):
            self.listbox_drinks.delete(0,END)
            self.listbox_foods.delete(0,END)

        #end menu form
        
         #receipt menu

        self.receipt_bg = PhotoImage(file=relative_to_assets("Receipt_bg.png"))
        self.canvas.create_image(421.0,540.0,image=self.receipt_bg)


        self.canvas.create_rectangle(51.0,108.0,788.0,109.0,fill="#000000",outline="")

        self.canvas.create_rectangle(52.0,979.0,789.0,980.0,fill="#000000",outline="")
            
        #end receipt menu
        self.add_product_img = PhotoImage(file=relative_to_assets("Add_product_btn.png"))
        self.add_product_btn = Button(self,image=self.add_product_img,borderwidth=0,highlightthickness=0,command=self.show_add_product,relief="flat")
        self.add_product_btn.place(x=247.0,y=352.0,width=347.0,height=147.0)

        self.edit_product_img = PhotoImage(file=relative_to_assets("Edit_product_btn.png"))
        self.edit_product_btn = Button(self,image=self.edit_product_img,borderwidth=0,highlightthickness=0,command=self.show_edit_product,relief="flat")
        self.edit_product_btn.place(x=247.0,y=580.0,width=347.0,height=147.0)


        self.home_img = PhotoImage(file=relative_to_assets("Home_btn.png"))
        self.home_btn= Button(self,image=self.home_img,borderwidth=0,highlightthickness=0,command=self.show_page_home,relief="flat")
        self.home_btn.place(x=45.0,y=5.0,width=50.0,height=50.0)


    def show_page_home(self):
        from main import Main
        self.destroy()
        self.main = Main(self.master)
        self.main.pack()

    
    def show_add_product(self):
        from add_product import Add_product
        self.add_product=Add_product(self)
        self.add_product.grab_set()


    def show_edit_product(self):
        from edit_product import Edit_product
        self.destroy()
        self.edit_product=Edit_product(self.master)
        self.edit_product.pack()
