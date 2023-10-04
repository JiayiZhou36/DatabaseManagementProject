import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox
import mysql.connector

class AddData(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Add Data')
        self.setGeometry(200, 200, 500, 400)

        # Create labels and line edits for input
        self.name_label = QLabel('Customer ID:')
        self.name_input = QLineEdit()

        self.email_label = QLabel('Customer Name:')
        self.email_input = QLineEdit()

        self.phone_label = QLabel('Customer Purchased:')
        self.phone_input = QLineEdit()

        self.id_label = QLabel('Employee ID:')
        self.id_input = QLineEdit()

        self.name2_label = QLabel('Employee Name:')
        self.name2_input = QLineEdit()

        self.role_label = QLabel('Employee Role:')
        self.role_input = QLineEdit()

        self.car1_label = QLabel('Car ID:')
        self.car1_input = QLineEdit()

        self.car2_label = QLabel('Car Color:')
        self.car2_input = QLineEdit()

        self.car3_label = QLabel('Car Number of Doors:')
        self.car3_input = QLineEdit()

        self.car4_label = QLabel('Car List Price:')
        self.car4_input = QLineEdit()

        self.car5_label = QLabel('Car Weight Capacity:')
        self.car5_input = QLineEdit()

        self.car6_label = QLabel('Car Manufacturer:')
        self.car6_input = QLineEdit()

        self.car7_label = QLabel('Car Model:')
        self.car7_input = QLineEdit()

        self.car8_label = QLabel('Car Date Manufacture (YYYY-MM-DD):')
        self.car8_input = QLineEdit()

        self.car9_label = QLabel('Car Date Delivery (YYYY-MM-DD):')
        self.car9_input = QLineEdit()

        self.car10_label = QLabel('Car Warranty End Date (YYYY-MM-DD):')
        self.car10_input = QLineEdit()

        self.car11_label = QLabel('Car Customization:')
        self.car11_input = QLineEdit()

        self.car12_label = QLabel('Car Trade-in:')
        self.car12_input = QLineEdit()

        # Create a drop-down box to choose which table to insert data into
        self.table_label = QLabel('Insert into table:')
        self.table_selector = QComboBox()
        self.table_selector.addItem('Customer')
        self.table_selector.addItem('Employee')
        self.table_selector.addItem('Car')
        self.table_selector.currentTextChanged.connect(self.update_ui)

        # Create a button to submit the data
        self.submit_button = QPushButton('Add Data')
        self.submit_button.clicked.connect(self.add_data)

        # Create a vertical layout to add widgets to
        vbox = QVBoxLayout()
        vbox.addWidget(self.table_label)
        vbox.addWidget(self.table_selector)
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_input)
        vbox.addWidget(self.email_label)
        vbox.addWidget(self.email_input)
        vbox.addWidget(self.phone_label)
        vbox.addWidget(self.phone_input)
        vbox.addWidget(self.id_label)
        vbox.addWidget(self.id_input)
        vbox.addWidget(self.name2_label)
        vbox.addWidget(self.name2_input)
        vbox.addWidget(self.role_label)
        vbox.addWidget(self.role_input)
        vbox.addWidget(self.car1_label)
        vbox.addWidget(self.car1_input)
        vbox.addWidget(self.car2_label)
        vbox.addWidget(self.car2_input)
        vbox.addWidget(self.car3_label)
        vbox.addWidget(self.car3_input)
        vbox.addWidget(self.car4_label)
        vbox.addWidget(self.car4_input)
        vbox.addWidget(self.car5_label)
        vbox.addWidget(self.car5_input)
        vbox.addWidget(self.car6_label)
        vbox.addWidget(self.car6_input)
        vbox.addWidget(self.car7_label)
        vbox.addWidget(self.car7_input)
        vbox.addWidget(self.car8_label)
        vbox.addWidget(self.car8_input)
        vbox.addWidget(self.car9_label)
        vbox.addWidget(self.car9_input)
        vbox.addWidget(self.car10_label)
        vbox.addWidget(self.car10_input)
        vbox.addWidget(self.car11_label)
        vbox.addWidget(self.car11_input)
        vbox.addWidget(self.car12_label)
        vbox.addWidget(self.car12_input)
        vbox.addWidget(self.submit_button)

        self.setLayout(vbox)

        # Set the initial UI state based on the selected table
        self.update_ui(self.table_selector.currentText())
        
    def update_ui(self, table):
        if table == 'Customer':
            self.name_label.show()
            self.name_input.show()
            self.email_label.show()
            self.email_input.show()
            self.phone_label.show()
            self.phone_input.show()
            self.id_label.hide()
            self.id_input.hide()
            self.name2_label.hide()
            self.name2_input.hide()
            self.role_label.hide()
            self.role_input.hide()
            self.car1_label.hide()
            self.car1_input.hide()
            self.car2_label.hide()
            self.car2_input.hide()
            self.car3_label.hide()
            self.car3_input.hide()
            self.car4_label.hide()
            self.car4_input.hide()
            self.car5_label.hide()
            self.car5_input.hide()
            self.car6_label.hide()
            self.car6_input.hide()
            self.car7_label.hide()
            self.car7_input.hide()
            self.car8_label.hide()
            self.car8_input.hide()
            self.car9_label.hide()
            self.car9_input.hide()
            self.car10_label.hide()
            self.car10_input.hide()
            self.car11_label.hide()
            self.car11_input.hide()
            self.car12_label.hide()
            self.car12_input.hide()
        elif table == 'Employee':
            self.id_label.show()
            self.id_input.show()
            self.name2_label.show()
            self.name2_input.show()
            self.role_label.show()
            self.role_input.show()
            self.name_label.hide()
            self.name_input.hide()
            self.email_label.hide()
            self.email_input.hide()
            self.phone_label.hide()
            self.phone_input.hide()
            self.car1_label.hide()
            self.car1_input.hide()
            self.car2_label.hide()
            self.car2_input.hide()
            self.car3_label.hide()
            self.car3_input.hide()
            self.car4_label.hide()
            self.car4_input.hide()
            self.car5_label.hide()
            self.car5_input.hide()
            self.car6_label.hide()
            self.car6_input.hide()
            self.car7_label.hide()
            self.car7_input.hide()
            self.car8_label.hide()
            self.car8_input.hide()
            self.car9_label.hide()
            self.car9_input.hide()
            self.car10_label.hide()
            self.car10_input.hide()
            self.car11_label.hide()
            self.car11_input.hide()
            self.car12_label.hide()
            self.car12_input.hide()
        elif table == 'Car':
            self.car1_label.show()
            self.car1_input.show()
            self.car2_label.show()
            self.car2_input.show()
            self.car3_label.show()
            self.car3_input.show()
            self.car4_label.show()
            self.car4_input.show()
            self.car5_label.show()
            self.car5_input.show()
            self.car6_label.show()
            self.car6_input.show()
            self.car7_label.show()
            self.car7_input.show()
            self.car8_label.show()
            self.car8_input.show()
            self.car9_label.show()
            self.car9_input.show()
            self.car10_label.show()
            self.car10_input.show()
            self.car11_label.show()
            self.car11_input.show()
            self.car12_label.show()
            self.car12_input.show()
            self.id_label.hide()
            self.id_input.hide()
            self.name2_label.hide()
            self.name2_input.hide()
            self.role_label.hide()
            self.role_input.hide()
            self.name_label.hide()
            self.name_input.hide()
            self.email_label.hide()
            self.email_input.hide()
            self.phone_label.hide()
            self.phone_input.hide()
        
    def add_data(self):
        # Connect to the MySQL database
        try:
            mydb = mysql.connector.connect(
                host="falcon.cs.wfu.edu",
                user="AliceLi",
                password="AliceLi321",
                database="321ProjectCars"
            )

            # Create a cursor object to execute SQL queries
            mycursor = mydb.cursor()

            # Insert the data into the selected table
            table = self.table_selector.currentText()
            if table == 'Customer':
                sql = "INSERT INTO Customer (idCustomer, Name, Purchase) VALUES (%s, %s, %s)"
                val = (self.name_input.text(), self.email_input.text(), self.phone_input.text())
            elif table == 'Employee':
                sql = "INSERT INTO Employee (idEmployee, Name, Role) VALUES (%s, %s, %s)"
                val = (self.id_input.text(), self.name2_input.text(), self.role_input.text())
            elif table == 'Car':
                sql = "INSERT INTO Car (idCar, NumberDoors, ListPrice, WeightCapacity, Manufacturer, Model, Color, DateManufacture, DateDelivery, WarrantyEndDate, Customization, Trade-in) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.car1_input.text(), self.car2_input.text(), self.car3_input.text(), car4_input.text(), self.car5_input.text(), self.car6_input.text(), car7_input.text(), self.car8_input.text(), self.car9_input.text(), car10_input.text(), self.car11_input.text(), self.car12_input.text(),)
            
            mycursor.execute(sql, val)
            mydb.commit()

            # Show a message box to indicate success
            msg_box = QMessageBox()
            msg_box.setText('Data added to {} table.'.format(table))
            msg_box.exec_()
            
        except mysql.connector.Error as error:
            # Show an error message if the data cannot be added
            print("Failed to insert record into table: {}".format(error))
            msg_box = QMessageBox()
            msg_box.setText('Failed to add data to {} table.'.format(table))
            msg_box.exec_()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    add_data = AddData()
    add_data.show()
    sys.exit(app.exec_())

