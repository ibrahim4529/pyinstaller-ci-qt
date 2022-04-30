import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow
                                                     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.resize(400, 400)
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    window.setCentralWidget(label)
    window.show()
    sys.exit(app.exec_())