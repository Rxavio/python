from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def showMessage(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    
        
    def viewData(self):
         connection = sqlite3.connect("student.db")
         query="SELECT * FROM details"
         result=connection.execute(query)
         self.tableWidget.setRowCount(0)
         for row_number,row_data in enumerate(result):
             self.tableWidget.insertRow(row_number)
             for column_number,data in enumerate(row_data):
                 self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
         connection.close()
         
    def addData(self):
        u_id= self.textid.text()
        u_name = self.textname.text()
        u_age= self.textage.text()
        u_class = self.textclass.text()
        connection  = sqlite3.connect("student.db")
        
        if u_id == "" or u_name == "" or u_age == "" or u_class == "":
            self.showMessage('information','Please complete the required field!')
        else:
            connection.execute("INSERT INTO details VALUES(?,?,?,?)",(u_id,u_name,u_age,u_class))
            connection.commit()
            connection.close()
            self.showMessage('information','successfully Added')
        
    def reset(self):
        u_id= self.textid.text()
        u_name = self.textname.text()
        u_age= self.textage.text()
        u_class = self.textclass.text()
        
        if u_id == "" and u_name == "" and u_age == "" and u_class == "":
            self.showMessage('information','oops,Empty field!')
        else:
            self.textid.setText("")
            self.textname.setText("")
            self.textage.setText("")
            self.textclass.setText("")
            
    def deleteData(self):
        u_id= self.textid.text()
        if u_id == "":
            self.showMessage('information','Oops,enter Id to delete')
            
        else:
            connection = sqlite3.connect("student.db")
            connection.execute("DELETE FROM details WHERE id="+str(u_id))
            self.showMessage('information','succesfully deleted!')
            connection.commit()
            connection.close()
      
        
     
        
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 379)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/Photos/cartoonD/bb.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(10, 50, 47, 13))
        
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 47, 13))
        self.label_4.setObjectName("label_4")
        self.textid = QtWidgets.QLineEdit(self.centralwidget)
        self.textid.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.textid.setObjectName("textid")
        
        self.textid.setPlaceholderText("Enter Id")
        
        self.textname = QtWidgets.QLineEdit(self.centralwidget)
        self.textname.setGeometry(QtCore.QRect(100, 110, 113, 20))
        self.textname.setObjectName("textname")
        
        self.textname.setPlaceholderText("Enter Name")
         
        self.textage = QtWidgets.QLineEdit(self.centralwidget)
        self.textage.setGeometry(QtCore.QRect(100, 170, 113, 20))
        self.textage.setObjectName("textage")

        self.textage.setPlaceholderText("Enter Age")
         
        self.textclass = QtWidgets.QLineEdit(self.centralwidget)
        self.textclass.setGeometry(QtCore.QRect(100, 230, 113, 20))
        self.textclass.setObjectName("textclass")

        self.textclass.setPlaceholderText("Enter class")
         
        self.btnclear = QtWidgets.QPushButton(self.centralwidget)
        self.btnclear.setGeometry(QtCore.QRect(20, 320, 75, 23))
        self.btnclear.setObjectName("btnclear")
        ###################button event ############################################3
        self.btnclear.clicked.connect(self.reset)
        ###################button event ############################################
        
        self.btnadd = QtWidgets.QPushButton(self.centralwidget)
        self.btnadd.setGeometry(QtCore.QRect(110, 320, 75, 23))
        self.btnadd.setObjectName("btnadd")
        ###################button event ############################################3
        self.btnadd.clicked.connect(self.addData)
        ###################button event ############################################
        self.btnupdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnupdate.setGeometry(QtCore.QRect(210, 320, 75, 23))
        self.btnupdate.setObjectName("btnupdate")

      
        ###################button event ############################################
        
        self.btndelete = QtWidgets.QPushButton(self.centralwidget)
        self.btndelete.setGeometry(QtCore.QRect(310, 320, 75, 23))
        self.btndelete.setObjectName("btndelete")
        ###################button event ############################################3
        self.btndelete.clicked.connect(self.deleteData)
        ###################button event ############################################

        
        self.btnsearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnsearch.setGeometry(QtCore.QRect(510, 320, 75, 23))
        self.btnsearch.setObjectName("btnsearch")
        self.btnview = QtWidgets.QPushButton(self.centralwidget)
        self.btnview.setGeometry(QtCore.QRect(410, 320, 75, 23))
        self.btnview.setObjectName("btnview")

        ###################button event ############################################3
        self.btnview.clicked.connect(self.viewData)
        ###################button event ############################################
        
        self.btnexit = QtWidgets.QPushButton(self.centralwidget)
        self.btnexit.setGeometry(QtCore.QRect(610, 320, 75, 23))
        self.btnexit.setObjectName("btnexit")
        
       

        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(230, 40, 451, 251))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setHorizontalHeaderLabels(('ID', 'NAMES','AGE','CLASS'))
        
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEST"))
        self.id.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "NAMES"))
        self.label_3.setText(_translate("MainWindow", "AGE"))
        self.label_4.setText(_translate("MainWindow", "CLASS"))
        self.btnclear.setText(_translate("MainWindow", "clear"))
        self.btnadd.setText(_translate("MainWindow", "add"))
        self.btnupdate.setText(_translate("MainWindow", "Update"))
        self.btndelete.setText(_translate("MainWindow", "Delete"))
        self.btnsearch.setText(_translate("MainWindow", "Search"))
        self.btnview.setText(_translate("MainWindow", "View"))
        self.btnexit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

