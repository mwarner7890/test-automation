from tkinter import *


class TestRunnerGui:
    def __init__(self, master):
        self.root = master
        self.frame = Frame(self.root)
        self.frame.pack()


root = Tk()
TestRunnerGui(root)
root.mainloop()
