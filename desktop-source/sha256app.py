__author__ = 'sashgorokhov'

try:
    from PySide import QtGui, QtCore
except ImportError:
    with open('error.txt', 'w') as f:
        f.write('PySide import error')
    exit(-1)

import sys
from mainform import MainForm

app = QtGui.QApplication(sys.argv[1:])

form = MainForm()
form.show()

app.exec_()