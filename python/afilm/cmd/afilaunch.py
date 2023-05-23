# ----------------------------------------------------------------------------------------------------------------------
# file       : afilm.cmd.afilaunch
# created    : 23/05/2023
# email      : js@anim.dk
#
# A Wrapper for launching software inside of a production context.
# ----------------------------------------------------------------------------------------------------------------------

import sys
from PySide2 import QtWidgets
import afilm.core.ui


# Build the UI.
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowTitle("afiLaunch")
        self.create_actions()
        self.create_menus()
        self.create_statusbar()


        self._main_widget = QtWidgets.QPushButton('Hello')
        self.setCentralWidget(self._main_widget)

        afilm.core.ui.center_on_screen(self)

    def create_actions(self):
        """"""
        pass

    def create_menus(self):
        """"""
        self.file_menu = self.menuBar().addMenu("&File")
        self.help_menu = self.menuBar().addMenu("&Help")

    def create_statusbar(self):
        """"""
        self.statusbar_label = QtWidgets.QLabel("")
        self.statusBar().showMessage("Ready")
        self.statusBar().addPermanentWidget(self.statusbar_label)


# Open Launcher window.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


