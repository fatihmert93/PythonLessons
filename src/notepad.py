import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog,QMainWindow,QAction,qApp



class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.textarea = QTextEdit()

        self.btn_clean = QPushButton("Clean")
        self.btn_open = QPushButton("Open File")
        self.btn_save = QPushButton("Save File")

        hbox = QHBoxLayout()

        hbox.addWidget(self.btn_clean)
        hbox.addWidget(self.btn_open)
        hbox.addWidget(self.btn_save)

        vbox = QVBoxLayout()

        vbox.addWidget(self.textarea)
        vbox.addLayout(hbox)
        self.setWindowTitle("Notepad++")

        self.setLayout(vbox)

        self.btn_clean.clicked.connect(self.clean_text)
        self.btn_save.clicked.connect(self.save_file)
        self.btn_open.clicked.connect(self.open_file)



    def clean_text(self):
        self.textarea.clear()

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
        with open(filename[0],"r") as file:
            self.textarea.setText(file.read())

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))

        with open(filename[0],"w") as file:
            file.write(self.textarea.toPlainText())

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.notepad = Notepad()

        self.setCentralWidget(self.notepad)

        self.create_menus()

    def create_menus(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")

        action_openfile = QAction("Open File",self)
        action_openfile.setShortcut("Ctrl+O")

        action_savefile = QAction("Save File", self)
        action_savefile.setShortcut("Ctrl+S")

        action_clean = QAction("Clean", self)
        action_clean.setShortcut("Ctrl+D")

        action_quit = QAction("Quit", self)
        action_quit.setShortcut("Ctrl+Q")

        file.addAction(action_savefile)
        file.addAction(action_openfile)
        file.addAction(action_clean)
        file.addAction(action_quit)

        file.triggered.connect(self.response)

        self.setWindowTitle("Text Editor")
        self.show()

    def response(self,action):
        if(action.text() == "Open File"):
            self.notepad.open_file()
        elif(action.text() == "Save File"):
            self.notepad.save_file()
        elif (action.text() == "Clean"):
            self.notepad.clean_text()
        elif (action.text() == "Quit"):
            qApp.quit()



app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())

