"""
Table of contents view for one collection
"""

from PyQt5.QtCore import (Qt, QAbstractListModel, QModelIndex, QSize,
                          QRectF, QRect, QPoint, )
from PyQt5.QtGui import (QPainter, QPalette, QPen, QTextOption)
from PyQt5.QtWidgets import QListView, QStyledItemDelegate, QStyle


def draw_album_icon(painter, x, y, h):
    r = h // 2
    center_x, center_y = x + r, y + r
    circle_center = QPoint(center_x, center_y)
    pen = painter.pen()
    pen.setCapStyle(Qt.RoundCap)
    pen.setWidth(2)
    painter.setPen(pen)
    r = r - 3  # margin
    r_dis = r // 4
    r_list = (r, r - 3 * r_dis, 2)
    for radius in r_list:
        painter.drawEllipse(circle_center, radius, radius)

    arc_list = [
        (r - r_dis, 16, 60),      # outer arc
        (r - r_dis * 2, 20, 50),  # inner arc
    ]
    for arc_r, start_angle, span in arc_list:
        topleft = QPoint(center_x - arc_r, center_y - arc_r)
        bottomright = QPoint(center_x + arc_r, center_y + arc_r)
        painter.drawArc(QRect(topleft, bottomright), 16 * start_angle, 16 * span)
        painter.drawArc(QRect(topleft, bottomright), 16 * (start_angle + 180), 16 * span)


class CollectionTOCModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.items = list(['理性与感性', '单身日志（Live）', '叶慧美', '晴日共剪窗'])

    def rowCount(self, _=QModelIndex()):
        return len(self.items)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == Qt.DisplayRole:
            return self.items[row]
        return None


class CollectionTOCDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def paint(self, painter, option, index):
        # refer to pixelator.py
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)

        text_pen = QPen(option.palette.color(QPalette.Text))
        hl_text_pen = QPen(option.palette.color(QPalette.HighlightedText))
        if option.state & QStyle.State_Selected:
            painter.setPen(hl_text_pen)
        else:
            painter.setPen(text_pen)

        # draw circle
        icon_margin_left = 3
        topleft = option.rect.topLeft()
        x, y = topleft.x() + icon_margin_left, topleft.y()
        h = option.rect.height()
        draw_album_icon(painter, x, y, h)

        text = index.data(Qt.DisplayRole)
        text_margin_left = h // 4
        topleft = QPoint(x + option.rect.height() + text_margin_left, y)
        painter.drawText(QRect(topleft, option.rect.bottomRight()), Qt.AlignVCenter, text)
        painter.restore()

    def sizeHint(self, option, index):
        if index.isValid():
            return QSize(100, 40)
        return super().sizeHint(option, index)


class CollectionTOCView(QListView):
    def __init__(self, app, parent=None):
        super().__init__(parent=parent)
        self._app = app

        delegate = CollectionTOCDelegate(self)
        self.setItemDelegate(delegate)
        if self._app is not None:
            model = CollectionTOCModel(self)
            self.setModel(model)

    def sizeHint(self):
        size = super().sizeHint()
        return QSize(50, size.height())



if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    view = CollectionTOCView(None)
    model = CollectionTOCModel(view)
    view.setModel(model)
    view.show()
    app.exec()
