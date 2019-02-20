import PySide2
from PySide2.QtGui import QColor, QPalette
from PySide2.QtCore import Qt, QObject, Slot
from PySide2.QtWidgets import QTreeView, QAction, QActionGroup, QMenu, QFileDialog, QApplication

import os


class ObjectTree(QTreeView):

    def __init__(self, parent=None):
        super(ObjectTree, self).__init__(parent)

        self.menu = QMenu(parent=self)

        self.create_context_menu()

    def create_context_menu(self):
        self.action_export_buffer = QAction("Export buffer", self)
        self.menu.addAction(self.action_export_buffer)

        #self.action_export_hex = QAction("Export as hex string", self)
        #self.menu.addAction(self.action_export_hex)

    def setModel(self, model: PySide2.QtCore.QAbstractItemModel):
        super(ObjectTree, self).setModel(model)
        self.expandAll()

    def mouseReleaseEvent(self, event: PySide2.QtGui.QMouseEvent):
        if event.button() == Qt.RightButton:
            index = self.indexAt(event.pos())
            if index.isValid():
                node = index.internalPointer()

                action = self.menu.exec_(self.mapToGlobal(event.pos()))

                if action == self.action_export_buffer:
                    file_path, _ = QFileDialog.getSaveFileName(self, "Save file")
                    file = open(file_path, "wb")
                    file.write(node.buffer)
                    file.close()
        else:
            super(ObjectTree, self).mouseReleaseEvent(event)
