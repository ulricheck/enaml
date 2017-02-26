#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
import os


def prepare_pyqt():
    import sip
    sip.setapi('QDate', 2)
    sip.setapi('QDateTime', 2)
    sip.setapi('QString', 2)
    sip.setapi('QTextStream', 2)
    sip.setapi('QTime', 2)
    sip.setapi('QUrl', 2)
    sip.setapi('QVariant', 2)


from qtpy import PYQT5, PYQT4, PYSIDE
from qtpy import API as QT_API

if PYQT4:
    prepare_pyqt()
elif PYSIDE or PYQT5:
    pass
else:
    msg = "Invalid Qt API %r, valid values are: 'pyqt', 'pyqt4', 'pyqt5', or 'pyside'"
    raise ValueError(msg % QT_API)
