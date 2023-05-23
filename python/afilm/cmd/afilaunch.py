# ----------------------------------------------------------------------------------------------------------------------
# file       : afilm.cmd.afilaunch
# created    : 23/05/2023
# email      : js@anim.dk
#
# A Wrapper for launching software inside of a production context.
# ----------------------------------------------------------------------------------------------------------------------

from PySide2 import QtWidgets
import sys


# Build the UI.
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowTitle("afiLaunch")
        self.create_menus()

        self.show()

    def create_menus(self):
        self.file_menu = self.menuBar().addMenu("&File")
        self.help_menu = self.menuBar().addMenu("&Help")


# Open Launcher window.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


