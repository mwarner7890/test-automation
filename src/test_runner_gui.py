from tkinter import *


class TestRunnerGui:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master, width=1000, height=512)
        self.frame.pack()


root = Tk()
TestRunnerGui(root)
root.mainloop()
