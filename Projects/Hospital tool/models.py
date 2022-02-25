"""
Hospital patient data base tool used to track patients and ailments.
"""




initializetxt = open("patient_db.txt", "a")


class Patient(object):
    """
    A Patient is a person who has come to see the doctor.
    they have name, age, weight, height, gender
    """

    def __init__(self, patnum, lname, fname, age, weight, height, bloodtype, sex):
        """
        Initializes a patient with patient number, last name, firstname, age, weight, height, bloodtype
        """
        
        self.patnum = patnum
        self.lname = lname.capitalize()
        self.fname = fname.capitalize()
        self.age = age
        self.weight = weight
        self.height = height
        self.bloodtype = bloodtype
        self.sex = sex

    def to_string(self):
        """
        turns a patient class into a string for storage in the txt file.
        """
        return f"{self.patnum} {self.lname} {self.fname} {self.age} {self.weight} {self.height} {self.bloodtype} {self.sex} "

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
        self.filename = "patient_db.txt"
        self.patient_strs = self.initialize_patients()

    def initialize_patients(self):
        """
        Get all the patients from the patient_db.txt
        """
        txt = open(self.filename, "r")
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


