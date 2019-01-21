# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog1.ui'
#
# Created: Mon Aug 20 21:15:36 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from datetime import datetime
from PySide.QtGui import QDialog
from database import DbHandler
import util

class AddDialog(QDialog):
    def __init__(self, dept_id, mainWindow):
        QDialog.__init__(self)
        self.mainWindow = mainWindow
        self.dept_id = dept_id
        self.db = DbHandler('norm.db')
        self.db.open()
        self.hardware_list = self.db.getHardware()

    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.closeEvent = self.closeEvent
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.hardwareComboBox = QtGui.QComboBox(Dialog)
        self.hardwareComboBox.setObjectName("hardwareComboBox")
        self.hardwareComboBox.addItems([hardware[1] for hardware in self.hardware_list])
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.hardwareComboBox)

        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.numberLineEdit = QtGui.QLineEdit(Dialog)
        self.numberLineEdit.setObjectName("numberLineEdit")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.numberLineEdit)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.nameLineEdit = QtGui.QLineEdit(Dialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.nameLineEdit)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.invNumLineEdit = QtGui.QLineEdit(Dialog)
        self.invNumLineEdit.setObjectName("invNumLineEdit")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.invNumLineEdit)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.yearSpinBox = QtGui.QSpinBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearSpinBox.sizePolicy().hasHeightForWidth())
        self.yearSpinBox.setSizePolicy(sizePolicy)
        self.yearSpinBox.setMinimum(2000)
        self.yearSpinBox.setMaximum(2099)
        self.yearSpinBox.setValue(datetime.now().year)
        self.yearSpinBox.setObjectName("yearSpinBox")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.yearSpinBox)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.costLineEdit = QtGui.QLineEdit(Dialog)
        self.costLineEdit.setObjectName("costLineEdit")
        self.horizontalLayout.addWidget(self.costLineEdit)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.formLayout_2.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout)

        self.amountSpinBox = QtGui.QSpinBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amountSpinBox.sizePolicy().hasHeightForWidth())
        self.amountSpinBox.setSizePolicy(sizePolicy)
        self.amountSpinBox.setProperty("value", 1)
        self.amountSpinBox.setObjectName("amountSpinBox")
        self.amountSpinBox.setMinimum(1)
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.amountSpinBox)

        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        #self.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText(u"&Добавить")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def accept(self):
        if len(self.nameLineEdit.text()) == 0:
            QtGui.QMessageBox.information(self.dialog, u"Нормы обеспеченности",
                u"Необходимо указать наименование обурудования.",
                QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return

        #number, name, inventory_number, year, cost, amount, department_id, hardware_id
        self.db.insert_equipment([
            self.numberLineEdit.text(),
            self.nameLineEdit.text(),
            self.invNumLineEdit.text(),
            self.yearSpinBox.text(),
            self.costLineEdit.text(),
            self.amountSpinBox.text(),
            self.dept_id,
            util.get_id_by_name(self.hardware_list, self.hardwareComboBox.currentText())
        ])
        self.db.commit()
        self.mainWindow.setTable()
        self.dialog.accept()

    def closeEvent(self, event):
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Добавить оборудование", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Порядковый номер:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Наименование:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Номенклатурный/инвентарный номер:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Год выпуска:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Цена:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Количество:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "руб.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Тип оборудования:", None, QtGui.QApplication.UnicodeUTF8))

