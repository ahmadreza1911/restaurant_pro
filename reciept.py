import os
from tkinter import *
from khayyam import *
from khayyam import jalali_date
from tkinter import  Tk, Canvas, Entry, Text, Button, PhotoImage
from database import *
from tkinter.font import Font
from datetime import date
#from main import Main


OUTPUT_PATH = os.path.abspath(__file__)
ASSETS_PATH = os.path.join(OUTPUT_PATH, r"C:\Users\ahmad\OneDrive\Desktop\git_pro\restaurant_pro\assets\frame0")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


class Receipt(Frame):
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
                self.listbox_receipt.insert(0,"%s %s %s %s" % (receipt[1],receipt[2],receipt[3],receipt[4]))




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
            receipt_id=int(self.receipt_num_lable.cget('text')) 
            jdate = JalaliDatetime.now()
            date = jdate.todatetime()
            max_daily_receipt= int(self.daily_receipt_num_lable.cget('text'))

            

            result=db.get_receipt_by_receiptid_menuid(receipt_id,menu_id)
            if len(result)==0:
                db.insert_into_receipt(receipt_id,menu_id,1,price,date,max_daily_receipt)

            else:
                db.increase_count(receipt_id,menu_id)

            
            load_receipt(receipt_id)

        self.listbox_drinks.bind('<Double-Button>', add_drink)


        self.listbox_foods = Listbox(self.canvas,background='#B9B9B9', exportselection=False,font=self.kalame_font) # Create a listbox
        self.canvas.create_window(1636.0,570.0, window=self.listbox_foods, width=470, height=780) 
        self.listbox_foods.configure(justify=RIGHT)

        foods=db.get_menu_items(True)

        for food in foods:
            self.listbox_foods.insert("end",food[1])

        
        def add_food(event):
            food_item=db.get_menu_item_by_name(self.listbox_foods.get(ACTIVE))
            menu_id=food_item[0][0]
            price=food_item[0][2]
            receipt_id=int(self.receipt_num_lable.cget('text')) 
            jdate = JalaliDatetime.now()
            date = jdate.todatetime()
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


        self.decrease_bt_image = PhotoImage(file=relative_to_assets("Decrease.png"))
        self.decrease_bt = Button(self,image=self.decrease_bt_image,borderwidth=0,highlightthickness=0,command=lambda: print("Decrease"),relief="flat")
        self.decrease_bt.place(x=735.0,y=913.0,width=70.0,height=90.0)


        self.increase_bt_image = PhotoImage(file=relative_to_assets("Increase.png"))
        self.increase_bt = Button(self,image=self.increase_bt_image,borderwidth=0,highlightthickness=0,command=lambda: print("increase_bt_image"),relief="flat")
        self.increase_bt.place(x=647.0,y=913.0,width=71.0,height=90.0)


        self.delete_line_image = PhotoImage(file=relative_to_assets("Delete_line.png"))
        self.delete_line = Button(self,image=self.delete_line_image,borderwidth=0,highlightthickness=0,command=lambda: print("delete_line_image"),relief="flat")
        self.delete_line.place(x=470.0,y=913.0,width=161.0,height=90.0)


        self.new_receipt_image = PhotoImage(file=relative_to_assets("New_receipt.png"))
        self.new_receipt= Button(self,image=self.new_receipt_image,borderwidth=0,highlightthickness=0,command=lambda: print("New_receipt clicked"),relief="flat")
        self.new_receipt.place(x=240.0,y=913.0,width=212.0,height=90.0)


        self.print_receipt_image = PhotoImage(file=relative_to_assets("Print_receipt.png"))
        self.print_receipt = Button(self,image=self.print_receipt_image,borderwidth=0,highlightthickness=0,command=lambda: print("print_ receipt clicked"),relief="flat")
        self.print_receipt.place(x=29.0,y=914.0,width=193.0,height=89.0)


        self.listbox_receipt = Listbox(self.canvas,background='#B9B9B9', exportselection=False,font=self.kalame_font) # Create a listbox
        #self.canvas.create_window(66.0,179.0,776.0,879.0,window=self.listbox_receipt)
        self.canvas.create_window(420.0,530.0, window=self.listbox_receipt, width=700, height=700) 
        self.listbox_receipt.configure(justify=RIGHT)



        #end receipt menu


        #header


        self.receipt_num_image = PhotoImage(file=relative_to_assets("Receipt_num.png"))
        self.canvas.create_image(426.0,109.0,image=self.receipt_num_image)

        self.receipt_num_lable=Label(self,background="#b1b1b1",font=("Kalameh Regular", 28))
        self.canvas.create_window (426.0, 109.0,width=120,height=28,window=self.receipt_num_lable) 

        self.max_receipt_num = db.get_max_receipt()
        if self.max_receipt_num[0][0]==None:
            self.max_receipt_num=0
        else:
            self.max_receipt_num=int(self.max_receipt_num[0][0]==None)

        self.max_receipt_num +=1


        self.receipt_num_lable.config(text=self.max_receipt_num)
        


        self.canvas.create_text(492.0,79.0,anchor="nw",text="شماره فاکتور",fill="#000000",font=("Kalameh Regular", 31 * -1))

        self.date_image = PhotoImage(file=relative_to_assets("Date.png"))
        self.canvas.create_image(686.0,109.0,image=self.date_image)
        self.today = JalaliDatetime.now().strftime('%Y/%m/%d')
        self.label_date = Label(self, text=self.today ,background="#b1b1b1",font=("Kalameh Regular", 17))
        self.canvas.create_window (686, 109,width=120,height=28 , window=self.label_date) 

        self.canvas.create_text(755.0,79.0,anchor="nw",text="تاریخ",fill="#000000",font=("Kalameh Regular", 31 * -1))



        self.canvas.create_text(173.0,79.0,anchor="nw",text="شماره فاکتور روزانه",fill="#000000",font=("Kalameh Regular", 31 * -1))
        self.daily_receipt_num_image = PhotoImage(file=relative_to_assets("Daily_receipt_num.png"))
        self.canvas.create_image(103.0,109.0,image=self.daily_receipt_num_image)
        self.daily_receipt_num_lable=Label(self,background="#b1b1b1",font=("Kalameh Regular", 28))
        self.canvas.create_window (103.0, 109.0,width=120,height=28,window=self.daily_receipt_num_lable)


        self.max_daily_receipt = db.get_max_daily_receipt()
        if self.max_daily_receipt[0][0]==None:
            self.max_daily_receipt=0
        else:
            self.max_daily_receipt=int(self.max_daily_receipt[0][0]==None)

        self.max_daily_receipt +=1
            
        

        self.daily_receipt_num_lable.config(text=self.max_daily_receipt)



        self.home_img = PhotoImage(file=relative_to_assets("Home_btn.png"))
        self.home_btn= Button(self,image=self.home_img,borderwidth=0,highlightthickness=0,command=self.show_page_home,relief="flat")
        self.home_btn.place(x=45.0,y=5.0,width=50.0,height=50.0)


        #end header
    

    def show_page_home(self):
        from main import Main
        
        self.destroy()
        

        # Create an instance of the MainFrame class
        self.main = Main(self.master)
        self.main.pack()
        #self.decrease_bt.place_forget()
        #self.increase_bt.place_forget()
        #self.delete_line.place_forget()
        #self.new_receipt.place_forget()
        #self.print_receipt.place_forget()
        #self..place_forget()
        #self..place_forget()
        #self.main=Main(self)
        #self.main.tkraise()


