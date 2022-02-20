import sys
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QMainWindow
    
)


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
        layout = QVBoxLayout()
        
        
        self.setLayout(layout)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('New Patient Entry')
        

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

