import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

# Create a subclass of QWidget to create the main window of the application
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle('PyQt5 GUI Example')
        self.setGeometry(100, 100, 300, 200)

        # Create a label and button widget
        self.label = QLabel('Click the button to display a message', self)
        self.button = QPushButton('Click me', self)

        # Create a vertical layout for the label and button widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set the main layout for the window
        self.setLayout(layout)

        # Connect the button click event to the showMessage function
        self.button.clicked.connect(self.showMessage)

    # Define the showMessage function to display a message when the button is clicked
    def showMessage(self):
        self.label.setText('Hello, PyQt5!')

if __name__ == '__main__':
    # Create a new QApplication instance
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()

    # Show the main window
    window.show()

    # Run the event loop
    sys.exit(app.exec_())
