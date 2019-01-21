# -*- coding: utf-8 -*-
from datetime import datetime

import os
import platform

from PySide import QtCore, QtGui
import PySide
import traceback
from PySide.QtGui import QMessageBox, QApplication
from database import DbHandler
import import_manager
from report_manager import ReporterManager
import settings
import gui_utils

class MainWindow(object):
    def __init__(self):
        self.db = DbHandler(settings.DATABASE_FILENAME)
        self.db.open()
        self.depts = self.db.getDepts()
        self.hardware = self.db.getHardwareNames()

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("Window")
        MainWindow.resize(930, 480)
        MainWindow.closeEvent = self.closeEvent
        MainWindow.setWindowIcon(gui_utils.get_icon("icon"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.label.setText(u"Кафедра")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.deptComboBox = QtGui.QComboBox(self.centralWidget)
        self.deptComboBox.setObjectName("deptComboBox")
        self.deptComboBox.activated[str].connect(self.setTable)
        self.deptComboBox.addItems([dept[1] for dept in self.depts])
        self.gridLayout.addWidget(self.deptComboBox, 0, 1, 1, 1)

        self.hardwareComboBox = QtGui.QComboBox(self.centralWidget)
        self.hardwareComboBox.setObjectName("hardwareComboBox")
        self.hardwareComboBox.activated[str].connect(self.setTable)
        self.hardwareComboBox.addItem(u"Все оборудование")
        self.hardwareComboBox.addItems([hard[0] for hard in self.hardware])
        self.gridLayout.addWidget(self.hardwareComboBox, 0, 2, 1, 1)

        self.table = QtGui.QTableWidget(self.centralWidget)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.verticalHeader().setVisible(False)
        #self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.resizeColumnsToContents()
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.handleHeaderMenu)

        self.gridLayout.addWidget(self.table, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralWidget)

        MainWindow.setWindowTitle(u"Норма обеспеченности")

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setWindowTitle("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.importAction = QtGui.QAction(u"Импорт", MainWindow, shortcut="Ctrl+Shift+I",
            triggered=self.importAction)
        self.importAction = self.createAction("importAction", u"Импорт", "import", "Ctrl+Shift+I", self.importFromFile)
        self.exportAction = self.createAction("exportAction", u"Экспорт", "export", "Ctrl+Shift+E", self.exportToFile)
        self.exitAction = self.createAction("exitAction", u"Выход", method=MainWindow.close)

        self.copyAction = self.createAction("copyAction", u"Копировать", "copy", "Ctrl+C", self.copyToClipboard)
        self.copyRowAction = self.createAction("copyRowAction", u"Копировать строку", "table_select_row", "Ctrl+Shift+C"
            , self.copyRowToClipboard)
        self.addEquipmentAction = self.createAction("addEquipmentAction", u"Добавить", "table_add",
            method=self.addEquipment)
        self.delEquipmentAction = self.createAction("delEquipmentAction", u"Удалить",
            method=self.delEquipment)
        self.removeAllAction = self.createAction("removeAllAction", u"Удалить оборудование кафедры",
            method=self.removeAll)

        self.configAction = self.createAction("configAction", u"Настройки...", "config", "Ctrl+,", self.config)

        self.globalTimesheeAction = self.createAction("globalTimesheeAction", u"Табель обеспеченности академии",
            method=self.getGlobalTimesheet)
        self.equipmentsAction = self.createAction("equipmentsAction", u"Материально-техническая база",
            method=self.getEquipments)
        self.backupAction = self.createAction("backupAction", u"Резервирование", "backup", method=self.backup)

        self.sqlSpyAction = self.createAction("sqlSpyAction", u"SQLiteSpy", method=self.runSQLiteSpy)
        self.vacuumAction = self.createAction("vacuumAction", u"Очистить БД", "refresh", method=self.vacuum)

        self.aboutAction = self.createAction("aboutAction", u"О программе...", method=self.about)

        self.searchAction = self.createAction("searchAction", u"Искать на Яндекс Маркете", method=self.search)

        self.fileMenu = self.createMenuItem("fileMenu", u"Файл", [
            self.importAction,
            self.exportAction,
            self.exitAction,
            self.createSeparator(),
            self.exitAction
        ])
        self.menubar.addAction(self.fileMenu.menuAction())

        self.editMenu = self.createMenuItem("editMenu", u"Правка", [
            self.copyAction,
            self.copyRowAction,
            self.createSeparator(),
            self.addEquipmentAction,
            self.delEquipmentAction,
            self.removeAllAction,
            self.createSeparator(),
            self.configAction

        ])
        self.menubar.addAction(self.editMenu.menuAction())

        self.reportMenu = self.createMenuItem("reportMenu", u"Отчеты", [
            self.globalTimesheeAction,
            self.equipmentsAction
        ])
        self.menubar.addAction(self.reportMenu.menuAction())

        self.toolsMenu = self.createMenuItem("toolsMenu", u"Инструменты", [
            self.vacuumAction,
            self.sqlSpyAction
        ])
        self.menubar.addAction(self.toolsMenu.menuAction())

        self.helpMenu = self.createMenuItem("helpMenu", u"Справка", [self.aboutAction])
        self.menubar.addAction(self.helpMenu.menuAction())

        self.toolBar.addActions([
            self.importAction,
            self.exportAction,
            self.addEquipmentAction,
            self.configAction,
            self.backupAction
        ])

        self.setTable()

    def createMenuItem(self, name, text, actions):
        menu = QtGui.QMenu(self.menubar)
        menu.setObjectName(name)
        menu.setTitle(text)
        menu.addActions(actions)
        return menu

    def createSeparator(self):
        action = QtGui.QAction(Window)
        action.setSeparator(True)
        return action

    def createAction(self, name, text, icon=None, shortcut=None, method=None):
        action = QtGui.QAction(Window)
        action.setIcon(gui_utils.get_icon(icon))
        action.setObjectName(name)
        action.setText(text)
        action.setShortcut(shortcut)
        action.triggered.connect(method)
        return action

    def runSQLiteSpy(self):
        from subprocess import call

        call(["./resources/SQLiteSpy/SQLiteSpy.exe", "norm.db"])

    def addEquipment(self):
        from add_dialog import AddDialog

        Dialog = QtGui.QDialog(Window)
        ui = AddDialog(self.deptComboBox.currentIndex() + 1, self)
        ui.setupUi(Dialog)
        Dialog.show()

    def delEquipment(self):
        if not self.table.currentItem() is None:
            reply = QtGui.QMessageBox.question(Window, u"Информация",
                u"Вы действительно хотите удалить <i>\"%s\"</i>?" % (unicode(self.equipment[self.table.currentIndex().row()][1])), QtGui.QMessageBox.Yes |
                                         QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                print self.equipment[self.table.currentIndex().row()][8]
                self.db.delete_hardware(self.equipment[self.table.currentIndex().row()][8])
                self.db.commit()

        self.setTable()

    def removeAll(self):
        dept_id = self.deptComboBox.currentIndex() + 1
        self.db.deleteEquipment(dept_id)
        self.db.commit()
        self.setTable()

    def exportToFile(self):
        #import uuid

        dept_id = self.deptComboBox.currentIndex() + 1
        timesheet = self.db.getTimesheet(dept_id)
        dept_name = self.db.getDeptName(dept_id)
        equipment = self.db.getEquipment(dept_id)
        report = ReporterManager("timesheet")
        report.set_department(dept_name)
        report.write_timesheet(timesheet)
        report.write_equipment(equipment)
        fileName, ok = QtGui.QFileDialog.getSaveFileName(Window, u"Сохранение табеля",
            os.path.join(QtCore.QDir.currentPath(), unicode(self.deptComboBox.currentText()) + ".xls"),
            u"Файлы Excel (*.xls)")
        if ok:
            self.save(report, fileName)

    def handleHeaderMenu(self, pos):
        menu = QtGui.QMenu()
        menu.addActions([
            self.copyAction,
            self.copyRowAction,
            self.addEquipmentAction,
            self.delEquipmentAction,
            self.removeAllAction,
            self.createSeparator(),
            self.importAction,
            self.exportAction,
            self.createSeparator(),
            self.searchAction])
        menu.exec_(QtGui.QCursor.pos())

    def search(self):
        import webbrowser

        list = self.table.currentItem().text().split(" ")
        str = " ".join(list[:-1])
        if len(str) != 0:
            webbrowser.open("http://market.yandex.ru/search.xml?text=%s" % str)

    def copyRowToClipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("\t".join([t.text() for t in self.table.selectedItems()]))

    def copyToClipboard(self):
        if not self.table.currentItem() is None:
            clipboard = QApplication.clipboard()
            clipboard.setText(self.table.currentItem().text())

    def vacuum(self):
        before = os.path.getsize(settings.DATABASE_FILENAME)
        self.db.vacuum()
        after = os.path.getsize(settings.DATABASE_FILENAME)
        clean = (before - after) / 1024

        QtGui.QMessageBox.question(Window, u"Информация",
            u"База данных была вычищена на %d Кб от ненужных данных.\n" % clean,
            QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def save(self, report, fileName):
        try:
            report.save(fileName)
        except:
            traceback.print_exc()
            QtGui.QMessageBox.critical(Window, u"Норма обеспеченности",
                u"Нет доступа на запись файла %s" % fileName)

        if settings.IS_OPEN_REPORT:
            #os.startfile(fileName)
            if os.name == "nt":
                os.startfile(fileName)
            elif os.name == "posix":
                os.system("xdg-open '%s'" % fileName.encode('utf-8'))


                #    def save(self, fileName):
                #        ok = True
                #        if os.path.exists(fileName):
                #            reply = QtGui.QMessageBox.question(Window, u"Подтвердить сохранение",
                #                u"%s уже существует.\nЗаменить?" % (fileName), QtGui.QMessageBox.Yes |
                #                                     QtGui.QMessageBox.No, QtGui.QMessageBox.No)
                #        if reply <> QtGui.QMessageBox.Yes:
                #            ok = False
                #
                #        if ok:
                #            report.save(fileName)

    def importFromFile(self):
        fileName, ok = QtGui.QFileDialog.getOpenFileName(Window, u"Импортировать опись", QtCore.QDir.currentPath(),
            u"Файлы Excel (*.xlsx)")

        if ok:
            dept_id = self.deptComboBox.currentIndex() + 1
            dept = self.deptComboBox.currentText()
            data = import_manager.load_from_file(fileName, dept_id)
            self.db.insertEquipments(data, dept_id)
            self.db.commit()
            self.setTable()

            QtGui.QMessageBox.question(Window, u"Импорт",
                u"<b>Кафедра {0}</b><br />Импортировано записей: {1}".format(dept.lower(), len(data)),
                QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)


    def closeEvent(self, event):
        self.db.close()
        event.accept()

    def setTable(self):
        text = self.deptComboBox.currentText()
        self.window.setWindowTitle(u"Кафедра %s - Норма обеспеченности" % (text[0].lower() + text[1:]))
        deptIndex = self.deptComboBox.currentIndex() + 1
        hardIndex = self.hardwareComboBox.currentIndex()
        if hardIndex > 0:
            self.equipment = self.db.getEquipmentByHardware((deptIndex, hardIndex))
        else:
            self.equipment = self.db.getEquipment(deptIndex)

        self.table.setColumnCount(6)
        self.table.setRowCount(len(self.equipment))

        self.table.setHorizontalHeaderLabels((
            u"№ п/п", u"Наименование", u"Номенклатурный или инвентарный номер", u"Год выпуска", u"Цена, руб.",
            u"Количество"))

        for row, cols in enumerate(self.equipment):
            for col, text in enumerate(cols):
                table_item = QtGui.QTableWidgetItem(text)
                if col == 4 and text != None:
                    text = "%0.2f" % text
                table_item.setText(unicode(text))
                self.table.setItem(row, col, table_item)

        self.table.resizeColumnsToContents()
        self.statusbar.showMessage(u"Количество строк: %d" % (len(self.equipment)))

    def config(self):
        import preferences_dialog

        Dialog = QtGui.QDialog(Window)
        ui = preferences_dialog.PreferencesDialog(self.depts)
        ui.setupUi(Dialog)
        Dialog.show()

    def getGlobalTimesheet(self):
        timesheet = self.db.getGlobalTimesheet()
        report = ReporterManager("global")
        report.set_department(0)
        report.write_timesheet(timesheet)
        fileName, ok = QtGui.QFileDialog.getSaveFileName(Window, u"Сохранение табеля",
            os.path.join(QtCore.QDir.currentPath(), u"Табель академии.xls"), u"Файлы Excel (*.xls)")
        if ok:
            self.save(report, fileName)

    def getEquipments(self):
        timesheet = self.db.getEquipments()
        report = ReporterManager("equipments")
        report.write_equipments(timesheet)
        fileName, ok = QtGui.QFileDialog.getSaveFileName(Window, u"Сохранение",
            os.path.join(QtCore.QDir.currentPath(), u"Материально-техническая база.xls"), u"Файлы Excel (*.xls)")
        if ok:
            self.save(report, fileName)

    def about(self):
        QMessageBox.about(Window, u"О программе...",
            u"""<b>Platform Details</b> v %s
        <p>Python %s -  PySide version %s - Qt version %s on %s
        <p>Copyright © %s Joe Bloggs.
        All rights reserved in accordance with<br/>
        GPL v2 or later
        <p>The program is provided AS IS with NO WARRANTY OF ANY KIND,
        INCLUDING THE WARRANTY OF DESIGN, MERCHANTABILITY AND
        FITNESS FOR A PARTICULAR PURPOSE.""" % (platform.__version__,
                                                platform.python_version(), PySide.__version__,
                                                PySide.QtCore.__version__,
                                                platform.system(), datetime.now().year))

    def backup(self):
        import shutil

        dt = datetime.now()
        dst = "norm-%s.db" % (dt.strftime('%Y%m%dialog%H%M%S'))
        if not os.path.exists("backup"):
            os.makedirs("backup")

        shutil.copy(settings.DATABASE_FILENAME, os.path.join("backup", dst))
        QMessageBox.question(Window, u"Резервное копирование",
            u"Резервное копирование базы данных завершено.\n %s" % (str(os.path.join("backup", dst))))

if __name__ == "__main__":
    import sys


    app = QtGui.QApplication(sys.argv)
    Window = QtGui.QMainWindow()
    ui = MainWindow()
    ui.setupUi(Window)
    Window.show()

    sys.exit(app.exec_())

