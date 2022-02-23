"""
Hospital patient data base tool used to track patients and ailments.
"""
import sys
from PySide6.QtWidgets import *

import sys
initializetxt = open('patient_db.txt', "a")


class Patient(object):
    """
    A Patient is a person who has come to see the doctor. 
    they have name, age, weight, height, gender
    """
    def __init__(self, patnum, lname, fname, age, weight, height, bloodtype):
        """
        Initializes a patient with patient number, last name, firstname, age, weight, height, bloodtype
        """
        
        self.height = height
        self.weight = weight
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.bloodtype = bloodtype
        self.age = age
        self.patnum = patnum

    def to_string(self):
        """
        turns a patient class into a string for storage in the txt file.
        """
        return f"{self.patnum} {self.lname} {self.fname} {self.age} {self.weight} {self.height} {self.bloodtype} "
        
    @classmethod
    def get_all_pats(cls):
        """
        get all the patients from the patient_db.txt and initialize them to a class and put in a list.
        """
        all_patients = []
        args = database().patient_strs
        for i in args:
            all_patients.append(cls(*i))
        return all_patients

class database(object):
    """
    database is used to open and manipulate the txt file holding all the patient data.
    """
    def __init__(self):
        self.filename = 'patient_db.txt'
        self.patient_strs = self.initialize_patients()


    def initialize_patients(self):
        """
        Get all the patients from the patient_db.txt
        """
        txt = open(self.filename, 'r')
        patient_strs = txt.read().splitlines()
        patient_strs = [x.split() for x in patient_strs]
        return patient_strs
    
    
    def add_db(self, patient):
        """
        Append patient to the end of the patient_db.txt

        patient: a string 
        """
    
        with open(self.filename, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(patient.to_string())

    def get_patnum(self):
        """
        gets the new patient number.
        """
        
        if self.patient_strs == []:
            return 1
        else:
            return int(self.patient_strs[-1][0]) + 1



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
        self.display_pat = Display_patient()
        

    def initUI(self):  
        self.lname = QLineEdit()
        self.fname = QLineEdit()
        self.age = QSpinBox()
        self.hgt = QLineEdit()
        self.weight = QLineEdit()
        self.blood = QComboBox()
        self.patnum = str(database().get_patnum())
        self.sex = 's'
        layout = QFormLayout()

    
        
        hbox = QHBoxLayout
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('New Patient Entry')
        self.blood.addItems(['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-'])

        layout.addRow(("Patient #:"), QLabel(self.patnum))
        layout.addRow(("Last Name:"), self.lname)
        layout.addRow(("First Name:"), self.fname)
        layout.addRow(("Age:"), self.age)
        layout.addRow(("Height (cm):"), self.hgt)
        layout.addRow(("Weight (kgs):"), self.weight)
        layout.addRow(("Blood Type:"), self.blood)
        layout.addRow(QLabel('Sex:'), QHBoxLayout())
        layout.addRow(QRadioButton('Male'), QRadioButton('Female'))
        
        layout.addRow(self.buttonBox)

        self.buttonBox.accepted.connect(self.create_pat)
        self.buttonBox.rejected.connect(self.reject)
        
        
        self.setLayout(layout)
        

    def create_pat(self):
        new_pat = Patient(self.patnum, self.lname.text(), self.fname.text(), self.age.text(), self.weight.text(), self.hgt.text(), self.blood.currentText())
        database().add_db(new_pat)

        self.display_pat.patnum.setText(self.patnum)
        self.display_pat.lname.setText(self.lname.text())
        self.display_pat.fname.setText(self.fname.text()) 
        self.display_pat.age.setText(self.age.text())  
        self.display_pat.hgt.setText(self.hgt.text()) 
        self.display_pat.weight.setText(self.weight.text()) 
        self.display_pat.blood.setText(self.blood.currentText()) 
        self.sex = QLabel()

        self.display_pat.show()
        
    
        self.close()

        
class Search_window(QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    This window will allow you to search through all patients in the patient class.
    """
    def __init__(self):
        super().__init__()
        self.display_pat = Display_patient()

        self.initUI()
        
    def initUI(self):  
        layout = QFormLayout()
        self.lname = QLineEdit()
        self.patnum = QLineEdit()
        backbtn = QDialogButtonBox.Cancel
        self.box = QDialogButtonBox(backbtn)
        self.search1 = QPushButton('Search')
        self.search2 = QPushButton('Search')
        self.namerr = QLabel()
        self.numerr = QLabel()

        layout.addRow('', self.namerr)
        layout.addRow(("Last Name:"), self.lname)
        layout.addRow('', self.search1)
        layout.addRow('', self.numerr)
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
        names = Patient.get_all_pats()
        for Patient.lname in names:
            if Patient.lname == self.lname.text().capitalize():
                print('found')
            else:
                self.namerr.setText(self.lname.text().capitalize() + ': Not Found')
        
    
    def patnum_search(self):
        numbers = [x.patnum for x in Patient.get_all_pats()]
        for i in numbers:
            if int(i) == int(self.patnum.text()):
                self.display_pat.patnum.setText(str(int(i)-1))
                self.display_pat.lname.setText((Patient.get_all_pats())[(int(i)-1)].lname)
                self.display_pat.fname.setText((Patient.get_all_pats())[(int(i)-1)].fname) 
                self.display_pat.age.setText((Patient.get_all_pats())[(int(i)-1)].age)  
                self.display_pat.hgt.setText((Patient.get_all_pats())[(int(i)-1)].height) 
                self.display_pat.weight.setText((Patient.get_all_pats())[(int(i)-1)].weight) 
                self.display_pat.blood.setText((Patient.get_all_pats())[(int(i)-1)].bloodtype) 
                self.sex = QLabel()
                
                self.close()
                self.display_pat.show()
            else:
                self.numerr.setText('Patient #' + self.patnum.text() + ': Not Found')

class Display_patient(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    This window will display patient information.
    """
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self): 
        self.patnum = QLabel()
        self.lname = QLabel()
        self.fname = QLabel() 
        self.age = QLabel() 
        self.hgt = QLabel() 
        self.weight = QLabel() 
        self.blood = QLabel() 
        self.sex = QLabel()
        layout = QFormLayout()
    
        
       
        self.setLayout(layout)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Patient info')

        layout.addRow(("Patient #:"), self.patnum)
        layout.addRow(("Last Name:"), self.lname)
        layout.addRow(("First Name:"), self.fname)
        layout.addRow(("Age:"), self.age)
        layout.addRow(("Height (cm):"), self.hgt)
        layout.addRow(("Weight (kgs):"), self.weight)
        layout.addRow(("Blood Type:"), self.blood)
        
def main():
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()