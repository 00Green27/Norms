from PySide import QtGui

def getIcon(name):
    icon = QtGui.QIcon()
    return icon.addPixmap(QtGui.QPixmap("resources/images/%s.png" % name), QtGui.QIcon.Normal, QtGui.QIcon.Off)