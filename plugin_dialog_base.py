# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WtyczkaDialogBase(object):
    def setupUi(self, WtyczkaDialogBase):
        WtyczkaDialogBase.setObjectName("WtyczkaDialogBase")
        WtyczkaDialogBase.resize(400, 585)
        self.button_box_ok_anuluj = QtWidgets.QDialogButtonBox(WtyczkaDialogBase)
        self.button_box_ok_anuluj.setGeometry(QtCore.QRect(20, 550, 341, 32))
        self.button_box_ok_anuluj.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_ok_anuluj.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box_ok_anuluj.setObjectName("button_box_ok_anuluj")
        self.mMapLayerComboBox_wybor_warstwy = QgsMapLayerComboBox(WtyczkaDialogBase)
        self.mMapLayerComboBox_wybor_warstwy.setGeometry(QtCore.QRect(60, 60, 271, 27))
        self.mMapLayerComboBox_wybor_warstwy.setObjectName("mMapLayerComboBox_wybor_warstwy")
        self.pushButton_obl_odleglosc = QtWidgets.QPushButton(WtyczkaDialogBase)
        self.pushButton_obl_odleglosc.setGeometry(QtCore.QRect(60, 100, 161, 28))
        self.pushButton_obl_odleglosc.setObjectName("pushButton_obl_odleglosc")
        self.pushButton_obl_pole = QtWidgets.QPushButton(WtyczkaDialogBase)
        self.pushButton_obl_pole.setGeometry(QtCore.QRect(60, 130, 161, 28))
        self.pushButton_obl_pole.setObjectName("pushButton_obl_pole")
        self.label_info_dol = QtWidgets.QLabel(WtyczkaDialogBase)
        self.label_info_dol.setGeometry(QtCore.QRect(60, 170, 251, 21))
        self.label_info_dol.setObjectName("label_info_dol")
        self.textBrowser_info_zwrotne = QtWidgets.QTextBrowser(WtyczkaDialogBase)
        self.textBrowser_info_zwrotne.setGeometry(QtCore.QRect(60, 190, 271, 311))
        self.textBrowser_info_zwrotne.setObjectName("textBrowser_info_zwrotne")
        self.label_info_gora = QtWidgets.QLabel(WtyczkaDialogBase)
        self.label_info_gora.setGeometry(QtCore.QRect(60, 40, 251, 20))
        self.label_info_gora.setObjectName("label_info_gora")

        self.retranslateUi(WtyczkaDialogBase)
        self.button_box_ok_anuluj.accepted.connect(WtyczkaDialogBase.accept) # type: ignore
        self.button_box_ok_anuluj.rejected.connect(WtyczkaDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WtyczkaDialogBase)

    def retranslateUi(self, WtyczkaDialogBase):
        _translate = QtCore.QCoreApplication.translate
        WtyczkaDialogBase.setWindowTitle(_translate("WtyczkaDialogBase", "Wtyczka Projekt 2 INF"))
        self.pushButton_obl_odleglosc.setText(_translate("WtyczkaDialogBase", "Oblicz odległość"))
        self.pushButton_obl_pole.setText(_translate("WtyczkaDialogBase", "Oblicz pole powierzchni"))
        self.label_info_dol.setText(_translate("WtyczkaDialogBase", "Informacja zwrotna programu:"))
        self.label_info_gora.setText(_translate("WtyczkaDialogBase", "Wybierz warswę:"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WtyczkaDialogBase = QtWidgets.QDialog()
    ui = Ui_WtyczkaDialogBase()
    ui.setupUi(WtyczkaDialogBase)
    WtyczkaDialogBase.show()
    sys.exit(app.exec_())
