import tkinter as tk
from tkinter import filedialog
import os


def open_folder_and_get_files():
    root = tk.Tk()
    root.withdraw()  # مخفی کردن پنجره اصلی
    folder_path = filedialog.askdirectory()  # باز کردن فایل بروزر و انتخاب پوشه
    print("مسیر پوشه انتخاب شده:", folder_path)

    # خواندن تمام فایل‌های موجود در این پوشه
    files_in_folder = os.listdir(folder_path)
    print("فایل‌های موجود در این پوشه:")
    for file in files_in_folder:
        print(os.path.join(folder_path, file))


open_folder_and_get_files()