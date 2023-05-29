def clear_qt_layout(layout):
    """
    - Remove all items/widgets from a Qt layout.

    - Parameters:
        - layout: The Qt layout to be cleared.
    """
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.deleteLater()
        else:
            clear_qt_layout(item.layout())