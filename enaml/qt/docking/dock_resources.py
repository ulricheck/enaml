from enaml.qt import PYQT5

if PYQT5:
    from .dock_resources_qt5 import *
else:
    from .dock_resources_qt4 import *
