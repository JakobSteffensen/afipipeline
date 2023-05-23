# ----------------------------------------------------------------------------------------------------------------------
# file       : afilm.core.ui
# created    : 23/05/2023
# email      : js@anim.dk
#
# UI utility functions.
# ----------------------------------------------------------------------------------------------------------------------

import webbrowser
from PySide2 import QtGui
from PySide2 import QtWidgets


def center_on_screen(widget):
    """"""
    screen = QtWidgets.QDesktopWidget().screenGeometry()
    size = widget.geometry()
    widget.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


def help(topic=None):
    """ Open a webbrowser on the current help topic."""
    webbrowser.open('https://anim.dk/')