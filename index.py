from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtWidgets
from os import path
import time
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import qApp, QFileDialog, QMessageBox

import sqlite3
from sqlite3 import Error


FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.getDblocation)  # Brows DB
        self.pushButton_3.clicked.connect(self.create_connection)
        self.pushButton.clicked.connect(self.connection)


    def getDblocation(self):
        save_place = QFileDialog.getOpenFileName(self, caption="chose db ", directory=".", filter="All Files (*.*)")
        text = str(save_place)
        name = (text[2:].split(',')[0].replace("'", ''))
        self.lineEdit.setText(name)


    def create_connection(self):
        this_path = os.getcwd()
        db_name = self.lineEdit_2.text()
        if len(db_name) == 0 :
            QMessageBox.about(self, "Title", "Message")
        else:
            db_in = this_path+"\\"+db_name+".db"
            connection = None
            try:
                connection = sqlite3.connect(db_in)
                print("Connection to SQLite DB successful")
                self.label_3.setText(db_name)
            except Error as e:
                print(f"The error '{e}' occurred")

            fullPath = this_path + "\\" + db_name + ".db"
            print(fullPath)
            self.lineEdit.setText(fullPath)

            return connection


    def connection(self):
        path = self.lineEdit.text()
        db_name = path.split("/")[-1].split(".")[0]
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
            self.label_3.setText(db_name)
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection







'''
## https://likegeeks.com/python-sqlite3-tutorial/ ##
# To show all tables
        con = sqlite3.connect(path)
        cursorObj = con.cursor()
        cursorObj.execute('SELECT name from sqlite_master where type= "table"')
        print(cursorObj.fetchall())
        
# to close connection
    con.close()
'''




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()