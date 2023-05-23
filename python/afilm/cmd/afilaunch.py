# ----------------------------------------------------------------------------------------------------------------------
# file       : afilm.cmd.afilaunch
# created    : 23/05/2023
# email      : js@anim.dk
#
# A Wrapper for launching software inside of a production context.
# ----------------------------------------------------------------------------------------------------------------------

import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

import afilm.core.pipeline
import afilm.core.ui


print(afilm.core.pipeline.pipeline_root())

# Build the UI.
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowTitle("afiPipeline | Launch")
        self.create_actions()
        self.create_menus()
        self.create_statusbar()
        self.create_toolbar()
        self._main_widget = QtWidgets.QPushButton('Hello')
        self.setCentralWidget(self._main_widget)

        afilm.core.ui.apply_style(self)
        afilm.core.ui.center_on_screen(self)

    def create_actions(self):
        """"""
        #self.about_action = QtWidgets.QAction(QtGui.QIcon('image/Information-icon.png'), "About", self, statusTip="Show the application's About box", triggered=self.about)
        self.quit_action = QtWidgets.QAction(QtGui.QIcon('image/remove-icon.png'), '&Quit', self,
                                             shortcut=QtGui.QKeySequence.Quit, statusTip='Quit', triggered=self.quit)
        #self.websiteAction = QtGui.QAction("Launcher Documentation", self, statusTip="Show Launcher Documentation", triggered=self.website)

    def create_menus(self):
        """"""
        self.file_menu = self.menuBar().addMenu('&File')
        self.file_menu.addAction(self.quit_action)

        self.help_menu = self.menuBar().addMenu('&Help')

    def create_statusbar(self):
        """"""
        self.statusbar_label = QtWidgets.QLabel('')
        self.statusBar().showMessage('Ready')
        self.statusBar().addPermanentWidget(self.statusbar_label)

    def create_toolbar(self):
        """"""
        self.toolbar = self.addToolBar('Production')
        self.toolbar.addWidget(QtWidgets.QLabel("Production:  "))
        #self.productionToolBar.addWidget(self.productionComboBox)

    def quit(self):
        """"""
        QtCore.QCoreApplication.quit()


# Open Launcher window.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


