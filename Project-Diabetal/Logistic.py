from tkinter import *
from tkinter import ttk
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

import confusion as cf
import numpy as np
import matplotlib.pyplot as plt
import threading
import PIL.Image
import PIL.ImageTk
import TestLogistic


class Logistic:
	
    flag = False
    
    def __init__(self, master, dataset):
        
        self.master = master
        
        self.output = ttk.Frame(master)
        self.output.grid(row=0, column=0)
        
        self.menu = ttk.Frame(master)
        self.menu.grid(row=0, column=1)
        
        self.top = ttk.Frame(self.menu)
        self.top.pack(fill=Y)
        
        self.bottom = ttk.Frame(self.menu)
        self.bottom.pack(fill=Y)
    
        self.start(dataset)
    
        
    def start(self, dataset):

        self.th = threading.Thread(target=self.processL(dataset))
        self.th.start()

        while not self.flag:
            sleep(0.5)
                        
    def activation(self, x):
        return 1 / (1 + np.exp(-x))
        
            
    def processL(self, dataset):
        
        X = dataset.iloc[ 1 : , 0 : 25].values
        y = dataset.iloc[ 1 : , 25].values

        scaler = preprocessing.MinMaxScaler()
        X = scaler.fit_transform(X)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        
        model = LogisticRegression(C=1e5, solver='lbfgs', multi_class='multinomial')
        model.fit(X_train, y_train)
        
        trainAccuracy = model.score(X_train, y_train)
        testAccuracy = model.score(X_test, y_test)
        
        x = 'Training Accuracy: {: .1f} %'.format(trainAccuracy*100)
        y = 'Testing Accuracy: {: .1f} %'.format(testAccuracy*100)
        
        
        ttk.Label(self.top, text = x, font = ('Arial', 14)).grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.top, text = y, font = ('Arial', 14)).grid(row=1, column=0, padx=5, pady=5)
        
        y_pred = model.predict(X_test)
        cnf_matrix = confusion_matrix(y_test, y_pred)
        np.set_printoptions(precision=2)
        
        print(model.coef_)

        target = np.asarray(['Diabetic', 'Non-Diabetic'])
        plt.figure()
        cf.plot_confusion_matrix(cnf_matrix, classes=target, title='Confusion matrix')
        plt.savefig('resources/matrix/cm-2.png')
        
        self.im = PIL.Image.open("resources/matrix/cm-2.png")
        self.photo = PIL.ImageTk.PhotoImage(self.im)
        ttk.Label(self.bottom, image = self.photo).grid(row=0, column=0)
        ttk.Button(self.bottom, text = 'Test New', command = self.test).grid(row=1, column=0)
        
        self.flag = True
        
    def test(self):
        self.window = Toplevel(self.master)
        TestLogistic.TestLogistic(self.window)