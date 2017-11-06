import test_runner
from tkinter import *


class TestRunnerGui:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.master.title('Test Runner')

        self.test_suite_module_name_dict = {
            'Throughput tests': 'throughput_testing',
            'Standard tests': 'standard_testing'
        }

        test_suites_frame = Frame(self.master)
        test_suites_list_label = Label(test_suites_frame, text='Test Suites')
        self.test_suites_list = Listbox(test_suites_frame)
        test_suites_list_label.pack()
        self.test_suites_list.pack()
        test_suites_frame.grid(row=0, column=0)
        for test_suite_name in self.test_suite_module_name_dict:
            self.test_suites_list.insert(END, test_suite_name)
        self.test_suites_list.bind('<<ListboxSelect>>', self.update_test_case_list)

        all_test_suites_frame = Frame(self.master)
        all_test_suites_list_label = Label(all_test_suites_frame, text='All Test Cases')
        self.all_test_suite_cases_list = Listbox(all_test_suites_frame)
        all_test_suites_list_label.pack()
        self.all_test_suite_cases_list.pack()
        all_test_suites_frame.grid(row=0, column=1)

        test_select_btn_frame = Frame(self.master)
        test_select_btn_move_to_scheduled = Button(test_select_btn_frame, text=' > ',
                                                   command=self.move_test_case_to_scheduled)
        test_select_btn_move_all_to_scheduled = Button(test_select_btn_frame, text='>>')
        test_select_btn_move_from_scheduled = Button(test_select_btn_frame, text='<<')
        test_select_btn_move_all_from_scheduled = Button(test_select_btn_frame, text=' < ')
        test_select_btn_move_to_scheduled.pack()
        test_select_btn_move_all_to_scheduled.pack()
        test_select_btn_move_from_scheduled.pack()
        test_select_btn_move_all_from_scheduled.pack()
        test_select_btn_frame.grid(row=0, column=2)

        scheduled_test_suites_frame = Frame(self.master)
        scheduled_test_suites_list_label = Label(scheduled_test_suites_frame, text='Scheduled Test Cases')
        self.scheduled_test_suites_list = Listbox(scheduled_test_suites_frame)
        scheduled_test_suites_list_label.pack()
        self.scheduled_test_suites_list.pack()
        scheduled_test_suites_frame.grid(row=0, column=3)

        test_run_stop_btn_frame = Frame(self.master)
        test_run_btn = Button(test_run_stop_btn_frame, text='    \n  Run  \n    ')
        test_stop_btn = Button(test_run_stop_btn_frame, text='    \n  Stop  \n    ')
        test_run_btn.config(state=DISABLED)
        test_stop_btn.config(state=DISABLED)
        test_run_btn.pack()
        test_stop_btn.pack()
        test_run_stop_btn_frame.grid(row=0, column=5)

        Label(self.master).grid(row=3)
        Label(self.master, text='Test Output').grid(row=4, column=0)
        Button(self.master, text='  Clear  ').grid(row=4, column=5)
        output_scrollbar = Scrollbar(self.master)
        output_scrollbar.grid(row=6, column=6, sticky='NS')
        test_output_text = Text(self.master, wrap=WORD, yscrollcommand=output_scrollbar)
        test_output_text.grid(row=6, column=0, columnspan=6)
        test_output_text.config(yscrollcommand=output_scrollbar.set,
                                state=DISABLED)
        output_scrollbar.config(command=test_output_text.yview)

    def update_test_case_list(self, event):
        curselection = event.widget.curselection()
        if curselection:
            selected_test_suite = self.test_suites_list.get(curselection)
            test_suite_module_name = self.test_suite_module_name_dict.get(selected_test_suite)
            test_suite_module = __import__(test_suite_module_name)
            self.all_test_suite_cases_list.delete(0, END)
            for test_name in test_runner.get_all_test_names_in_suite(test_suite_module):
                self.all_test_suite_cases_list.insert(END, test_name)

    def move_test_case_to_scheduled(self):
        selected_test_case = self._get_selected_test_case()
        self.scheduled_test_suites_list.insert(END, selected_test_case)
        self.all_test_suite_cases_list.delete(self.all_test_suite_cases_list.curselection())

    def _get_selected_test_case(self):
        return self.all_test_suite_cases_list.get(self.all_test_suite_cases_list.curselection())


root = Tk()
TestRunnerGui(root)
root.mainloop()
