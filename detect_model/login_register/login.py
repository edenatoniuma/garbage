# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(712, 448)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 12, 671, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.account_label = QtWidgets.QLabel(self.layoutWidget)
        self.account_label.setObjectName("account_label")
        self.verticalLayout.addWidget(self.account_label)
        self.account_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_edit.setObjectName("account_edit")
        self.verticalLayout.addWidget(self.account_edit)
        self.pws_label = QtWidgets.QLabel(self.layoutWidget)
        self.pws_label.setObjectName("pws_label")
        self.verticalLayout.addWidget(self.pws_label)
        self.pwd_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.pwd_edit.setObjectName("pwd_edit")
        self.verticalLayout.addWidget(self.pwd_edit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.text_blank = QtWidgets.QTextBrowser(self.layoutWidget)
        self.text_blank.setObjectName("text_blank")
        self.horizontalLayout.addWidget(self.text_blank)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.login_in_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.login_in_btn.setObjectName("login_in_btn")
        self.horizontalLayout_3.addWidget(self.login_in_btn)
        self.sign_up_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.sign_up_btn.setObjectName("sign_up_btn")
        self.horizontalLayout_3.addWidget(self.sign_up_btn)
        self.exit_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_3.addWidget(self.exit_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.account_label.setText(_translate("Form", "账号"))
        self.pws_label.setText(_translate("Form", "密码"))
        self.login_in_btn.setText(_translate("Form", "登录"))
        self.sign_up_btn.setText(_translate("Form", "注册"))
        self.exit_btn.setText(_translate("Form", "退出"))
