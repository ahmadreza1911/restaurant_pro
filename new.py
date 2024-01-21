from tkinter import *
from tkinter import ttk

# ایجاد یک پنجره
window = Tk()
window.title("نوت بوک با")

# ایجاد یک نوت بوک با
notebook = ttk.Notebook(window)
notebook.pack()

# ایجاد یک کانواس
canvas = Canvas(notebook, width=200, height=200, bg="white")

# اضافه کردن یک تب با متن و کانواس
notebook.add(canvas, text="گزارش ماهانه")

# نمایش پنجره
window.mainloop()
