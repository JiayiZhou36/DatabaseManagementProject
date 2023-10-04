import pymysql
import sys
from PyQt5 import QtWidgets
import pandas as pd
import re
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem


 
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(482, 451)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        
        self.CustomerPurchase = QtWidgets.QPushButton(Form)
        self.CustomerPurchase.setObjectName("CustomerPurchase")
        self.horizontalLayout.addWidget(self.CustomerPurchase)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout) 
        
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.label_2 = QtWidgets.QPushButton(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        
        self.CustomerNotPurchase = QtWidgets.QPushButton(Form)
        self.CustomerNotPurchase.setObjectName("CustomerNotPurchase")
        self.horizontalLayout_2.addWidget(self.CustomerNotPurchase)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        
        self.label_3 = QtWidgets.QPushButton(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        
        self.employee = QtWidgets.QPushButton(Form)
        self.employee.setObjectName("Employee")
        self.horizontalLayout_3.addWidget(self.employee)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        
        self.pushButton = QtWidgets.QLabel(Form)
        self.pushButton.setObjectName("pushButton")
        
        #we have connected clicked signal of button with the selec_data method
        #self.pushButton.clicked.connect(Form.select_data)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout) 
        
        self.retranslateUi(Form)
        self.CustomerPurchase.clicked.connect(self.lCustomerPurchase)
        self.label_2.clicked.connect(self.lCar)
        self.label_3.clicked.connect(self.lEmployeelist)
        self.employee.clicked.connect(self.lemployee)
        self.CustomerNotPurchase.clicked.connect(self.lCustomerNotPurchase)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def lemployee(self):
        try:
            mydb = mc.connect(
 
                host="falcon.cs.wfu.edu",
                user="JiayiZhou",
                password="JiayiZhou321",
                database="321ProjectCars"
            )
 
            mycursor = mydb.cursor()
 
            mycursor.execute("select E.Name as EmployeeName, Co.Name as CustomerName,  C.ListPrice, C.Model from Sales S inner join Employee E inner join Car C inner join Customer Co where E.idEmployee = S.idEmployee and C.idCar = S.idCar and Co.idCustomer = S.idCustomer;")
 
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            # Clear the table
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # Get column names
            column_names = [i[0] for i in mycursor.description]

            # Insert column names as the first row
            self.tableWidget.insertRow(0)
            for column_number, column_name in enumerate(column_names):
                self.tableWidget.setItem(0, column_number, QTableWidgetItem(column_name))

            # Insert data rows
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number + 1)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number + 1, column_number, QTableWidgetItem(str(data)))
 
 

        except mc.Error as e:
            print("Error")
            
    def lCar(self):
        try:
            mydb = mc.connect(
 
                host="falcon.cs.wfu.edu",
                user="JiayiZhou",
                password="JiayiZhou321",
                database="321ProjectCars"
            )
 
            mycursor = mydb.cursor()
 
            mycursor.execute("select * from Car")
            result = mycursor.fetchall()
 
            # Clear the table
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # Get column names
            column_names = [i[0] for i in mycursor.description]

            # Insert column names as the first row
            self.tableWidget.insertRow(0)
            for column_number, column_name in enumerate(column_names):
                self.tableWidget.setItem(0, column_number, QTableWidgetItem(column_name))

            # Insert data rows
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number + 1)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number + 1, column_number, QTableWidgetItem(str(data)))


        except mc.Error as e:
            print("Error")
            
    def lEmployeelist(self):
        try:
            mydb = mc.connect(
 
                host="falcon.cs.wfu.edu",
                user="JiayiZhou",
                password="JiayiZhou321",
                database="321ProjectCars"
            )
 
            mycursor = mydb.cursor()
 
            mycursor.execute("select * from Employee")
 
            result = mycursor.fetchall()
            # Clear the table
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # Get column names
            column_names = [i[0] for i in mycursor.description]

            # Insert column names as the first row
            self.tableWidget.insertRow(0)
            for column_number, column_name in enumerate(column_names):
                self.tableWidget.setItem(0, column_number, QTableWidgetItem(column_name))

            # Insert data rows
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number + 1)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number + 1, column_number, QTableWidgetItem(str(data)))
 
 

        except mc.Error as e:
            print("Error")
        
    def lCustomerPurchase(self):
        try:
            mydb = mc.connect(
 
                host="falcon.cs.wfu.edu",
                user="JiayiZhou",
                password="JiayiZhou321",
                database="321ProjectCars"
            )
 
            mycursor = mydb.cursor()
 
            mycursor.execute("SELECT Name FROM Customer where Purchase =1")
 
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            # Clear the table
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # Get column names
            column_names = [i[0] for i in mycursor.description]

            # Insert column names as the first row
            self.tableWidget.insertRow(0)
            for column_number, column_name in enumerate(column_names):
                self.tableWidget.setItem(0, column_number, QTableWidgetItem(column_name))

            # Insert data rows
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number + 1)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number + 1, column_number, QTableWidgetItem(str(data)))
 
 

        except mc.Error as e:
            print("Error")
        
    def lCustomerNotPurchase(self):
        try:
            mydb = mc.connect(
 
                host="falcon.cs.wfu.edu",
                user="JiayiZhou",
                password="JiayiZhou321",
                database="321ProjectCars"
            )
 
            mycursor = mydb.cursor()
 
            mycursor.execute("SELECT Name FROM Customer where Purchase =0")
 
            result = mycursor.fetchall()
    
            # Clear the table
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # Get column names
            column_names = [i[0] for i in mycursor.description]

            # Insert column names as the first row
            self.tableWidget.insertRow(0)
            for column_number, column_name in enumerate(column_names):
                self.tableWidget.setItem(0, column_number, QTableWidgetItem(column_name))

            # Insert data rows
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number + 1)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number + 1, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error")
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Car Dealershop"))
        self.label.setText(_translate("Form", "Click the buttons to view"))
        self.label_2.setText(_translate("Form", "Car Information"))
        self.label_3.setText(_translate("Form", "Employee List"))
        self.CustomerPurchase.setText(_translate("Form", "Customer who purchased"))
        self.CustomerNotPurchase.setText(_translate("Form", "Customer who not purchased"))
        self.employee.setText(_translate("Form", "Sale Report"))
        self.pushButton.setText(_translate("Form", "That is all the result. Thank you so much."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())