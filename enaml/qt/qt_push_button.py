#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from PyQt4.QtGui import QPushButton

from atom.api import Typed

from enaml.widgets.push_button import ProxyPushButton

from .qt_abstract_button import QtAbstractButton
from .qt_menu import QtMenu


class QtPushButton(QtAbstractButton, ProxyPushButton):
    """ A Qt implementation of an Enaml ProxyPushButton.

    """
    #: A reference to the widget created by the proxy.
    widget = Typed(QPushButton)

    #--------------------------------------------------------------------------
    # Initialization API
    #--------------------------------------------------------------------------
    def create_widget(self):
        """ Create the underlying QPushButton widget.

        """
        self.widget = QPushButton(self.parent_widget())

    def init_layout(self):
        """ Handle layout initialization for the push button.

        """
        super(QtPushButton, self).init_layout()
        self.widget.setMenu(self.menu())

    #--------------------------------------------------------------------------
    # Utility Methods
    #--------------------------------------------------------------------------
    def menu(self):
        """ Find and return the menu child for this widget.

        Returns
        -------
        result : QMenu or None
            The menu defined for this widget, or None if not defined.

        """
        m = self.declaration.menu
        if m is not None:
            return m.proxy.widget or None

    #--------------------------------------------------------------------------
    # Child Events
    #--------------------------------------------------------------------------
    # def child_removed(self, child):
    #     """ Handle the child removed event for a QtPushButton.

    #     """
    #     if isinstance(child, QtMenu):
    #         self.widget().setMenu(self.menu())

    # def child_added(self, child):
    #     """ Handle the child added event for a QtPushButton.

    #     """
    #     if isinstance(child, QtMenu):
    #         self.widget().setMenu(self.menu())