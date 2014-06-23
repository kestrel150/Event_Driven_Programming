#Aaron Parker
#170614
#Event Driven Programming

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")

        self.stacked_layout =  QStackedLayout()
        self.stacked_widget = QWidget()
        self.stacked_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.stacked_widget)

        self.create_main_layout()
        self.create_hello_layout()
        
        self.stacked_layout.setCurrentIndex(0) #sets the layout that will show first
        

    def create_main_layout(self):
        #widgets
        self.text_box = QLineEdit()
        self.submit_button = QPushButton("Submit")
        #layout
        self.layout = QVBoxLayout()
        #widgets
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)
        #Widget to hold layout
        self.widget = QWidget()
        #add layout to widget
        self.widget.setLayout(self.layout)
        #set central widget
        self.stacked_layout.addWidget(self.widget)

        self.submit_button.clicked.connect(self.switch_layout)

    def switch_layout(self):
        index = self.stacked_layout.currentIndex()

        self.stacked_layout.setCurrentIndex(1)
        if index == 1:
            name = self.text_box.text()
            self.label.setText("Hello {0}.".format(name))

    def create_hello_layout(self):
        self.label = QLabel()
        self.back_button = QPushButton("Back")

        self.hello_layout = QVBoxLayout()

        self.hello_layout.addWidget(self.label)
        self.hello_layout.addWidget(self.back_button)

        self.hello_widget = QWidget()

        self.hello_widget.setLayout(self.hello_layout)

        self.stacked_layout.addWidget(self.hello_widget)

        self.back_button.clicked.connect(self.switch_layout)
        


        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    window.raise_()
    application.exec_()
    
