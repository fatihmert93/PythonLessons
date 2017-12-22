import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog

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

        self.show()



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



app = QApplication(sys.argv)

notepad = Notepad()

sys.exit(app.exec_())

