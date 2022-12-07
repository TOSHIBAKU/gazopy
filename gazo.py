import pyautogui as pygui
import tkinter
from tkinter import filedialog
import icrawler
from icrawler.builtin import GoogleImageCrawler

name=pygui.prompt('集める画像の名前を入力してください。')
val=int(pygui.prompt('画像の集める枚数を入力してください'))
idir='C:\\Users\souma'
f_path = tkinter.filedialog.askdirectory(initialdir = idir)
crawler = GoogleImageCrawler(storage={"root_dir" : str(f_path)})

pygui.press('Enter')


crawler.crawl(
keyword=name,
max_num=val,
)