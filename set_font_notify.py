#
# Binary Ninja - Header Font Normalizer
#

from binaryninja import PluginCommand
from binaryninjaui import UIActionHandler, UIAction, Menu, UIActionContext

from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

def FontSizeBugfix(context: UIActionContext):

    all_widgets = QApplication.allWidgets()

    reference_size = 0

    for widget in all_widgets:
        # fix font chaos
        cur_widget = widget.font()

        current_pt_size = cur_widget.pointSize()

        if(not reference_size):
            reference_size = current_pt_size

        if(reference_size < current_pt_size):
            cur_widget.setPointSize(reference_size)
            widget.setFont(cur_widget)

UIAction.registerAction("Font Fix Enabled")
UIActionHandler.globalActions().bindAction("Font Fix Enabled", UIAction(lambda context: None, FontSizeBugfix))
Menu.mainMenu("Plugins").addAction("Font Fix Enabled", "", 0)