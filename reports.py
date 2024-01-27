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
        style.configure('TNotebook', background='#6A6A6A')
        self.style = style
        ttk.Treeview

        self.daily_reports = self.Daily_reports(self) 
        self.report_by_date = self.Report_by_date(self)
        self.report_by_name = self.Report_by_name(self)
        
        self.daily_reports_img = PhotoImage(file=relative_to_assets("Daily_reports.png"))
        self.report_by_date_img = PhotoImage(file=relative_to_assets("Report_by_date.png"))
        self.report_by_name_img = PhotoImage(file=relative_to_assets("Report_by_name.png"))


        self.add(self.daily_reports,image=self.daily_reports_img)
        self.add(self.report_by_date,image=self.report_by_date_img)
        self.add(self.report_by_name,image=self.report_by_name_img)

    class Daily_reports(Frame):
        def __init__(self,parent):
            super().__init__(parent)
            #from tkinter import ttk
            self.place(x = 0, y = 0)
            self.canvas=Canvas(self,bg = "black",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")
            self.canvas.pack()

            self.layout()


            
        def layout(self):
            self.kalame_font = Font(family="Kalame Regular", size=20)
        
            self.main_receipt_bg = PhotoImage(file=relative_to_assets("Main_1_bg.png"))
            self.canvas.create_image(960.0,540.0,image=self.main_receipt_bg)
            style = ttk.Style()
            # تغییر فونت tree
            #style.configure("Treeview.heading", font=('Kalame Regular', 20))
            style.configure("Treeview.Heading", font=('Kalame Regular', 16))
            style.configure("Treeview", font=('Kalame Regular', 12))

            self.tree=ttk.Treeview(self)
            self.canvas.create_window(980.0,540.0, window=self.tree, width=700, height=800)

            
            self.tree["columns"] = ( "مبلغ فاکتور", "شماره فاکتور روزانه" ,"شماره فاکتور","تاریخ")

            self.tree.column("#0", width=0, stretch=NO)
            self.tree.column("مبلغ فاکتور", anchor=E, width=50)
            self.tree.column("شماره فاکتور روزانه", anchor=E, width=50)
            self.tree.column("شماره فاکتور", anchor=E, width=50)
            self.tree.column("تاریخ", anchor=E, width=80) # اضافه کردن ستون تاریخ

            self.tree.heading("#0", text="", anchor=E)
            self.tree.heading("مبلغ فاکتور", text="مبلغ فاکتور", anchor=E)
            self.tree.heading("شماره فاکتور روزانه", text="شماره فاکتور روزانه", anchor=E)
            self.tree.heading("شماره فاکتور", text="شماره فاکتور", anchor=E)
            self.tree.heading("تاریخ", text="تاریخ", anchor=E) # اضافه کردن عنوان ستون تاریخ

            self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
            self.scroll.pack(side=RIGHT, fill=Y)

            self.tree.configure(yscrollcommand=self.scroll.set)

            date= JalaliDatetime.now().strftime('%Y/%m/%d')
            print(type(date))
            receipts=db.get_receipt_by_date(date=date)
            printed_receipt_ids = {}
            for receipt in receipts :
                receipt_id=receipt[0]
                daily_receipt_id=receipt[5]
                total=db.get_total_by_receipt_id(receipt_id)
                if receipt_id not in printed_receipt_ids: 
                    self.tree.insert("", "end", values=(total,daily_receipt_id, receipt_id, date))
                    printed_receipt_ids[receipt_id]=True

            



    class Report_by_date(Frame):
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



    class Report_by_name(Frame):
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