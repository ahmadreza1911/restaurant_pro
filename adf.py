def load_receipt(receipt_id):
    # اتصال به دیتابیس
    cont = sqlite3.connect('test.db')
    c = cont.cursor()
    # اجرای دستور SQL برای گرفتن اطلاعات فاکتور از جدول table_receipt
    c.execute('SELECT * FROM table_receipt WHERE receipt_id = ?', (receipt_id,))
    result = c.fetchone()
    # بررسی اینکه آیا نتیجه خالی است یا خیر
    if result is None:
        # اگر نتیجه خالی باشد، یعنی receipt_id وجود ندارد
        # پاک کردن ویجت‌ها از داده‌های قبلی
        listbox.delete(0, END)
        date_label.config(text="")
        daily_receipt_id_label.config(text="")
        # نمایش پیام خطا
        messagebox.showerror("Error", "receipt_id not found")
    else:
        # اگر نتیجه خالی نباشد، یعنی فاکتور پیدا شده است
        # گرفتن تاریخ و daily_receipt_id از نتیجه
        date = result[4]
        daily_receipt_id = result[5]
        # نمایش تاریخ و daily_receipt_id در لیبل‌ها
        date_label.config(text=date)
        daily_receipt_id_label.config(text=daily_receipt_id)
        # پاک کردن لیست باکس از داده‌های قبلی
        listbox.delete(0, END)
        # اجرای دستور SQL برای گرفتن اطلاعات آیتم‌های فاکتور از جدول table_receipt
        c.execute('SELECT * FROM table_receipt WHERE receipt_id = ?', (receipt_id,))
        items = c.fetchall()
        # حلقه برای گرفتن اطلاعات هر آیتم از فاکتور
        for item in items:
            # گرفتن menu_id، count و price از نتیجه
            menu_id = item[1]
            count = item[2]
            price = item[3]
            # اجرای دستور SQL برای گرفتن name از جدول table_menu
            c.execute('SELECT name FROM table_menu WHERE ID = ?', (menu_id,))
            name = c.fetchone()[0]
            # اضافه کردن اطلاعات آیتم به لیست باکس
            listbox.insert(END, f"{name} - {count} - {price}")
    # بستن اتصال
    cont.close()
