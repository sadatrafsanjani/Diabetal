from tkinter import *
from tkinter import ttk
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.externals.six import StringIO
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

import confusion as cf
import numpy as np
import matplotlib.pyplot as plt
import pydotplus
import threading
import PIL.Image
import PIL.ImageTk
import TestTree


class Tree:
    
    flag = False
    
    def __init__(self, master, dataset, features):
        
        self.master = master
        
        self.output = ttk.Frame(master)
        self.output.grid(row=0, column=0)
        
        self.menu = ttk.Frame(master)
        self.menu.grid(row=0, column=1)
        
        self.top = ttk.Frame(self.menu)
        self.top.pack(fill=Y)
        
        self.bottom = ttk.Frame(self.menu)
        self.bottom.pack(fill=Y)
        
        self.start(dataset, features)
    
        
    def start(self, dataset, features):

        self.th = threading.Thread(target=self.processD(dataset, features))
        self.th.start()

        while not self.flag:
            sleep(0.5)

            
    def processD(self, dataset, features):
       
        X = dataset.iloc[ 1 : , 0 : 25].values
        y = dataset.iloc[ 1 : , 25].values

        scaler = preprocessing.MinMaxScaler()
        X = scaler.fit_transform(X)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        
        model = tree.DecisionTreeClassifier(criterion='entropy')
        model.fit(X_train, y_train)
        
        filename = "resources/tree/tree.png"
        target = np.asarray(['Diabetic', 'Non-Diabetic'])
        dot_data = StringIO()
        tree.export_graphviz(model,feature_names=features, out_file=dot_data, class_names=target, filled=True)  
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
        graph.write_png(filename)
        
        self.ims = PIL.Image.open(filename)
        self.photos = PIL.ImageTk.PhotoImage(self.ims)
        ttk.Label(self.output, image = self.photos).pack()
        
        trainAccuracy = np.mean(cross_val_score(model, X_train, y_train, cv=10))
        testAccuracy = np.mean(cross_val_score(model, X_test, y_test, cv=10))
        
        x = 'Training Accuracy: {: .1f} %'.format(trainAccuracy*100)
        y = 'Testing Accuracy: {: .1f} %'.format(testAccuracy*100)
        
        ttk.Label(self.top, text = x, font = ('Arial', 14)).grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.top, text = y, font = ('Arial', 14)).grid(row=1, column=0, padx=5, pady=5)
        
        y_pred = model.predict(X_test)
        cnf_matrix = confusion_matrix(y_test, y_pred)
        np.set_printoptions(precision=2)

        target = np.asarray(['Diabetic', 'Non-Diabetic'])
        plt.figure()
        cf.plot_confusion_matrix(cnf_matrix, classes=target, title='Confusion matrix')
        plt.savefig('resources/matrix/cm-1.png')
        
        self.im = PIL.Image.open("resources/matrix/cm-1.png")
        self.photo = PIL.ImageTk.PhotoImage(self.im)
        ttk.Label(self.bottom, image = self.photo).grid(row=0, column=0)
        ttk.Button(self.bottom, text = 'Test New', command = self.test).grid(row=1, column=0)
        
        self.flag = True
        
        
    def test(self):
        self.window = Toplevel(self.master)
        TestTree.TestTree(self.window)
    