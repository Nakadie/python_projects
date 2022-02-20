from re import search
import sys
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QMainWindow,
    QFormLayout,
    QLayout,
    QLayoutItem,
    QLabel,
    QComboBox,
    QLineEdit,
    QSpinBox,
    QRadioButton,
    QDialogButtonBox,
    QDialog
    
)
initializetxt = open('gui_tester.txt', "a")

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.w = None
        self.initUI()
        self.New_Patient_window = New_Patient_window()
        self.Search_window = Search_window()
        
    def initUI(self):      
        # initialize ui for main window
       
        self.btn1 = QPushButton("New Patient", self)
        self.btn1.move(30, 50)
        self.btn1.clicked.connect(self.goto_newpat)

        self.btn2 = QPushButton("Search", self)
        self.btn2.move(150, 50)   
        self.btn2.clicked.connect(self.goto_search)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Patient Database')
        self.show()

    def goto_newpat(self, checked):
        self.newpat = New_Patient_window()
        self.newpat.show()

    def goto_search(self, checked):
        """"""
        self.search = Search_window()
        self.search.show()

class New_Patient_window(QDialog):
    """
    This "window" is a QDialog. If it has no parent, it
    will appear as a free-floating window as we want.
    This window will allow entry for patient data then store it in the patient class 
    then save to the txt file.
    """
    def __init__(self):
        super().__init__()
        
        self.initUI()
        

    def initUI(self):  

        #variables
        self.lname = QLineEdit()
        self.fname = QLineEdit()
        self.age = QSpinBox()
        self.hgt = QLineEdit()
        self.weight = QLineEdit()
        self.blood = QComboBox()
        self.sex = 's'
        layout = QFormLayout()
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)

        # Window Setup
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('New Patient Entry')
        
        #table setup
        self.blood.addItems(['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-'])
        layout.addRow(("Last Name:"), self.lname)
        layout.addRow(("First Name:"), self.fname)
        layout.addRow(("Age:"), self.age)
        layout.addRow(("Height (cm):"), self.hgt)
        layout.addRow(("Weight (kgs):"), self.weight)
        layout.addRow(("Blood Type:"), self.blood)
        layout.addRow(QLabel('Sex:'), QHBoxLayout())
        layout.addRow(QRadioButton('Male'), QRadioButton('Female'))
        layout.addRow(self.buttonBox)

        #Button commands.
        self.buttonBox.accepted.connect(self.create_pat)
        self.buttonBox.rejected.connect(self.reject)
        
        
        self.setLayout(layout)
        print(self.lname.text)

    def create_pat(self):
  
        
        print("last name : {0}".format(self.lname.text()))
        print("bloodtype : {0}".format(self.blood.currentText()))
        print("Age : {0}".format(self.age.text()))

        # closing the window
        self.close()

        
class Search_window(QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    This window will allow you to search through all patients in the patient class.
    """
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):  
        layout = QFormLayout()
        self.lname = QLineEdit()
        self.patnum = QLineEdit()
        backbtn = QDialogButtonBox.Cancel
        self.box = QDialogButtonBox(backbtn)
        self.search1 = QPushButton('Search')
        self.search2 = QPushButton('Search')
        layout.addRow(("Last Name:"), self.lname)
        layout.addRow('', self.search1)
        layout.addRow(("Patient #:"), self.patnum)
        layout.addRow('', self.search2)
        layout.addRow('', self.box)
        self.setLayout(layout)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Search')

        self.box.rejected.connect(self.reject)

        self.search1.clicked.connect(self.name_search)
        self.search2.clicked.connect(self.patnum_search)

    def name_search(self):
        print(self.lname.text())
        self.close()
    
    def patnum_search(self):
        print(self.patnum.text())
        self.close()
        

        
def main():
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

