# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs\gui_fit.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(526, 664)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cbModel = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbModel.sizePolicy().hasHeightForWidth())
        self.cbModel.setSizePolicy(sizePolicy)
        self.cbModel.setObjectName("cbModel")
        self.horizontalLayout_3.addWidget(self.cbModel)
        self.btnPrintDiffEquations = QtWidgets.QPushButton(Dialog)
        self.btnPrintDiffEquations.setCheckable(False)
        self.btnPrintDiffEquations.setChecked(False)
        self.btnPrintDiffEquations.setAutoRepeat(False)
        self.btnPrintDiffEquations.setAutoDefault(False)
        self.btnPrintDiffEquations.setObjectName("btnPrintDiffEquations")
        self.horizontalLayout_3.addWidget(self.btnPrintDiffEquations)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.cbCustom = QtWidgets.QCheckBox(Dialog)
        self.cbCustom.setObjectName("cbCustom")
        self.verticalLayout.addWidget(self.cbCustom)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.cbMethod = QtWidgets.QComboBox(Dialog)
        self.cbMethod.setObjectName("cbMethod")
        self.verticalLayout.addWidget(self.cbMethod)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pteEquation = QtWidgets.QPlainTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteEquation.sizePolicy().hasHeightForWidth())
        self.pteEquation.setSizePolicy(sizePolicy)
        self.pteEquation.setMinimumSize(QtCore.QSize(0, 200))
        self.pteEquation.setMaximumSize(QtCore.QSize(16777215, 200))
        self.pteEquation.setPlainText("")
        self.pteEquation.setObjectName("pteEquation")
        self.verticalLayout.addWidget(self.pteEquation)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.leX0 = QtWidgets.QLineEdit(Dialog)
        self.leX0.setObjectName("leX0")
        self.horizontalLayout.addWidget(self.leX0)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.leX1 = QtWidgets.QLineEdit(Dialog)
        self.leX1.setObjectName("leX1")
        self.horizontalLayout.addWidget(self.leX1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.sbParamsCount = QtWidgets.QSpinBox(Dialog)
        self.sbParamsCount.setMinimum(1)
        self.sbParamsCount.setMaximum(10)
        self.sbParamsCount.setObjectName("sbParamsCount")
        self.horizontalLayout.addWidget(self.sbParamsCount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.cbUpdateInitValues = QtWidgets.QCheckBox(Dialog)
        self.cbUpdateInitValues.setObjectName("cbUpdateInitValues")
        self.verticalLayout.addWidget(self.cbUpdateInitValues)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnFit = QtWidgets.QPushButton(Dialog)
        self.btnFit.setCheckable(False)
        self.btnFit.setChecked(False)
        self.btnFit.setAutoRepeat(False)
        self.btnFit.setAutoDefault(False)
        self.btnFit.setObjectName("btnFit")
        self.horizontalLayout_2.addWidget(self.btnFit)
        self.btnPrintReport = QtWidgets.QPushButton(Dialog)
        self.btnPrintReport.setCheckable(False)
        self.btnPrintReport.setChecked(False)
        self.btnPrintReport.setAutoRepeat(False)
        self.btnPrintReport.setAutoDefault(False)
        self.btnPrintReport.setObjectName("btnPrintReport")
        self.horizontalLayout_2.addWidget(self.btnPrintReport)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setAutoDefault(False)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_2.addWidget(self.btnOK)
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setAutoDefault(False)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_2.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Model:"))
        self.btnPrintDiffEquations.setText(_translate("Dialog", "Print differential equations"))
        self.cbCustom.setText(_translate("Dialog", "Custom model (equation window will be editable)"))
        self.label_13.setText(_translate("Dialog", "Minimizing algorithm:"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">def func(x, *params):</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "Selected x range:"))
        self.label_11.setText(_translate("Dialog", "from"))
        self.label_12.setText(_translate("Dialog", "to"))
        self.label_9.setText(_translate("Dialog", "Params"))
        self.cbUpdateInitValues.setText(_translate("Dialog", "Update initial values when linear region move is finished"))
        self.label_7.setText(_translate("Dialog", "Fixed"))
        self.label_3.setText(_translate("Dialog", "Param"))
        self.label_8.setText(_translate("Dialog", "Error"))
        self.label_6.setText(_translate("Dialog", "Upper\n"
"bound"))
        self.label_4.setText(_translate("Dialog", "Lower\n"
"bound"))
        self.label_5.setText(_translate("Dialog", "<= Value <="))
        self.btnFit.setText(_translate("Dialog", "Fit"))
        self.btnPrintReport.setText(_translate("Dialog", "Print report"))
        self.btnOK.setText(_translate("Dialog", "Ok"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
