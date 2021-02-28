from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import sys

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("LoginUI/login.ui", self)
        self.loginButton.clicked.connect(self.login_func)
        self.signupButton.clicked.connect(self.show_signup)

    # Login the user
    def login_func(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        if username == "root" and password == "root":
            qtw.QMessageBox.information(self, "Success", "You are logged in.")
        else:
            qtw.QMessageBox.critical(self, "Fail", "Failed to login!")

    # Prompt signup screen
    def show_signup(self):
        widget.addWidget(Signup())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("LoginUI/signup.ui", self)
        self.signupButton.clicked.connect(self.signup_func)
    
    def signup_func(self):
        email = self.usernameInput.text()
        password = self.passwordInput.text()
        if password == self.confirmPasswordInput.text() and len(password) > 0:
            qtw.QMessageBox.information(self, "Success", "Successfully created account.")
            # Go back to Login screen
            widget.addWidget(Login())
            widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
mainWindow = Login()
widget = qtw.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()

app.exec_()
