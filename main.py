import sys

from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QTableView,
    QFileSystemModel,
    QStyledItemDelegate,
    QAbstractItemView
)
from pyqt.helpers import UiBase


class TableModel(QAbstractTableModel):
    def columnCount(self, index):
        return 4

    def rowCount(self, index):
        return 4

    def data(self, index, role):
        if role == Qt.DisplayRole: 
            return str((index.column(), index.row()))
        else:
            return None


class HighlightingRowsTable(QTableView, UiBase):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setup_ui()
        self.setModel(TableModel())
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    def mouseMoveEvent(self, event):
        index = self.indexAt(event.pos())
        self.selectRow(index.row())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = TableModel()
    hrt = HighlightingRowsTable()
    hrt.setModel(model)
    hrt.show()
    app.exec_()
