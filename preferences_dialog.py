# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from PySide.QtGui import QInputDialog, QDialog
from database import DbHandler
import settings

class PreferencesDialog(QDialog):
    def __init__(self, depts):
        QDialog.__init__(self)
        self.depts = depts
        self.removedDepts = []
        self.db = DbHandler('norm.db')
        self.db.open()
        self.depts = self.db.getDepts()
        self.nextId = self.db.nextDeptId()

    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 380)
        Dialog.closeEvent = self.closeEvent
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        #        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        #        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        #        sizePolicy.setHorizontalStretch(0)
        #        sizePolicy.setVerticalStretch(0)
        #        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        #        self.groupBox_2.setSizePolicy(sizePolicy)
        #        self.groupBox_2.setObjectName("groupBox_2")
        #        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        #        self.gridLayout_5.setObjectName("gridLayout_5")
        #        self.dbLabel = QtGui.QLabel(self.groupBox_2)
        #        self.dbLabel.setObjectName("dbLabel")
        #        self.gridLayout_5.addWidget(self.dbLabel, 0, 0, 1, 1)
        #        self.dbLineEdit = QtGui.QLineEdit(self.groupBox_2)
        #        self.dbLineEdit.setObjectName("dbLineEdit")
        #        self.gridLayout_5.addWidget(self.dbLineEdit, 0, 1, 1, 1)
        #        self.dbPushButton = QtGui.QPushButton(self.groupBox_2)
        #        self.dbPushButton.setObjectName("dbPushButton")
        #        self.gridLayout_5.addWidget(self.dbPushButton, 0, 2, 1, 1)
        #        self.rdbLabel = QtGui.QLabel(self.groupBox_2)
        #        self.rdbLabel.setObjectName("rdbLabel")
        #        self.gridLayout_5.addWidget(self.rdbLabel, 1, 0, 1, 1)
        #        self.rdbLineEdit = QtGui.QLineEdit(self.groupBox_2)
        #        self.rdbLineEdit.setObjectName("rdbLineEdit")
        #        self.gridLayout_5.addWidget(self.rdbLineEdit, 1, 1, 1, 1)
        #        self.rdbPushButton = QtGui.QPushButton(self.groupBox_2)
        #        self.rdbPushButton.setObjectName("rdbPushButton")
        #        self.gridLayout_5.addWidget(self.rdbPushButton, 1, 2, 1, 1)
        #        self.templLabel = QtGui.QLabel(self.groupBox_2)
        #        self.templLabel.setObjectName("templLabel")
        #        self.gridLayout_5.addWidget(self.templLabel, 2, 0, 1, 1)
        #        self.templLineEdit = QtGui.QLineEdit(self.groupBox_2)
        #        self.templLineEdit.setObjectName("templLineEdit")
        #        self.gridLayout_5.addWidget(self.templLineEdit, 2, 1, 1, 1)
        #        self.templPushButton = QtGui.QPushButton(self.groupBox_2)
        #        self.templPushButton.setObjectName("templPushButton")
        #        self.gridLayout_5.addWidget(self.templPushButton, 2, 2, 1, 1)
        #        self.defaultLabel = QtGui.QLabel(self.groupBox_2)
        #        self.defaultLabel.setObjectName("defaultLabel")
        #        self.gridLayout_5.addWidget(self.defaultLabel, 3, 0, 1, 1)
        #        self.reportsLineEdit = QtGui.QLineEdit(self.groupBox_2)
        #        self.reportsLineEdit.setObjectName("reportsLineEdit")
        #        self.gridLayout_5.addWidget(self.reportsLineEdit, 3, 1, 1, 1)
        #        self.defaultPushButton = QtGui.QPushButton(self.groupBox_2)
        #        self.defaultPushButton.setObjectName("defaultPushButton")
        #        self.gridLayout_5.addWidget(self.defaultPushButton, 3, 2, 1, 1)
        #        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.yearSpinBox = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearSpinBox.sizePolicy().hasHeightForWidth())
        self.yearSpinBox.setSizePolicy(sizePolicy)
        self.yearSpinBox.setMinimum(2010)
        self.yearSpinBox.setMaximum(2099)
        self.yearSpinBox.setObjectName("yearSpinBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.yearSpinBox)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 142, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setObjectName("hardwareComboBox")
        self.comboBox.addItems([dept[1] for dept in self.depts])
        self.comboBox.activated[str].connect(self.setNormsTable)

        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtGui.QPushButton(self.tab_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.addButton.setIcon(icon)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.deleteButton = QtGui.QPushButton(self.tab_4)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_7.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.deptTable = QtGui.QTableWidget(self.tab_4)
        self.deptTable.setObjectName("deptTable")
        self.deptTable.setColumnCount(0)
        self.deptTable.setRowCount(0)
        self.deptTable.verticalHeader().setVisible(False)
        self.deptTable.horizontalHeader().setHighlightSections(False)
        self.deptTable.setAlternatingRowColors(True)
        self.deptTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.deptTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.gridLayout_7.addWidget(self.deptTable, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.normsTable = QtGui.QTableWidget(self.tab)
        self.normsTable.setObjectName("normsTable")
        self.normsTable.setColumnCount(0)
        self.normsTable.setRowCount(0)
        self.normsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.normsTable.setAlternatingRowColors(True)
        self.gridLayout_2.addWidget(self.normsTable, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.hardwareTable = QtGui.QTableWidget(self.tab_2)
        self.hardwareTable.setObjectName("hardwareTable")
        self.hardwareTable.setColumnCount(0)
        self.hardwareTable.setRowCount(0)
        self.hardwareTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.hardwareTable.setAlternatingRowColors(True)
        self.gridLayout_3.addWidget(self.hardwareTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.setDeptsTable()
        self.setHardwareTable()
        self.setNormsTable()
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.loadSettings()
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.addButton.clicked.connect(self.addDept)
        self.deleteButton.clicked.connect(self.deleteDept)
        self.deptTable.cellChanged.connect(self.updateDept)

    def addDept(self):
        text, ok = QInputDialog.getText(self.dialog, u"Нормы обеспеченности",
            u"Введите название кафедры:", QtGui.QLineEdit.Normal,
            None, QtCore.Qt.WindowSystemMenuHint)
        if ok and text:
            self.depts.append((self.nextId, text))
            self.nextId += 1
            self.comboBox.clear()
            self.comboBox.addItems([dept[1] for dept in self.depts])
            self.setDeptsTable()

    def deleteDept(self):
        self.removedDepts.append(self.depts[self.deptTable.currentRow()])
        self.depts.remove(self.depts[self.deptTable.currentRow()])
        self.comboBox.clear()
        self.comboBox.addItems([dept[1] for dept in self.depts])
        self.setDeptsTable()

    def updateDept(self):
        if self.deptTable.currentItem() is not  None:
            self.depts[self.deptTable.currentRow()][1] = self.deptTable.currentItem().text()
            self.comboBox.clear()
            self.comboBox.addItems([dept[1] for dept in self.depts])


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(u"Настройки")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), u"Общие")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), u"Кафедры")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), u"Нормы обеспеченности")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), u"Ооборудование")
        self.label.setText(u"Кафедра")
        self.groupBox.setTitle(u"Запуск")
        self.checkBox.setText(u"Открывать отчет после сохранения")
        #        self.groupBox_2.setTitle(u"Расположение")
        #        self.dbLabel.setText(u"База данных:")
        #        self.dbPushButton.setText(u"Обзор...")
        #        self.rdbLabel.setText(u"Резервные копии базы:")
        #        self.rdbPushButton.setText(u"Обзор...")
        #        self.templLabel.setText(u"Шаблоны:")
        #        self.templPushButton.setText(u"Обзор...")
        #        self.defaultLabel.setText(u"Отчеты:")
        #        self.defaultPushButton.setText(u"Обзор...")
        self.groupBox_3.setTitle(u"Разное")
        self.label_2.setText(u"Год списания:")
        self.addButton.setText(u"Добавить")
        self.deleteButton.setText(u"Удалить")

    #todo загрузка IS_OPEN_REPORT отрабатывает неверно из-за приведения к bool
    def loadSettings(self):
        self.checkBox.setChecked(bool(settings.IS_OPEN_REPORT))
        #        self.dbLineEdit.setText(settings.DATABASE_PATH)
        #        self.rdbLineEdit.setText(settings.BACKUP_PATH)
        #        self.templLineEdit.setText(settings.TEMPLATES_PATH)
        #        self.reportsLineEdit.setText(settings.REPORT_PATH)
        self.yearSpinBox.setValue(settings.YEAR)


    def setDeptsList(self):
        for dept in self.depts:
            self.comboBox.addItem(dept[1])

    def accept(self):
        self.saveSettings()
        self.saveDepts()
        self.saveNorms()
        self.saveHardware()
        self.db.commit()
        self.db.close()
        self.dialog.accept()

    def saveSettings(self):
        settings.IS_OPEN_REPORT = self.checkBox.checkState()
        #        settings.DATABASE_PATH = self.dbLineEdit.text()
        #        settings.BACKUP_PATH = self.rdbLineEdit.text()
        #        settings.TEMPLATES_PATH = self.templLineEdit.text()
        #        settings.REPORT_PATH = self.reportsLineEdit.text()
        settings.YEAR = self.yearSpinBox.value()

    def saveDepts(self):
        depts = []
        for id, name in self.depts:
            depts.append((id, name))
        self.db.insertDepts(depts)
        self.db.deleteDepts(self.removedDepts)
        self.db.commit()

    def saveNorms(self):
        dept_id = self.comboBox.currentIndex() + 1
        norms = []
        for i in xrange(0, 10):
            norms.append((
                dept_id,
                i + 1,
                int(self.normsTable.item(i, 0).text())
                ))
        self.db.insertNorms(norms)
        self.db.commit()

    def saveHardware(self):
        hard = []
        for i in xrange(0, 10):
            hard.append((
                int(self.hardwareTable.item(i, 0).text()),
                float(self.hardwareTable.item(i, 1).text()),
                i + 1
                ))
        self.db.insertHardware(hard)
        self.db.commit()

    def setDeptsTable(self):
        self.deptTable.setColumnCount(1)
        self.deptTable.setRowCount(len(self.depts))
        self.deptTable.horizontalHeader().setStretchLastSection(True)
        self.deptTable.setHorizontalHeaderLabels((u"Кафедра",))
        for row, name in enumerate(self.depts):
            table_item = QtGui.QTableWidgetItem(name[1])
            table_item.setText(unicode(name[1]))
            self.deptTable.setItem(row, 0, table_item)


    def setHardwareTable(self):
        names = self.db.getHardwareNames()
        hardware = self.db.getHardwareInfo()
        self.hardwareTable.setColumnCount(2)
        self.hardwareTable.setRowCount(len(hardware))
        self.hardwareTable.setHorizontalHeaderLabels((u"Срок службы", u"Цена, руб."))
        self.hardwareTable.setVerticalHeaderLabels([l[0] for l in names])
        for row, cols in enumerate(hardware):
            for col, text in enumerate(cols):
                if col == 1:

                    text = "%0.2f" % text if text is not None else 0
                table_item = QtGui.QTableWidgetItem(text)
                table_item.setText(unicode(text))
                self.hardwareTable.setItem(row, col, table_item)


    def setNormsTable(self):
        dept_id = self.comboBox.currentIndex() + 1
        names = self.db.getHardwareNames()
        norms = self.db.getNorms(dept_id)
        self.normsTable.setColumnCount(1)
        count = len(norms)
        if count == 0:
            count = 10
            for n in xrange(count):
                norms.append((10,))
        self.normsTable.setRowCount(count)
        self.normsTable.setHorizontalHeaderLabels((u"Норма",))
        self.normsTable.setVerticalHeaderLabels([l[0] for l in names])

        for row, cols in enumerate(norms):
            text = cols[0]
            table_item = QtGui.QTableWidgetItem(text)
            table_item.setText(unicode(text))
            self.normsTable.setItem(row, 0, table_item)

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = PreferencesDialog(0)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

