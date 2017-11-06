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
        self.test_select_btn_move_to_scheduled = Button(test_select_btn_frame, text=' > ',
                                                        command=self.move_test_case_to_scheduled)
        self.test_select_btn_move_all_to_scheduled = Button(test_select_btn_frame, text='>>',
                                                            command=self.move_all_test_cases_to_scheduled)
        self.test_select_btn_move_all_from_scheduled = Button(test_select_btn_frame, text='<<',
                                                              command=self.move_all_test_cases_from_scheduled)
        self.test_select_btn_move_from_scheduled = Button(test_select_btn_frame, text=' < ',
                                                          command=self.move_test_case_from_scheduled)
        self.test_select_btn_move_to_scheduled.pack()
        self.test_select_btn_move_all_to_scheduled.pack()
        self.test_select_btn_move_all_from_scheduled.pack()
        self.test_select_btn_move_from_scheduled.pack()
        test_select_btn_frame.grid(row=0, column=2)

        scheduled_test_suites_frame = Frame(self.master)
        scheduled_test_suites_list_label = Label(scheduled_test_suites_frame, text='Scheduled Test Cases')
        self.scheduled_test_suites_list = Listbox(scheduled_test_suites_frame)
        scheduled_test_suites_list_label.pack()
        self.scheduled_test_suites_list.pack()
        scheduled_test_suites_frame.grid(row=0, column=3)

        test_run_stop_btn_frame = Frame(self.master)
        self.test_run_btn = Button(test_run_stop_btn_frame, text='    \n  Run  \n    ',
                                   command=self.run_tests)
        self.test_stop_btn = Button(test_run_stop_btn_frame, text='    \n  Stop  \n    ',
                                    command=self.stop_tests)
        self.test_run_btn.config(state=DISABLED)
        self.test_stop_btn.config(state=DISABLED)
        self.test_run_btn.pack()
        self.test_stop_btn.pack()
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
        curselection = self.all_test_suite_cases_list.curselection()
        if curselection:
            selected_test_case = self._get_selected_test_case_from_all_test_cases()
            self._insert_into_scheduled_test_list(END, selected_test_case)
            self.all_test_suite_cases_list.delete(curselection)

    def move_all_test_cases_to_scheduled(self):
        while self.all_test_suite_cases_list.get(0):
            test_case_name = self.all_test_suite_cases_list.get(0)
            self._insert_into_scheduled_test_list(END, test_case_name)
            self.all_test_suite_cases_list.delete(0)

    def move_all_test_cases_from_scheduled(self):
        while self.scheduled_test_suites_list.get(0):
            test_case_name = self.scheduled_test_suites_list.get(0)
            self.all_test_suite_cases_list.insert(END, test_case_name)
            self._delete_from_scheduled_test_list(0)

    def move_test_case_from_scheduled(self):
        curselection = self.scheduled_test_suites_list.curselection()
        if curselection:
            selected_test_case = self._get_selected_test_case_from_scheduled_tests()
            self.all_test_suite_cases_list.insert(END, selected_test_case)
            self._delete_from_scheduled_test_list(0)

    def _insert_into_scheduled_test_list(self, index, test_name):
        self.scheduled_test_suites_list.insert(index, test_name)
        if self.scheduled_test_suites_list.get(0):
            self.test_suites_list.config(state=DISABLED)
            self.test_run_btn.config(state=NORMAL)
        else:
            self.test_suites_list.config(state=NORMAL)
            self.test_run_btn.config(state=DISABLED)

    def _delete_from_scheduled_test_list(self, index):
        self.scheduled_test_suites_list.delete(index)
        if self.scheduled_test_suites_list.get(0):
            self.test_suites_list.config(state=DISABLED)
            self.test_run_btn.config(state=NORMAL)
        else:
            self.test_suites_list.config(state=NORMAL)
            self.test_run_btn.config(state=DISABLED)

    def _get_selected_test_case_from_all_test_cases(self):
        return self.all_test_suite_cases_list.get(self.all_test_suite_cases_list.curselection())

    def _get_selected_test_case_from_scheduled_tests(self):
        return self.scheduled_test_suites_list.get(self.scheduled_test_suites_list.curselection())

    def run_tests(self):
        print('Running tests')
        self.test_run_btn.config(state=DISABLED)
        self.test_stop_btn.config(state=NORMAL)

        self.test_select_btn_move_to_scheduled.config(state=DISABLED)
        self.test_select_btn_move_all_to_scheduled.config(state=DISABLED)
        self.test_select_btn_move_all_from_scheduled.config(state=DISABLED)
        self.test_select_btn_move_from_scheduled.config(state=DISABLED)

    def stop_tests(self):
        print('Stopping tests')
        self.test_run_btn.config(state=NORMAL)
        self.test_stop_btn.config(state=DISABLED)

        self.test_select_btn_move_to_scheduled.config(state=NORMAL)
        self.test_select_btn_move_all_to_scheduled.config(state=NORMAL)
        self.test_select_btn_move_all_from_scheduled.config(state=NORMAL)
        self.test_select_btn_move_from_scheduled.config(state=NORMAL)


root = Tk()
TestRunnerGui(root)
root.mainloop()
