import os
from tkinter import *
from khayyam import *
from tkinter import   Canvas, Entry, Button, PhotoImage,messagebox
from database import *
from tkinter.font import Font
import csv

OUTPUT_PATH = os.path.abspath(__file__)
ASSETS_PATH = os.path.join(OUTPUT_PATH, r"C:\Users\ahmad\OneDrive\Desktop\restaurant_pro\assets\frame0")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Edit_receipt(Frame):
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

        #menu form
        self.menu_bg_image = PhotoImage(file=relative_to_assets("Menu_bg.png"))
        self.canvas.create_image(1381.0,540.0,image=self.menu_bg_image)


        self.canvas.create_rectangle(909.0,152.0,1852.0,153.0,fill="#000000",outline="")


        self.canvas.create_rectangle(1379.0,180.0,1381.0,957.0,fill="#000000",outline="")


        self.canvas.create_text(1692.0,73.0,anchor="nw",text="منوی غذاها",fill="#000000",font=("Kalameh Regular", 48 * -1))


        self.canvas.create_text(1101.0,73.0,anchor="nw",text="منوی نوشیدنی ها",fill="#000000",font=("Kalameh Regular", 48 * -1))


        def load_receipt(receipt_id):
            self.listbox_receipt.delete(0,'end')
            receipts=db.get_receipt_by_receiptid(receipt_id)
            for receipt in receipts:
                self.listbox_receipt.insert(0,"%s-%s %s %s" % (receipt[1],str(receipt[2])+ "عدد","{:,}".format(receipt[3]) + " ریال","{:,}".format(receipt[4]) + " ریال"))
                total=db.get_total_by_receipt_id(receipt_id)
                self.total_label.config(text="")
                self.total_label.config(text="{:,}".format(total) + " ریال")



        self.listbox_drinks = Listbox(self.canvas,background='#B9B9B9', exportselection=False,font=self.kalame_font) # Create a listbox
        self.canvas.create_window(1125.0,569.0, window=self.listbox_drinks, width=470, height=780) 
        self.listbox_drinks.configure(justify=RIGHT)

        drinks=db.get_menu_items(False)

        for drink in drinks:
            self.listbox_drinks.insert("end",drink[1])

        def add_drink(event):
            drink_item=db.get_menu_item_by_name(self.listbox_drinks.get(ACTIVE))
            menu_id=drink_item[0][0]
            price=drink_item[0][2]
            receipt_id=int(self.receipt_num_entry.get()) 
            date = self.label_date.cget('text')
        
            max_daily_receipt= int(self.daily_receipt_num_lable.cget('text'))

            

            result=db.get_receipt_by_receiptid_menuid(receipt_id,menu_id)
            if len(result)==0:
                db.insert_into_receipt(receipt_id,menu_id,1,price,date,max_daily_receipt)

            else:
                db.increase_count(receipt_id,menu_id)

            
            load_receipt(receipt_id)

        self.listbox_drinks.bind('<Double-Button>', add_drink)


        self.listbox_foods = Listbox(self.canvas,background='#B9B9B9', exportselection=False,font=self.kalame_font) 
        self.canvas.create_window(1636.0,570.0, window=self.listbox_foods, width=470, height=780) 
        self.listbox_foods.configure(justify=RIGHT)

        foods=db.get_menu_items(True)

        for food in foods:
            self.listbox_foods.insert("end",food[1])

        
        def add_food(event):
            food_item=db.get_menu_item_by_name(self.listbox_foods.get(ACTIVE))
            menu_id=food_item[0][0]
            price=food_item[0][2]
            receipt_id=int(self.receipt_num_entry.get())
            date = self.label_date.cget('text')
            max_daily_receipt= int(self.daily_receipt_num_lable.cget('text'))

            

            result=db.get_receipt_by_receiptid_menuid(receipt_id,menu_id)
            if len(result)==0:
                db.insert_into_receipt(receipt_id,menu_id,1,price,date,max_daily_receipt)

            else:
                db.increase_count(receipt_id,menu_id)

            
            load_receipt(receipt_id)


        self.listbox_foods.bind('<Double-Button>',add_food)
        #end menu form


       

        #receipt menu

        self.receipt_bg = PhotoImage(file=relative_to_assets("Receipt_bg.png"))
        self.canvas.create_image(421.0,540.0,image=self.receipt_bg)


        self.canvas.create_rectangle(51.0,159.0,788.0,160.0,fill="#000000",outline="")

        self.canvas.create_rectangle(53.0,897.0,790.0,898.0,fill="#000000",outline="")

         #header


        self.receipt_num_image = PhotoImage(file=relative_to_assets("Receipt_num.png"))
        self.canvas.create_image(426.0,109.0,image=self.receipt_num_image)

        self.canvas.create_text(492.0,79.0,anchor="nw",text="شماره فاکتور",fill="#000000",font=("Kalameh Regular", 31 * -1))
        self.receipt_num_entry=Entry(self,background="#b1b1b1",font=("Kalameh Regular", 28),justify='center')
        self.canvas.create_window (426.0, 109.0,width=100,height=40,window=self.receipt_num_entry) 



        def entry_key_release(key):
            try:
                receipt_id= int(self.receipt_num_entry.get())
                result=db.get_date_and_daily_receipt_id(receipt_id)
                load_receipt(receipt_id)
                if result== None:
                    self.label_date.config(text="")
                    self.daily_receipt_num_lable.config(text="")
                    self.total_label.config(text="")
                else:
                    self.label_date.config(text=result[0][0])
                    self.daily_receipt_num_lable.config(text=result[0][1])
                    
                
            except:
                
                self.listbox_receipt.delete(0,'end')
                self.label_date.config(text='')
                self.daily_receipt_num_lable.config(text='')
                self.total_label.config(text="")
                


        self.receipt_num_entry.bind('<KeyRelease>', entry_key_release)
        
        

        self.date_image = PhotoImage(file=relative_to_assets("Date.png"))
        self.canvas.create_image(686.0,109.0,image=self.date_image)
        self.label_date = Label(self,background="#b1b1b1",font=("Kalameh Regular", 17))
        self.canvas.create_window (686, 109,width=120,height=28 , window=self.label_date) 

        self.canvas.create_text(755.0,79.0,anchor="nw",text="تاریخ",fill="#000000",font=("Kalameh Regular", 31 * -1))


        self.canvas.create_text(173.0,79.0,anchor="nw",text="شماره فاکتور روزانه",fill="#000000",font=("Kalameh Regular", 31 * -1))
        self.daily_receipt_num_image = PhotoImage(file=relative_to_assets("Daily_receipt_num.png"))
        self.canvas.create_image(103.0,109.0,image=self.daily_receipt_num_image)
        self.daily_receipt_num_lable=Label(self,background="#b1b1b1",font=("Kalameh Regular", 28))
        self.canvas.create_window (103.0, 109.0,width=120,height=28,window=self.daily_receipt_num_lable)

        self.canvas.create_text(365.0,835.0,anchor="nw",text="مبلغ کل",fill="#000000",font=("Kalameh Regular", 31 * -1))
        self.total_image = PhotoImage(file=relative_to_assets("Total_label.png"))
        self.canvas.create_image(216.0,855.0,image=self.total_image)
        self.total_label=Label(self,background="#929292",font=("Kalameh Regular", 28))
        self.canvas.create_window (216.0, 855.0,width=220,height=28,window=self.total_label)

        self.home_img = PhotoImage(file=relative_to_assets("Home_btn.png"))
        self.home_btn= Button(self,image=self.home_img,borderwidth=0,highlightthickness=0,command=self.show_page_home,relief="flat")
        self.home_btn.place(x=45.0,y=5.0,width=50.0,height=50.0)


        #end header
        def decrease_item():
            menu_item_name=self.listbox_receipt.get(ACTIVE)
            result=db.get_menu_item_by_name(menu_item_name.split('-')[0])
            menu_item_id=result[0][0]            
            receipt_id=int(self.receipt_num_entry.get())
            db.decrease_count(receipt_id,menu_item_id)
            load_receipt(receipt_id)

            
        self.decrease_bt_image = PhotoImage(file=relative_to_assets("Decrease.png"))
        self.decrease_bt = Button(self,image=self.decrease_bt_image,borderwidth=0,highlightthickness=0,command=decrease_item,relief="flat")
        self.decrease_bt.place(x=656.0,y=913.0,width=70.0,height=90.0)


        def increase_item():
            menu_item_name=self.listbox_receipt.get(ACTIVE)
            result=db.get_menu_item_by_name(menu_item_name.split('-')[0])
            menu_item_id=result[0][0]            
            receipt_id=int(self.receipt_num_entry.get())
            db.increase_count(receipt_id,menu_item_id)
            load_receipt(receipt_id)
            

        self.increase_bt_image = PhotoImage(file=relative_to_assets("Increase.png"))
        self.increase_bt = Button(self,image=self.increase_bt_image,borderwidth=0,highlightthickness=0,command=increase_item,relief="flat")
        self.increase_bt.place(x=550.0,y=913.0,width=71.0,height=90.0)


        def delete_line():
            receipt_id=int(self.receipt_num_entry.get())
            menu_line=self.listbox_receipt.get(ACTIVE)
            menu_line_name=menu_line.split('-')[0]
            result=db.get_menu_item_by_name(menu_line_name)
            menu_line_id=int(result[0][0])
            db.delete_receipt(receipt_id,menu_line_id)
            load_receipt(receipt_id)

        self.delete_line_image = PhotoImage(file=relative_to_assets("Delete_line.png"))
        self.delete_line = Button(self,image=self.delete_line_image,borderwidth=0,highlightthickness=0,command=delete_line,relief="flat")
        self.delete_line.place(x=354.0,y=913.0,width=161.0,height=90.0)


        def print_receipt():
            receipt_id=self.receipt_num_entry.get()
            receipts=db.get_receipt_by_receiptid(receipt_id)
            if len(receipts)==0:
                messagebox.showerror("خطا", "فاکتور خالی می  باشد",icon='warning')
            else:

                file = open("receipt.csv", "w", newline="", encoding="utf-8")
                writer = csv.writer(file)
                result=db.get_date_and_daily_receipt_id(receipt_id)
                daily_receipt=result[0][1]
                date=result[0][0]
            
                writer.writerow(["نرم افزار حسابداری رستوران"])
                writer.writerow(["شماره فاکتور", receipt_id])
                writer.writerow(["شماره فاکتور روزانه",daily_receipt])
                writer.writerow(["تاریخ",date])
                writer.writerow(["مجموع قیمت", "قیمت", "تعداد", "نام غذا"])


                for receipt in receipts:
                    line = " {0},{1},{2},{3}\n".format(receipt[4], receipt[3], receipt[2], receipt[1])
                    file.write(line)

                total = self.total_label.cget("text")
                writer.writerow(["قیمت کل", total])
                file.close()



        self.print_receipt_image = PhotoImage(file=relative_to_assets("Print_receipt.png"))
        self.print_receipt = Button(self,image=self.print_receipt_image,borderwidth=0,highlightthickness=0,command=print_receipt,relief="flat")
        self.print_receipt.place(x=126.0,y=914.0,width=193.0,height=89.0)


        self.listbox_receipt = Listbox(self.canvas,background='#B9B9B9', exportselection=False,font=self.kalame_font) 
        self.canvas.create_window(420.0,495.0, window=self.listbox_receipt, width=750, height=620) 
        self.listbox_receipt.configure(justify=RIGHT)

        #end receipt menu


    def show_page_home(self):
        from main import Main 
        self.destroy()
        self.main = Main(self.master)
        self.main.pack()



