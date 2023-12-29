from PyQt6.QtGui import QColor

STATUS_COLORS = {
    "ok": QColor(0, 255, 0, 127),
    "nofile": QColor(255, 255, 0, 127),
    "notauth": QColor(255, 127, 0, 127),
    "banned": QColor(255, 0, 0, 127),
}


def get_status_from_color(color):
    for s, c in STATUS_COLORS.items():
        if c == color:
            return s
