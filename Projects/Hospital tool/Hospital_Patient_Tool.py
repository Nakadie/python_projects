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
        self.lname = QLineEdit()
        self.fname = QLineEdit()
        self.age = QSpinBox()
        self.hgt = QLineEdit()
        self.weight = QLineEdit()
        self.blood = QComboBox()
        self.sex = 's'
        layout = QFormLayout()
    
        
        hbox = QHBoxLayout
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('New Patient Entry')
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

        self.buttonBox.accepted.connect(self.create_pat)
        self.buttonBox.rejected.connect(self.reject)
        
        
        self.setLayout(layout)
        print(self.lname.text)

    def create_pat(self):
        new_pat = Patient(database().get_patnum(), self.lname.text(), self.fname.text(), self.age.text(), self.weight.text(), self.hgt.text(), self.blood.currentText())
        database().add_db(new_pat)
    
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
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


    

    
    def create_list(self):
        """
        Creates the list that lists patient info in individual strings.
        """
        pass
        # data = [x.split() for x in self.patient_strs]
        # return data

    



#patients_list = [Patient('Brady', 'tom', 225, 75, 'O+', 34)]


# Patient('Brady', 'tom', 225, 75, 'O+', 34).get_patnum()
# database().initialize_patients()
# database().add_db((patients_list[0]))
# database().create_list()
# print(database().patient_strs)


