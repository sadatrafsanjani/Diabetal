from tkinter import *
from tkinter import ttk
from pandastable import Table
import pandas as pd
import Tree
import Logistic
import Loader
import PIL.Image
import PIL.ImageTk

class Diabetal:
    
    def __init__(self, master, filename='dataset.csv'):
        
        self.master = master
        self.header = ttk.Frame(master)
        self.header.pack(padx=10, pady=10)
        
        self.im = PIL.Image.open("resources/img/logo.gif")
        self.logo = PIL.ImageTk.PhotoImage(self.im)
        ttk.Label(self.header, image = self.logo).pack(fill=X)
        ttk.Label(self.header, text = 'Diabetes Prediction System -A Machine Learning Approach', font = ('Arial', 12)).pack()
        
        self.content = ttk.Frame(master)
        self.content.pack(fill=X)
        
        self.table = ttk.Frame(self.content)
        self.table.pack(fill=X)
        
        self.menu = ttk.Frame(master)
        self.menu.pack()
        
        dataset = pd.read_csv(filename)
        
        self.wraggling(dataset)
        
    def wraggling(self, dataset):
        
        dataset.columns = ["Age", "Gender", "Height","Weight", "BMI", "Profession",
                   "DMYears", "RiskFactor", "Exercise", "FoodHabit", "JunkFood", 
                   "Polydipsia", "Polyuria", "Blurr","WeightLoss","ExtremeHunger",
                   "Tiredness", "SlowHealing", "Infection", "Hemoglobin", "FastingSugar",
                   "ABFSugar","Creatinine", "Treatment", "Result"]
                   
    
        dataset = dataset.drop(["Hemoglobin", "FastingSugar","ABFSugar","Creatinine",'Treatment'], axis=1)
        
        gender = pd.get_dummies(dataset['Gender'])
        merge = pd.concat([dataset, gender], axis='columns')
        dataset = merge.drop(['Gender', 'Female'], axis='columns')
        
        profession = pd.get_dummies(dataset['Profession'])
        merge = pd.concat([dataset, profession], axis='columns')
        dataset = merge.drop(['Profession', 'Both'], axis='columns')
        
        risk = pd.get_dummies(dataset['RiskFactor'])
        merge = pd.concat([dataset, risk], axis='columns')
        dataset = merge.drop(['RiskFactor', 'No'], axis='columns')
        
        habit = pd.get_dummies(dataset['FoodHabit'])
        merge = pd.concat([dataset, habit], axis='columns')
        dataset = merge.drop(['FoodHabit', 'Vegetarian'], axis='columns')

        junk = pd.get_dummies(dataset['JunkFood'])
        merge = pd.concat([dataset, junk], axis='columns')
        dataset = merge.drop(['JunkFood', 'Moderately'], axis='columns')
        
        result = dataset['Result']
        dataset = dataset.drop(['Result'], axis=1)
        features = list(dataset.columns.values)
        dataset['Result'] = result
        
        dataset = dataset.fillna(dataset.mean()).dropna(axis=1, how='all')
        features = dataset.columns[ : 25]
        
        Table(self.table, dataframe=dataset, showtoolbar=False, showstatusbar=False).show()
        
        ttk.Button(self.menu, text = 'Decision Tree', command = lambda:self.decision(dataset, features)).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(self.menu, text = 'Logistic Regression', command = lambda:self.logistic(dataset)).grid(row=0, column=1, padx=5, pady=5)
        
    def decision(self, dataset, features):
        self.window = Toplevel(self.master)
        Tree.Tree(self.window, dataset, features)
        
    def logistic(self, dataset):
        self.window = Toplevel(self.master)
        Logistic.Logistic(self.window, dataset)

def main():
    
    root = Tk()
    Loader.Loader(root)
    root.title('Diabetal')
    root.wm_iconbitmap('resources/img/logo.ico')
    root.geometry("400x300")
    root.mainloop()
    

if __name__ == "__main__":
    main()