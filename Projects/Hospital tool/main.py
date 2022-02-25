import views
import sys

def main():

    app = views.QApplication(sys.argv)
    ex = views.MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()