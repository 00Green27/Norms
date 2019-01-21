from PySide import QtGui

def get_icon(name):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("resources/images/%s.png" % name), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    if icon is None:
        icon.addPixmap(QtGui.QPixmap("resources/images/%s.png" % "pixel"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon
