import os
from tkinter import *
from khayyam import *
from khayyam import jalali_date
from tkinter import  Tk, Canvas, Entry, Text, Button, PhotoImage,ttk
from database import *
from tkinter.font import Font
from datetime import date
from tkcalendar import Calendar , DateEntry
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
        
        
        self.daily_reports_img = PhotoImage(file=relative_to_assets("Daily_reports.png"))
        self.report_by_date_img = PhotoImage(file=relative_to_assets("Report_by_date.png"))
        


        self.add(self.daily_reports,image=self.daily_reports_img)
        self.add(self.report_by_date,image=self.report_by_date_img)
        

    class Daily_reports(Frame):
        def __init__(self,parent):
            super().__init__(parent)
            #from tkinter import ttk
            self.place(x = 0, y = 0)
            self.canvas=Canvas(self,bg = "black",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")
            self.canvas.pack()

            self.layout()

        def show_page_home(self):
            from main import Main       
            self.destroy()
            self.main = Main(self.master)
            self.main.pack()
            
        def layout(self):
            self.kalame_font = Font(family="Kalame Regular", size=20)
        
            self.main_receipt_bg = PhotoImage(file=relative_to_assets("Main_1_bg.png"))
            self.canvas.create_image(960.0,540.0,image=self.main_receipt_bg)
            style = ttk.Style()
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
            receipts=db.get_receipt_by_date(date=date)
            printed_receipt_ids = {}
            sum_total=0
            for receipt in receipts :
                receipt_id=receipt[0]
                daily_receipt_id=receipt[5]
                total=db.get_total_by_receipt_id(receipt_id)
                
                if receipt_id not in printed_receipt_ids: 
                    self.tree.insert("", "end", values=(total,daily_receipt_id, receipt_id, date))
                    sum_total+= total
                    printed_receipt_ids[receipt_id]=True
            self.tree.insert("","end", values=(sum_total, "مبلغ کل", "", ""))
                    



            self.home_img = PhotoImage(file=relative_to_assets("Home_btn.png"))
            self.home_btn= Button(self,image=self.home_img,borderwidth=0,highlightthickness=0,command=self.show_page_home,relief="flat")
            self.home_btn.place(x=45.0,y=5.0,width=50.0,height=50.0)

    


    class Report_by_date(Frame):
        def __init__(self,parent):
            super().__init__(parent)
            self.place(x = 0, y = 0)
            self.canvas=Canvas(self,bg = "black",height = 1080,width = 1920,bd = 0,highlightthickness = 0,relief = "ridge")
            self.canvas.pack()
         
            self.layout1()

        def show_page_home(self):
            from main import Main       
            self.destroy()
            self.main = Main(self.master)
            self.main.pack()
        
        

            
        def layout1(self):
            
        
            self.kalame_font = Font(family="Kalame Regular", size=20)
        
            self.main_receipt_bg = PhotoImage(file=relative_to_assets("Main_1_bg.png"))
            self.canvas.create_image(960.0,540.0,image=self.main_receipt_bg)


            style = ttk.Style()
            self.canvas.create_text(1304.0,59.0,anchor="nw",text="از  تاریخ",fill="#FFFFFF",font=("Kalameh Regular", 30 * -1))

            self.canvas.create_text(975.0,59.0,anchor="nw",text="تا تاریخ",fill="#FFFFFF",font=("Kalameh Regular", 30 * -1))

            self.button_bg_img = PhotoImage(file=relative_to_assets("Button_bg.png"))
            self.canvas.create_image(960.0,79.0,image=self.button_bg_img)



            self.start_date_img = PhotoImage(file=relative_to_assets("Date_label.png"))
            self.canvas.create_image(1178.0,78.0,image=self.start_date_img)

            self.end_date_img = PhotoImage(file=relative_to_assets("Date_label.png"))
            self.canvas.create_image(848.0,78.0,image=self.end_date_img)


            datee= JalaliDatetime.now().strftime('%Y/%m/%d')
            datee_list=datee.split('/')
            today_year=datee_list[0][-2:]
            today_month=datee_list[1]
            today_day=datee_list[2]

            start_day_var = StringVar(self)
            start_month_var = StringVar(self)
            start_year_var = StringVar(self)


            start_day_var.set(today_day)
            start_month_var.set(today_month)
            start_year_var.set(today_year)



            days1 = list(range(1, 32))
            days=[]
            for num in days1:
                num = str(num)
                num = num.zfill(2)
                days.append(num)

            months1 = list(range(1, 13))
            months=[]
            for num in months1:
                num = str(num)
                num = num.zfill(2)
                months.append(num)
            years1 = list(range(0, 100))
            years=[]
            for num in years1:
                num = str(num)
                num = num.zfill(2)
                years.append(num)


            self.start_date_day=OptionMenu(self, start_day_var, *days)
            self.canvas.create_window (1258.0, 80.0,width=55,height=30,window=self.start_date_day)
            self.start_date_day.config(background="#D9D9D9", font=("Kalameh Regular", 20))

            self.start_date_month = OptionMenu(self, start_month_var, *months)
            self.canvas.create_window (1190.0, 80.0,width=55,height=30,window=self.start_date_month)
            self.start_date_month.config(background="#D9D9D9", font=("Kalameh Regular", 20))

            self.start_date_year = OptionMenu(self, start_year_var, *years)
            self.canvas.create_window (1122.0, 80.0,width=55,height=30,window=self.start_date_year)
            self.start_date_year.config(background="#D9D9D9", font=("Kalameh Regular", 20))

            end_day_var = StringVar(self)
            end_month_var = StringVar(self)
            end_year_var = StringVar(self)

            end_day_var.set(today_day)
            end_month_var.set(today_month)
            end_year_var.set(today_year)

            self.end_date_day=OptionMenu(self, end_day_var, *days)
            self.canvas.create_window (928.0, 80.0,width=55,height=30,window=self.end_date_day)
            self.end_date_day.config(background="#D9D9D9", font=("Kalameh Regular", 20))

            self.end_date_month=OptionMenu(self, end_month_var, *months)
            self.canvas.create_window (860.0, 80.0,width=55,height=30,window=self.end_date_month)
            self.end_date_month.config(background="#D9D9D9", font=("Kalameh Regular", 20))

            self.end_date_year=OptionMenu(self, end_year_var, *years)
            self.canvas.create_window (792.0, 80.0,width=55,height=30,window=self.end_date_year)
            self.end_date_year.config(background="#D9D9D9", font=("Kalameh Regular", 20))


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

            
            def find_date():
                start_day = start_day_var.get()
                start_month = start_month_var.get()
                start_year = start_year_var.get()

                start_year = '14' + start_year

                start_date = JalaliDatetime(int(start_year), int(start_month), int(start_day))

                start_date_str = start_date.strftime('%Y/%m/%d')
                end_day = end_day_var.get()
                end_month = end_month_var.get()
                end_year = end_year_var.get()

                end_year = '14' + end_year

                end_date = JalaliDatetime(int(end_year), int(end_month), int(end_day))
                end_date_str = end_date.strftime('%Y/%m/%d')

                for item in self.tree.get_children (): 
                    self.tree.delete (item) 

                receipts=db.get_receipt_between_date(start_date_str,end_date_str)
                printed_receipt_ids = {}
                sum_total=0
                for receipt in receipts :

                    receipt_id=receipt[0]
                    daily_receipt_id=receipt[5]
                    date=receipt[4]
                    total=db.get_total_by_receipt_id(receipt_id)
                        
                    if receipt_id not in printed_receipt_ids: 
                        self.tree.insert("", "end", values=(total,daily_receipt_id, receipt_id, date))
                        sum_total+= total
                        printed_receipt_ids[receipt_id]=True
                self.tree.insert("","end", values=(sum_total, "مبلغ کل", "", ""))
            


            self.search_button_img = PhotoImage(file=relative_to_assets("Search_button.png"))
            self.search_button = Button(self,image=self.search_button_img,borderwidth=0,highlightthickness=0,command=find_date,relief="flat")
            self.search_button.place(x=583.0,y=56.0,width=119.0,height=41.0)

            self.home_img = PhotoImage(file=relative_to_assets("Home_btn.png"))
            self.home_btn= Button(self,image=self.home_img,borderwidth=0,highlightthickness=0,command=self.show_page_home,relief="flat")
            self.home_btn.place(x=45.0,y=5.0,width=50.0,height=50.0)

        


        