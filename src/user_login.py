import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.create_connection()

        self.init_ui()

    def create_connection(self):
        conn = sqlite3.connect("database.db")

        createString = "Create Table If Not Exists users (username TEXT,password TEXT)"
        self.cursor = conn.cursor()
        self.cursor.execute(createString)

        conn.commit()

    def init_ui(self):

        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_login = QtWidgets.QPushButton("Giriş")
        self.textarea = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.textarea)
        v_box.addStretch()
        v_box.addWidget(self.btn_login)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Giriş Ekranı")
        self.btn_login.clicked.connect(self.login)

        self.show()

    def login(self):
        username = self.username.text()
        password = self.password.text()

        self.cursor.execute("Select * From users Where username = ? and password = ?",(username,password))

        data = self.cursor.fetchall()

        print(data)

        if len(data) == 0:
            self.textarea.setText("Böyle bir kullanıcı mevcut değil !")
        else:
            self.textarea.setText("Giriş başarılı")





app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())