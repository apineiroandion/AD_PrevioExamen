import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QLabel, \
    QGridLayout, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        titulo = "SPARTAN PASSWORD PROTECTOR"
        self.setWindowTitle(titulo)
        self.setGeometry(100, 100, 800, 600)


        caja_v = QVBoxLayout()
        container = QWidget()
        container.setLayout(caja_v)
        self.setCentralWidget(container)

        botones_h = BotonesLayout()
        title_h = TitleLayout(titulo)
        caja_h = BodyLayout()

        caja_v.addLayout(botones_h)
        caja_v.addLayout(title_h)
        caja_v.addLayout(caja_h)


        self.show()


class BotonesLayout(QHBoxLayout):
        def __init__(self):
            super().__init__()

            self.boton_add = QPushButton("Añadir")
            self.boton_add.setFixedHeight(150)
            self.boton_editar = QPushButton("Editar")
            self.boton_editar.setFixedHeight(150)
            self.boton_eliminar = QPushButton("Eliminar")
            self.boton_eliminar.setFixedHeight(150)
            self.boton_aceptar = QPushButton("Aceptar")
            self.boton_aceptar.setFixedHeight(150)

            self.addWidget(self.boton_add)
            self.addWidget(self.boton_editar)
            self.addWidget(self.boton_eliminar)
            self.addWidget(self.boton_aceptar)

class TitleLayout(QHBoxLayout):
    def __init__(self, titulo=""):
        super().__init__()

        font = QFont()
        font.setPointSize(20)

        self.title = QLabel(titulo)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(font)

        self.addWidget(self.title)

class BodyLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        left_v = LeftLayout()
        right_v = QVBoxLayout()

        self.addLayout(left_v)
        self.addLayout(right_v)

class LeftLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        login_g = LoginLayout()
        log_v = QVBoxLayout()

        self.addLayout(login_g)
        self.addLayout(log_v)

class LoginLayout(QGridLayout):
    def __init__(self):
        super().__init__()

        buttons_h = QHBoxLayout()

        title = QLabel("Login")
        username_label = QLabel("Username")
        password_label = QLabel("Password")
        username_text = QLineEdit()
        password_text = QLineEdit()
        login_button = QPushButton("Login")
        forgot_button = QPushButton("Forgot Password")

        buttons_h.addStretch()
        buttons_h.addWidget(login_button)
        buttons_h.addWidget(forgot_button)

        self.addWidget(title, 0, 0)
        self.addWidget(username_label, 1, 0)
        self.addWidget(password_label, 1, 1)
        self.addWidget(username_text, 2, 0)
        self.addWidget(password_text, 2, 1)
        self.addLayout(buttons_h, 3,0, 1, 2)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()