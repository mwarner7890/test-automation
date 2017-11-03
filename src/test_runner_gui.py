from tkinter import *


class TestRunnerGui:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.master.title('Test Runner')
        Button(self.master, text='Test Suites').grid(row=0, column=0)
        Button(self.master, text='Tests').grid(row=0, column=1)

        test_select_btn_frame = Frame(self.master)
        test_select_btn_select = Button(test_select_btn_frame, text=' > ')
        test_select_btn_select_all = Button(test_select_btn_frame, text='>>')
        test_select_btn_deselect = Button(test_select_btn_frame, text='<<')
        test_select_btn_deselect_all = Button(test_select_btn_frame, text=' < ')
        test_select_btn_select.pack()
        test_select_btn_select_all.pack()
        test_select_btn_deselect.pack()
        test_select_btn_deselect_all.pack()
        test_select_btn_frame.grid(row=0, column=2)

        Button(self.master, text='Scheduled Tests').grid(row=0, column=4)

        test_run_stop_btn_frame = Frame(self.master)
        test_run_btn = Button(test_run_stop_btn_frame, text='Run')
        test_stop_btn = Button(test_run_stop_btn_frame, text='Stop')
        test_run_btn.pack()
        test_stop_btn.pack()
        test_run_stop_btn_frame.grid(row=0, column=5)

        Button(self.master, text='Test Output').grid(row=3, column=0)
        Button(self.master, text='Clear').grid(row=3, column=4)
        Button(self.master, text='dawjdioawdoz\najwoidjioawjdoiaw\nawidjoiawd\najwodiawj').grid(row=4, column=0)


root = Tk()
TestRunnerGui(root)
root.mainloop()
