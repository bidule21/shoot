import Tkinter as tk
import ShootBE as sbe
import ttk


class ShootApp(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.shootBackEnd = sbe.ShootBE('')

        # define the gui elements
        self.data_treeview = ttk.Treeview(self)
        self.column_id = list()

        self.build_gui()
        self.set_treeview_column_ids(self.shootBackEnd.column_heading_list)

        # checks to see that column ids were set before calling
        if self.column_id != '':
            self.set_treeview_column_headings()

        self.init_window = InitPrompt()

    def build_gui(self):
        self.data_treeview.grid(row=0)

    def set_treeview_column_ids(self, headings):
        self.column_id = []

        # set values for the column identifier list
        for heading_count in range(len(headings)):
            self.column_id.append('#' + str(heading_count))
            # print(column_id[heading_count])

        # apply the identifiers to the columns
        self.data_treeview['columns'] = self.column_id

    def set_treeview_column_headings(self):
        # get values of headings from backend
        headings = self.shootBackEnd.get_column_headings_shootdb()

        # iterate over list to add them to the treeview
        for column_count in range(len(headings)):
            self.data_treeview.heading(column=self.column_id[column_count], text=headings[column_count])
            # self.data_treeview.column(self.column_id[column_count], stretch=True, width=80)

    def set_treeview_data_values(self):
        print(ShootApp.set_treeview_data_values)
        # get data values from backend

        data = self.shootBackEnd.get_all_records_shootdb




# prompt shown on startup, where user selects working db location
class InitPrompt(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.grab_set()
        self.confirm_button = tk.Button(self, text='Confirm', default='active').grid(row=1, column=3)
        self.cancel_button = tk.Button(self, text='Cancel', command=self.close).grid(row=1, column=2)
        self.browse_button = tk.Button(self, text='Browse...').grid(row=1, column=1)
        self.entry_label = tk.Label(self, text='Database:').grid(row=0, column=0)
        self.db_entry = tk.Entry(self).grid(row=0, column=1, columnspan=3)

    def close(self):
        self.grab_release()
        self.destroy()

# MAIN BLOCK
if __name__ == "__main__":
    root = tk.Tk()
    ShootApp(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
