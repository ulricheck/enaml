#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from . import QT_API

from qtpy import PYQT5, PYQT4, PYSIDE, PythonQtError

# currently not wrapped in qtpy - Issue17 on github opened
# from qtpy.QtOpenGL import *

if PYQT5:
    from PyQt5.QtOpenGL import *
elif PYQT4:
    from PyQt4.QtOpenGL import *
elif PYSIDE:
    from PySide.QtOpenGL import *
else:
    raise PythonQtError('No Qt bindings could be found')
