import sys

from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QHBoxLayout


class MyDialog(QDialog):
    """
    A simple dialog with a label, a textbox and a button.
    """

    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of MyDialog")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        super().__init__(None)
        print("Initializing MyClass")
        self.button = None
        self.textbox = None
        self.label = None
        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle("My Dialog")
        self.label = QLabel("Enter your name:")
        self.textbox = QLineEdit()
        self.button = QPushButton("OK")

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.textbox)
        hbox.addWidget(self.button)

        self.setLayout(hbox)

        self.button.clicked.connect(self.on_button_click)

        self.show()

    def on_button_click(self):
        name = self.textbox.text()
        print(f"Hello, {name}!")
        self.accept()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog()
    sys.exit(app.exec_())
