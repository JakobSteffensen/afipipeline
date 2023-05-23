# ----------------------------------------------------------------------------------------------------------------------
# file       : afilm.core.ui
# created    : 23/05/2023
# email      : js@anim.dk
#
# UI utility functions.
# ----------------------------------------------------------------------------------------------------------------------
from pathlib import Path
import webbrowser

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

import afilm.core.io
import afilm.core.pipeline


def apply_style(widget):
    """"""
    stylesheet_string = ''
    stylesheet_path = afilm.core.pipeline.pipeline_root() / 'resource/style/stylesheet.qss'

    # Open stylesheet and convert to string.
    with open(stylesheet_path, 'r') as stylesheet:
        for line in stylesheet:
            line.replace('\n', ' ')
            line.replace('\t', ' ')
            stylesheet_string = stylesheet_string+line

    # Apply stylesheet string if it is valid.
    if len(stylesheet_string):
        widget.setStyleSheet(stylesheet_string)


def create_combo_box(self, rebuild_function=None, index_changed_function=None):
    """"""
    combo_box = QtWidgets.QComboBox()
    combo_box.rebuild = rebuild_function
    combo_box.addItems(QtCore.QStringList(combox_box.rebuild()))

    if index_changed_function:
        combo_box.currentIndexChanged.connect(index_changed_function)

    return comboBox


def center_on_screen(widget):
    """"""
    screen = QtWidgets.QDesktopWidget().screenGeometry()
    size = widget.geometry()
    widget.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


def help(topic=None):
    """ Open a webbrowser on the current help topic."""
    webbrowser.open('https://anim.dk/')