from PyQt5.QtCore import Qt, QSize
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
        self.meta_widget = MetaWidget(CollectionToolbar(), self)

        self._setup_ui()

    def sizeHint(self):
        size = super().sizeHint()
        return QSize(300, size.height())

    def _setup_ui(self):
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self.meta_widget)
        self._layout.addStretch(0)
