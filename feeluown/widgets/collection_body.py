from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QSizePolicy, QLabel, QVBoxLayout,\
    QHBoxLayout

from feeluown.widgets.meta import MetaWidget


class CollectionToolbar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def songs_mode(self):
        pass

    def artists_mode(self):
        pass


class CollectionBody(QFrame):
    def __init__(self, app, parent=None):
        super().__init__(parent=parent)
        self._app = app

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.meta_widget = MetaWidget(self)

        self._setup_ui()

    def _setup_ui(self):
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
