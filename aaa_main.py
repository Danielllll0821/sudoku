import sys
import aaa
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = aaa.Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
