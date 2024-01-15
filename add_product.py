import os
from tkinter import *
from khayyam import *
from tkinter import  Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
from database import *
from tkinter.font import Font
from main import Main


OUTPUT_PATH = os.path.abspath(__file__)
ASSETS_PATH = os.path.join(OUTPUT_PATH, r"C:\Users\ahmad\OneDrive\Desktop\git_pro\restaurant_pro\assets\frame0")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Add_product(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        #self.place(x = 0, y = 0)
        self.canvas = Canvas(self,bg = "#FFFFFF",height = 642,width = 558,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.pack()

        self.layout()

    def layout(self):

        self.kalame_font = Font(family="Kalame Regular", size=18)

        self.add_product_bg1 = PhotoImage(file=relative_to_assets("Add_product_bg1.png"))
        self.canvas.create_image(294.0,359.0,image=self.add_product_bg1)


        self.add_product_bg2= PhotoImage(file=relative_to_assets("Add_product_bg2.png"))
        self.canvas.create_image(269.0,320.0,image=self.add_product_bg2)



        self.name_of_food = PhotoImage(file=relative_to_assets("Name_of_food.png"))
        self.canvas.create_image(195.0,125.0,image=self.name_of_food)


        self.name_entry = Entry(self,background="#E4E4E4",font=self.kalame_font,justify='right')
        self.canvas.create_window (195.0, 125.0,width=200,height=40,window=self.name_entry)

        


        self.price_of_food = PhotoImage(file=relative_to_assets("Price_of_food.png"))
        self.canvas.create_image(195.0,231.0,image=self.price_of_food)



        def validate(user_input):
            # اگر ورودی کاربر عددی باشد
            if user_input.isdigit():
                # برگرداندن True
                return True
            # در غیر این صورت
            else:
                # نمایش یک پیام خطا
                messagebox.showerror("Error", "Please enter a valid number")
                # برگرداندن False
                return False

        # ایجاد یک شی از تابع اعتبارسنجی
        vcmd = self.register(validate)


        self.price_entry = Entry(self,background="#E4E4E4",font=self.kalame_font,justify='right',validate="key", validatecommand=(vcmd, "%P"))
        self.canvas.create_window (195.0, 231.0,width=200,height=40,window=self.price_entry)


        self.type_of_food = PhotoImage(file=relative_to_assets("Type_of_food.png"))
        self.canvas.create_image(195.0,337.0,image=self.type_of_food)

        
        var=BooleanVar()                            

        self.food_button = Radiobutton(self, text="غذا",bg="#E4E4E4",font=("Kalameh Regular", 15 ),variable=var,value=True)
        self.drink_button = Radiobutton(self, text="نوشیدنی",bg="#E4E4E4",font=("Kalameh Regular", 15 ),variable=var,value=False)
        self.food_button.place(x=110.0,y=320.0,width=80.0,height=30.0)
        self.drink_button.place(x=190.0,y=320.0,width=80.0,height=30.0)

        self.canvas.create_text(344.0,320.0,anchor="nw",text="انتخاب نوع منو",fill="#050202",font=("Kalameh Regular", 28 * -1))
        self.canvas.create_text(329.0,102.0,anchor="nw",text="نام غذا یا نوشیدنی ",fill="#050202",font=("Kalameh Regular", 28 * -1))
        self.canvas.create_text(381.0,214.0,anchor="nw",text="قیمت",fill="#050202",font=("Kalameh Regular", 28 * -1))

        def submit_data():
            id=db.get_max_id_menuid()
            if id[0][0]==None:
                id=0
            else:
                id=int(id[0][0])
            id += 1
            name=self.name_entry.get()
            price=self.price_entry.get()
            type_of_food=var.get()
            if name == "" or price == "" :
                messagebox.showerror("Error", "Please fill all the fields")
                return
            try:
                price = int(price)
            except ValueError:
                messagebox.showerror("Error", "Price must be an integer")
                return
            try: 
                db.insert(id,name,price,type_of_food)
                messagebox.showinfo("Success", "Data added to the database")
            except:
                messagebox.showerror("Error", "Name already exists in the database")
        self.confrim_btn = PhotoImage(file=relative_to_assets("Confrim_btn.png"))
        self.button_1 = Button(self,image=self.confrim_btn,borderwidth=0,highlightthickness=0,command=submit_data,relief="flat")
        self.button_1.place(x=172.0,y=454.0,width=213.0,height=91.0)
            

        self.back_button = PhotoImage(file=relative_to_assets("Back.png"))
        self.button_2 = Button(self,image=self.back_button,borderwidth=0,highlightthickness=0,command=self.destroy,relief="flat")
        self.button_2.place(x=6.0,y=7.0,width=40.0,height=40.0)




       


