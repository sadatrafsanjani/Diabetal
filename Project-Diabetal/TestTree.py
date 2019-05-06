from tkinter import *
from tkinter import ttk
        
class TestTree:
    
    def __init__(self, master):
        
        self.menu = ttk.Frame(master)
        self.menu.pack(fill=Y)
        
        Label(self.menu, text="Age").grid(row=0, column=0)
        self.entry1 = Entry(self.menu).grid(row=0, column=1)
        
        Label(self.menu, text="Gender").grid(row=1, column=0)
        variable = StringVar(master)
        variable.set("Female")
        self.entry2 = OptionMenu(self.menu, variable, "Female", "Male").grid(row=1, column=1)
        
        Label(self.menu, text="Height").grid(row=2, column=0)
        self.entry3 = Entry(self.menu).grid(row=2, column=1)
        
        Label(self.menu, text="Weight").grid(row=3, column=0)
        self.entry4 = Entry(self.menu).grid(row=3, column=1)
        
        Label(self.menu, text="Profession").grid(row=4, column=0)
        variable = StringVar(master)
        variable.set("Mental")
        self.entry5 = OptionMenu(self.menu, variable, "Mental", "Physical", "Both").grid(row=4, column=1)
        
        Label(self.menu, text="Years").grid(row=5, column=0)
        self.entry6 = Entry(self.menu).grid(row=5, column=1)
        
        Label(self.menu, text="Risk factor").grid(row=6, column=0)
        variable = StringVar(master)
        variable.set("Father")
        self.entry7 = OptionMenu(self.menu, variable, "Father", "Mother", "Paternal Grandparent", "Maternal Grandparent", "No").grid(row=6, column=1)
        
        Label(self.menu, text="Do you Exercise?").grid(row=7, column=0)
        v = IntVar()
        self.entry8 = Radiobutton(self.menu, text="Yes", variable=v, value=1).grid(row=7, column=1)
        self.entry9 = Radiobutton(self.menu, text="No", variable=v, value=2).grid(row=7, column=2)
        
        Label(self.menu, text="Food Habit").grid(row=8, column=0)
        self.entry10 = Radiobutton(self.menu, text="Vegetarian", variable=v, value=1).grid(row=8, column=1)
        self.entry11 = Radiobutton(self.menu, text="Non-Vegetarian", variable=v, value=1).grid(row=8, column=2)
        
        Label(self.menu, text="Junk Food").grid(row=9, column=0)
        variable = StringVar(master)
        variable.set("Moderately")
        self.entry12 = OptionMenu(self.menu, variable, "Moderately", "Rarely", "Often").grid(row=9, column=1)
        
        Label(self.menu, text="Frequent Thirst").grid(row=10, column=0)
        v = IntVar()
        self.entry13 = Radiobutton(self.menu, text="Yes", variable=v, value=1).grid(row=10, column=1)
        self.entry14 = Radiobutton(self.menu, text="No", variable=v, value=1).grid(row=10, column=2)
        
        Label(self.menu, text="Frequent Urination").grid(row=11, column=0)
        v = IntVar()
        self.entry15 = Radiobutton(self.menu, text="Yes", variable=v, value=1).grid(row=11, column=1)
        self.entry16 = Radiobutton(self.menu, text="No", variable=v, value=1).grid(row=11, column=2)
        
        Label(self.menu, text="Shortness of Sight").grid(row=12, column=0)
        v = IntVar()
        self.entry17 = Radiobutton(self.menu, text="Yes", variable=v, value=1).grid(row=12, column=1)
        self.entry18 = Radiobutton(self.menu, text="No", variable=v, value=1).grid(row=12, column=2)
        
        Label(self.menu, text="Weight Loss").grid(row=13, column=0)
        v = IntVar()
        self.entry19 = Radiobutton(self.menu, text="Yes", variable=v, value=1).grid(row=13, column=1)
        self.entry20 = Radiobutton(self.menu, text="No", variable=v, value=1).grid(row=13, column=2)
        
        Label(self.menu, text="Extreme Hunger").grid(row=14, column=0)
        v = IntVar()
        self.entry21 = Radiobutton(self.menu, text="Yes", variable=v, value=1).grid(row=14, column=1)
        self.entry22 = Radiobutton(self.menu, text="No", variable=v, value=1).grid(row=14, column=2)
        
        Label(self.menu, text="Tiredness").grid(row=15, column=0)
        v = IntVar()
        self.entry23 = Radiobutton(self.menu, text="Yes", variable=v, value=1).grid(row=15, column=1)
        self.entry24 = Radiobutton(self.menu, text="No", variable=v, value=1).grid(row=15, column=2)
        
        Label(self.menu, text="Slow Healing").grid(row=16, column=0)
        v = IntVar()
        self.entry25 = Radiobutton(self.menu, text="Yes", variable=v, value=1).grid(row=16, column=1)
        self.entry26 = Radiobutton(self.menu, text="No", variable=v, value=1).grid(row=16, column=2)
        
        Label(self.menu, text="Infection").grid(row=17, column=0)
        v = IntVar()
        self.entry27 = Radiobutton(self.menu, text="Yes", variable=v, value=1).grid(row=17, column=1)
        self.entry28 = Radiobutton(self.menu, text="No", variable=v, value=1).grid(row=17, column=2)
        
        Label(self.menu, text="Hemoglobin").grid(row=18, column=0)
        self.entry29 = Entry(self.menu).grid(row=18, column=1)
        
        Label(self.menu, text="Fasting Sugar").grid(row=19, column=0)
        self.entry30 = Entry(self.menu).grid(row=19, column=1)
        
        Label(self.menu, text="Sugar After Breakfast").grid(row=20, column=0)
        self.entry31 = Entry(self.menu).grid(row=20, column=1)
        
        Label(self.menu, text="Creatinine").grid(row=21, column=0)
        self.entry32 = Entry(self.menu).grid(row=21, column=1)
        
        Label(self.menu, text="Predict").grid(row=22, column=0)
        ttk.Button(self.menu, text = 'Predict', command = self.test).grid(row=22, column=1)
        
        self.output = ttk.Frame(master)
        self.output.pack(fill=Y)
        Label(self.output, text="Result").pack(fill=X)
        
    def test(self):
        pass
        