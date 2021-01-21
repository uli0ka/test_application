import time
from tkinter import *


class BaseWindow:
    def __init__(self):
        self.lbl1 = Label(text="Date and time:").grid(row=0, column=0)
        self.lbl = Label(text="", width=20, height=3)
        self.lbl.grid(row=0, column=1, columnspan=3)
        self.btn_output = Button(text="Вывести", command=lambda txt=time.ctime(time.time()): self.clicked_output(txt)) \
            .grid(row=1, column=0)
        self.btn_clear = Button(text="Очистить", command=lambda txt="": self.clicked_output(txt)) \
            .grid(row=1, column=3)

    def clicked_output(self, txt):
        self.lbl['text'] = txt

