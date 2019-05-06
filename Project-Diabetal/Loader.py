from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import Diabetal
        
class Loader:

    def __init__(self, master):
        
        self.master = master
        self.master.resizable(False, False)
        
        self.content = ttk.Frame(master)
        self.content.pack(padx=10, pady=10)
        ttk.Button(self.content, text = 'Load CSV', command = self.csvs).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(self.content, text = 'Go', command = self.go).grid(row=1, column=0, padx=5, pady=5)
        
    def csvs(self):
        
        self.filename = askopenfilename(filetypes=[("CSV Files", "*.csv")])
        
        
    def go(self):
        
        if(self.filename is ''):
            messagebox.showinfo("Error!", "Please load the Step-1 File")
        else:
            self.window = Toplevel(self.master)
            self.master.withdraw()
            Diabetal.Diabetal(self.window, self.filename)
        
    
        
        
    