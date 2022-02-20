"""
Hospital patient data base tool used to track patients and ailments.
"""
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
    QSpinBox
)

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
        self.patnum = patnum #self.get_patnum()
        # self.patlist = self.get_all_pats()

    def get_patnum(self):
        """
        gets the new patient number.
        """
        database()
        if database().patient_strs == []:
            return 1
        else:
            return int(database().patient_strs[-1][0]) + 1
        
       


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



class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.w = None
        self.initUI()
        self.New_Patient_window = New_Patient_window()
        self.Search_window = Search_window()
        
    def initUI(self):      
        
       
        btn1 = QPushButton("New Patient", self)
        btn1.move(30, 50)
        btn1.clicked.connect(self.goto_newpat)
        btn2 = QPushButton("Search", self)
        btn2.move(150, 50)
      
                   
        btn2.clicked.connect(self.goto_search)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Patient Database')
        self.show()

    def goto_newpat(self, checked):
        if self.New_Patient_window.isVisible():
            self.New_Patient_window.hide()

        else:
            self.New_Patient_window.show()

    def goto_search(self, checked):
        if self.Search_window.isVisible():
            self.Search_window.hide()

        else:
            self.Search_window.show()


class New_Patient_window(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):  
        layout = QFormLayout()
        
        
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('New Patient Entry')
        combobox1 = QComboBox()
        combobox1.addItems(['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-'])
        layout.addRow(("Last Name:"), QLineEdit())
        layout.addRow(("First Name:"), QLineEdit())
        layout.addRow(("Age:"), QSpinBox())
        layout.addRow(("Height (cm):"), QLineEdit())
        layout.addRow(("Weight (kgs):"), QLineEdit())
        layout.addRow(("Blood Type:"), combobox1)
        self.setLayout(layout)
        
        

class Search_window(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):  
        layout = QVBoxLayout()
       
        self.setLayout(layout)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Search')
        

        
def main():
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


    

    
    # def create_list(self):
    #     """
    #     Creates the list that lists patient info in individual strings.
    #     """
    #     pass
    #     # data = [x.split() for x in self.patient_strs]
    #     # return data

    



#patients_list = [Patient('Brady', 'tom', 225, 75, 'O+', 34)]


# Patient('Brady', 'tom', 225, 75, 'O+', 34).get_patnum()
# database().initialize_patients()
# database().add_db((patients_list[0]))
# database().create_list()
# print(database().patient_strs)
print(Patient.get_all_pats())

