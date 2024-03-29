import os
from tkinter import *
#from khayyam import *
from tkinter import  Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
from database import *
from tkinter.font import Font
from reciept import Receipt

OUTPUT_PATH = os.path.abspath(__file__)
ASSETS_PATH = ASSETS_PATH = os.path.join(OUTPUT_PATH, r"C:\Users\ahmad\OneDrive\Desktop\restaurant_pro\assets\frame0")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Edit_product(Frame):
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


        self.listbox_drinks = Listbox(self.canvas,background='#B9B9B9', exportselection=False,font=self.kalame_font) 
        self.canvas.create_window(1125.0,569.0, window=self.listbox_drinks, width=470, height=780) 
        self.listbox_drinks.configure(justify=RIGHT)


        self.listbox_foods = Listbox(self.canvas,background='#B9B9B9', exportselection=False,font=self.kalame_font) 
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

        #end menu form
        
        #receipt menu

        self.receipt_bg = PhotoImage(file=relative_to_assets("Receipt_bg.png"))
        self.canvas.create_image(421.0,540.0,image=self.receipt_bg)


        self.canvas.create_rectangle(51.0,108.0,788.0,109.0,fill="#000000",outline="")

        self.canvas.create_rectangle(52.0,979.0,789.0,980.0,fill="#000000",outline="")
            
        #end receipt menu

        self.name_of_food = PhotoImage(file=relative_to_assets("Entry_bg.png"))
        self.canvas.create_image(304.0,270.0,image=self.name_of_food)

        self.name_of_food_entry=Entry(self,background="#E4E4E4",font=("Kalameh Regular", 28),justify='right')
        self.canvas.create_window (304.0, 270.0,width=300,height=80,window=self.name_of_food_entry)


        self.type_of_food = PhotoImage(file=relative_to_assets("Entry_bg.png"))
        self.canvas.create_image(304.0,567.0,image=self.type_of_food)
        

        def validate(user_input):
            if user_input == "" or user_input.isdigit():
                return True
            else:
                messagebox.showerror("خطا", "لطفا یک عدد معتبر وارد کنید")
                return False

        vcmd = self.register(validate)


        self.price_of_food = PhotoImage(file=relative_to_assets("Entry_bg.png"))
        self.canvas.create_image(304.0,419.0,image=self.price_of_food)

        self.price_of_food_entry=Entry(self,background="#E4E4E4",font=("Kalameh Regular", 28),justify='right',validate="key", validatecommand=(vcmd, "%P"))
        self.canvas.create_window (304.0, 419.0,width=300,height=80,window=self.price_of_food_entry)

        var=BooleanVar() 
        self.food_button = Radiobutton(self, text="غذا",bg="#E4E4E4",font=("Kalameh Regular", 20 ),variable=var,value=True)
        self.drink_button = Radiobutton(self, text="نوشیدنی",bg="#E4E4E4",font=("Kalameh Regular", 20 ),variable=var,value=False)
        self.food_button.place(x=200.0,y=545.0,width=100.0,height=40.0)
        self.drink_button.place(x=300.0,y=545.0,width=100.0,height=40.0)
        

        self.id_entry=Entry(self)


        def add_drink(event):
            self.name_of_food_entry.delete(0, 'end')
            self.price_of_food_entry.delete(0, 'end')
            self.id_entry.delete(0, 'end')
            drink_item=db.get_menu_item_by_name(self.listbox_drinks.get(ACTIVE))
            id=drink_item[0][0]
            name=drink_item[0][1]
            price=drink_item[0][2]
            type_of_food=drink_item[0][3]
            self.name_of_food_entry.insert(0, name)
            self.price_of_food_entry.insert(0, price)
            self.id_entry.insert(0,id)
            if type_of_food == 1:
                var.set(True) 
            else:
                var.set(False)

        self.listbox_drinks.bind('<Double-Button>', add_drink)




        def add_food(event):
            self.name_of_food_entry.delete(0, 'end')
            self.price_of_food_entry.delete(0, 'end')
            self.id_entry.delete(0, 'end')
            food_item=db.get_menu_item_by_name(self.listbox_foods.get(ACTIVE))
            id=food_item[0][0]
            name=food_item[0][1]
            price=food_item[0][2]
            type_of_food=food_item[0][3]
            self.name_of_food_entry.insert(0, name)
            self.price_of_food_entry.insert(0, price)
            self.id_entry.insert(0,id)
            if type_of_food == 1:
                var.set(True) 
            else:
                var.set(False)

        self.listbox_foods.bind('<Double-Button>', add_food)



        def submit_data():
            id=int(self.id_entry.get())
            name=self.name_of_food_entry.get()
            price=self.price_of_food_entry.get()
            type_of_food=var.get()

            
            if name == "" or price == "" :
                messagebox.showerror("خطا", "لطفا همه فیلد ها را پر کنید")
                return
            try:
                price = int(price)
            except ValueError:
                messagebox.showerror("خطا", "قیمت کالا فقط مقدار عددی میتواند بگیرد")
                return
            try: 
                db.update(id,name,price,type_of_food)
                messagebox.showinfo("موفق", "اطلاعات با موفقیت تغییر کرد")
                self.listbox_drinks.delete(0, END) 
                self.listbox_foods.delete(0, END) 

                load_listbox(self)
            except:
                messagebox.showerror("خطا", "نام تکراری می باشد")





        self.submit = PhotoImage(file=relative_to_assets("Submit.png"))
        self.submit_btn = Button(self,image=self.submit,borderwidth=0,highlightthickness=0,command=submit_data,relief="flat")
        self.submit_btn.place(x=271.8,y=731.4,width=298.667,height=127.6)


        def delete_data():
            id =int(self.id_entry.get())
            answer = messagebox.askokcancel("هشدار", "آیا مطمئنید که می خواهید این غذا را حذف کنید؟")
            
            if answer == True:
                db.delete(id)
                messagebox.showinfo("موفق", "اطلاعات با موفقیت حذف شد")
                self.listbox_foods.delete(0, END) 
                self.listbox_drinks.delete(0, END) 
                load_listbox(self)
            else:
                return





        self.delete_button_img = PhotoImage(file=relative_to_assets("Delete_btn.png"))
        self.delete_button = Button(self,image=self.delete_button_img,borderwidth=0,highlightthickness=0,command=delete_data,relief="flat")
        self.delete_button.place(x=99.0,y=763.0,width=148.0,height=64.0)





        self.canvas.create_text(513.0,538.0,anchor="nw",text="انتخاب نوع منو",fill="#050202",font=("Kalameh Regular", 35 * -1))
        self.canvas.create_text(492.0,241.0,anchor="nw",text="نام غذا یا نوشیدنی ",fill="#050202",font=("Kalameh Regular", 35 * -1))
        self.canvas.create_text(565.0,390.0,anchor="nw",text="قیمت",fill="#050202",font=("Kalameh Regular", 35 * -1))



        self.home_img = PhotoImage(file=relative_to_assets("Big_back.png"))
        self.home_btn= Button(self,image=self.home_img,borderwidth=0,highlightthickness=0,command=self.show_page_home,relief="flat")
        self.home_btn.place(x=45.0,y=5.0,width=50.0,height=50.0)


    def show_page_home(self):
        from main_edit_product import Main_edit_product
        self.destroy()
        self.main_edit_product = Main_edit_product(self.master)
        self.main_edit_product.pack()