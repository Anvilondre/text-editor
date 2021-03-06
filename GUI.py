# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import os
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_text = TextEdit(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(20, 70, 801, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main_text.setFont(font)
        self.main_text.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.main_text.setObjectName("main_text")
        self.font_label = QtWidgets.QLabel(self.centralwidget)
        self.font_label.setGeometry(QtCore.QRect(340, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.font_label.setFont(font)
        self.font_label.setObjectName("font_label")
        self.font_size_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.font_size_spinBox.setGeometry(QtCore.QRect(580, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_size_spinBox.setFont(font)
        self.font_size_spinBox.setMinimum(5)
        self.font_size_spinBox.setMaximum(100)
        self.font_size_spinBox.setProperty("value", 12)
        self.font_size_spinBox.setObjectName("font_size_spinBox")
        self.bold_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bold_checkBox.setGeometry(QtCore.QRect(40, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bold_checkBox.setFont(font)
        self.bold_checkBox.setObjectName("bold_checkBox")
        self.italic_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.italic_checkBox.setGeometry(QtCore.QRect(120, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.italic_checkBox.setFont(font)
        self.italic_checkBox.setObjectName("italic_checkBox")
        self.underline_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.underline_checkBox.setGeometry(QtCore.QRect(200, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.underline_checkBox.setFont(font)
        self.underline_checkBox.setObjectName("underline_checkBox")
        self.select_font_box = QtWidgets.QFontComboBox(self.centralwidget)
        self.select_font_box.setGeometry(QtCore.QRect(400, 20, 171, 31))
        self.select_font_box.setObjectName("select_font_box")
        self.color_change_button = QtWidgets.QToolButton(self.centralwidget)
        self.color_change_button.setGeometry(QtCore.QRect(670, 10, 111, 51))
        self.color_change_button.setText("")
        self.color_change_button.setObjectName("color_change_button")
        self.color_change_button.setStyleSheet("background-color: black")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAllignment = QtWidgets.QMenu(self.menubar)
        self.menuAllignment.setObjectName("menuAllignment")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_open = QtWidgets.QAction(MainWindow)
        self.menu_open.setObjectName("menu_open")
        self.menu_save = QtWidgets.QAction(MainWindow)
        self.menu_save.setObjectName("menu_save")
        self.left_alignment = QtWidgets.QAction(MainWindow)
        self.left_alignment.setObjectName("left_alignment")
        self.right_alignment = QtWidgets.QAction(MainWindow)
        self.right_alignment.setObjectName("right_alignment")
        self.center_alignment = QtWidgets.QAction(MainWindow)
        self.center_alignment.setObjectName("center_alignment")
        self.justify_alignment = QtWidgets.QAction(MainWindow)
        self.justify_alignment.setObjectName("justify_alignment")
        self.menu_print = QtWidgets.QAction(MainWindow)
        self.menu_print.setObjectName("menu_print")
        self.menu_print_preview = QtWidgets.QAction(MainWindow)
        self.menu_print_preview.setObjectName("menu_print_preview")
        self.menu_export_pdf = QtWidgets.QAction(MainWindow)
        self.menu_export_pdf.setObjectName("menu_export_pdf")
        self.menuFile.addAction(self.menu_open)
        self.menuFile.addAction(self.menu_save)
        self.menuFile.addAction(self.menu_print)
        self.menuFile.addAction(self.menu_print_preview)
        self.menuFile.addAction(self.menu_export_pdf)
        self.menuAllignment.addAction(self.left_alignment)
        self.menuAllignment.addAction(self.right_alignment)
        self.menuAllignment.addAction(self.center_alignment)
        self.menuAllignment.addAction(self.justify_alignment)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAllignment.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_text.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.font_label.setText(_translate("MainWindow", "Font:"))
        self.bold_checkBox.setText(_translate("MainWindow", "Bold"))
        self.italic_checkBox.setText(_translate("MainWindow", "Italic"))
        self.underline_checkBox.setText(_translate("MainWindow", "Underline"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAllignment.setTitle(_translate("MainWindow", "Alignment"))
        self.menu_open.setText(_translate("MainWindow", "Open"))
        self.menu_save.setText(_translate("MainWindow", "Save"))
        self.left_alignment.setText(_translate("MainWindow", "Left"))
        self.right_alignment.setText(_translate("MainWindow", "Right"))
        self.center_alignment.setText(_translate("MainWindow", "Center"))
        self.justify_alignment.setText(_translate("MainWindow", "Justify"))
        self.menu_print.setText(_translate("MainWindow", "Print"))
        self.menu_print_preview.setText(_translate("MainWindow", "Print Preview"))
        self.menu_export_pdf.setText(_translate("MainWindow", "Export to PDF"))


class TextEdit(QtWidgets.QTextEdit):

    def canInsertFromMimeData(self, source):

        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):

        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():

            for u in source.urls():
                file_ext = os.path.splitext(str(u.toLocalFile()))[1].lower()
                if u.isLocalFile() and file_ext in ['.jpg', '.png', '.bmp']:
                    image = QtGui.QImage(u.toLocalFile())
                    document.addResource(QtGui.QTextDocument.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                else:
                    break
            else:
                return

        elif source.hasImage():
            image = source.imageData()
            cur_uuid = uuid.uuid4().hex
            document.addResource(QtWidgets.QTextDocument.ImageResource, cur_uuid, image)
            cursor.insertImage(cur_uuid)
            return

        super(TextEdit, self).insertFromMimeData(source)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
