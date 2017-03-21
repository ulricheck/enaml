#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from . import QT_API 

from qtpy import PYQT5, PYQT4, PYSIDE
from qtpy.QtCore import *


if PYQT4 or PYQT5:
    QDateTime.toPython = QDateTime.__dict__['toPyDateTime']
    QDate.toPython = QDate.__dict__['toPyDate']
    QTime.toPython = QTime.__dict__['toPyTime']
    #__version_info__ = tuple(map(int, QT_VERSION_STR.split('.')))
    # Remove the input hook or pdb.set_trace() will infinitely recurse
    pyqtRemoveInputHook()
