from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFrame, QHBoxLayout
from feeluown.widgets.table_container import TableContainer
from feeluown.widgets.collection_container import CollectionContainer

from fuocore import aio


class RightPanel(QFrame):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self._app = app

        self._layout = QHBoxLayout(self)
        self.table_container = TableContainer(self._app, self)
        self.collection_container = CollectionContainer(self._app, self)
        self.table_container.hide()
        self.collection_container.hide()
        self._layout.addWidget(self.table_container)
        self._layout.addWidget(self.collection_container)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

    def sizeHint(self):
        size = super().sizeHint()
        return QSize(760, size.height())

    def show_model(self, model):
        self.table_container.show()
        self.collection_container.hide()
        # TODO: use PreemptiveTask
        aio.create_task(self.table_container.show_model(model))

    def show_collection(self, coll):
        self.table_container.hide()
        self.collection_container.show()
        self.collection_container.show_collection(coll)
