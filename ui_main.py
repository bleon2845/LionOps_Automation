# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LionOps_Automation.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(656, 509)
        self.actionTELEFONICA = QAction(MainWindow)
        self.actionTELEFONICA.setObjectName(u"actionTELEFONICA")
        self.actionSAMSUNG = QAction(MainWindow)
        self.actionSAMSUNG.setObjectName(u"actionSAMSUNG")
        self.actionInbound = QAction(MainWindow)
        self.actionInbound.setObjectName(u"actionInbound")
        self.actionInbound_2 = QAction(MainWindow)
        self.actionInbound_2.setObjectName(u"actionInbound_2")
        self.actionOutbound = QAction(MainWindow)
        self.actionOutbound.setObjectName(u"actionOutbound")
        self.actionCheck_Materials = QAction(MainWindow)
        self.actionCheck_Materials.setObjectName(u"actionCheck_Materials")
        self.actionPrint_Docs_SAP = QAction(MainWindow)
        self.actionPrint_Docs_SAP.setObjectName(u"actionPrint_Docs_SAP")
        self.actionCheck_Materials_2 = QAction(MainWindow)
        self.actionCheck_Materials_2.setObjectName(u"actionCheck_Materials_2")
        self.actionSave_PDF_SAP = QAction(MainWindow)
        self.actionSave_PDF_SAP.setObjectName(u"actionSave_PDF_SAP")
        self.actionAudit_Materials = QAction(MainWindow)
        self.actionAudit_Materials.setObjectName(u"actionAudit_Materials")
        self.actionSave_PDF_SAP_2 = QAction(MainWindow)
        self.actionSave_PDF_SAP_2.setObjectName(u"actionSave_PDF_SAP_2")
        self.actionAudit_Materials_2 = QAction(MainWindow)
        self.actionAudit_Materials_2.setObjectName(u"actionAudit_Materials_2")
        self.actionPrint_PDF = QAction(MainWindow)
        self.actionPrint_PDF.setObjectName(u"actionPrint_PDF")
        self.actionCreate_Orders = QAction(MainWindow)
        self.actionCreate_Orders.setObjectName(u"actionCreate_Orders")
        self.actionOPERATION = QAction(MainWindow)
        self.actionOPERATION.setObjectName(u"actionOPERATION")
        self.actionAUTOMATION = QAction(MainWindow)
        self.actionAUTOMATION.setObjectName(u"actionAUTOMATION")
        self.actionREPORTS = QAction(MainWindow)
        self.actionREPORTS.setObjectName(u"actionREPORTS")
        self.actionLogin = QAction(MainWindow)
        self.actionLogin.setObjectName(u"actionLogin")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Pages = QStackedWidget(self.frame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_createorders = QWidget()
        self.page_createorders.setObjectName(u"page_createorders")
        self.verticalLayout_3 = QVBoxLayout(self.page_createorders)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CreateOrders = QLabel(self.page_createorders)
        self.CreateOrders.setObjectName(u"CreateOrders")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.CreateOrders.setFont(font)

        self.horizontalLayout.addWidget(self.CreateOrders)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Login = QLabel(self.page_createorders)
        self.Login.setObjectName(u"Login")

        self.horizontalLayout.addWidget(self.Login)

        self.user_create = QLineEdit(self.page_createorders)
        self.user_create.setObjectName(u"user_create")

        self.horizontalLayout.addWidget(self.user_create)

        self.pass_create = QLineEdit(self.page_createorders)
        self.pass_create.setObjectName(u"pass_create")

        self.horizontalLayout.addWidget(self.pass_create)

        self.btn_login_create = QPushButton(self.page_createorders)
        self.btn_login_create.setObjectName(u"btn_login_create")

        self.horizontalLayout.addWidget(self.btn_login_create)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_open = QPushButton(self.page_createorders)
        self.btn_open.setObjectName(u"btn_open")

        self.horizontalLayout_2.addWidget(self.btn_open)

        self.txt_filecreation = QLineEdit(self.page_createorders)
        self.txt_filecreation.setObjectName(u"txt_filecreation")

        self.horizontalLayout_2.addWidget(self.txt_filecreation)

        self.btn_creation = QPushButton(self.page_createorders)
        self.btn_creation.setObjectName(u"btn_creation")

        self.horizontalLayout_2.addWidget(self.btn_creation)

        self.btn_close = QPushButton(self.page_createorders)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tb_creation = QTableWidget(self.page_createorders)
        if (self.tb_creation.columnCount() < 12):
            self.tb_creation.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_creation.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tb_creation.setObjectName(u"tb_creation")

        self.verticalLayout_3.addWidget(self.tb_creation)

        self.Pages.addWidget(self.page_createorders)
        self.page_savepdf = QWidget()
        self.page_savepdf.setObjectName(u"page_savepdf")
        self.verticalLayout_2 = QVBoxLayout(self.page_savepdf)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SavePDF = QLabel(self.page_savepdf)
        self.SavePDF.setObjectName(u"SavePDF")
        self.SavePDF.setFont(font)

        self.horizontalLayout_3.addWidget(self.SavePDF)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.page_savepdf)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.user_save = QLineEdit(self.page_savepdf)
        self.user_save.setObjectName(u"user_save")

        self.horizontalLayout_3.addWidget(self.user_save)

        self.pass_save = QLineEdit(self.page_savepdf)
        self.pass_save.setObjectName(u"pass_save")

        self.horizontalLayout_3.addWidget(self.pass_save)

        self.btn_login_save = QPushButton(self.page_savepdf)
        self.btn_login_save.setObjectName(u"btn_login_save")

        self.horizontalLayout_3.addWidget(self.btn_login_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_openprint = QPushButton(self.page_savepdf)
        self.btn_openprint.setObjectName(u"btn_openprint")

        self.horizontalLayout_4.addWidget(self.btn_openprint)

        self.txt_fileprint = QLineEdit(self.page_savepdf)
        self.txt_fileprint.setObjectName(u"txt_fileprint")

        self.horizontalLayout_4.addWidget(self.txt_fileprint)

        self.btn_print = QPushButton(self.page_savepdf)
        self.btn_print.setObjectName(u"btn_print")

        self.horizontalLayout_4.addWidget(self.btn_print)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_opendoc = QPushButton(self.page_savepdf)
        self.btn_opendoc.setObjectName(u"btn_opendoc")

        self.horizontalLayout_5.addWidget(self.btn_opendoc)

        self.txt_filedoc = QLineEdit(self.page_savepdf)
        self.txt_filedoc.setObjectName(u"txt_filedoc")

        self.horizontalLayout_5.addWidget(self.txt_filedoc)

        self.btn_printdoc = QPushButton(self.page_savepdf)
        self.btn_printdoc.setObjectName(u"btn_printdoc")

        self.horizontalLayout_5.addWidget(self.btn_printdoc)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.tableWidget_2 = QTableWidget(self.page_savepdf)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_2.addWidget(self.tableWidget_2)

        self.Pages.addWidget(self.page_savepdf)

        self.verticalLayout_4.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 656, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        icon = QIcon()
        icon.addFile(u"icons/categories.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon)
        self.menuOperation = QMenu(self.menubar)
        self.menuOperation.setObjectName(u"menuOperation")
        self.menuInbound = QMenu(self.menuOperation)
        self.menuInbound.setObjectName(u"menuInbound")
        self.menuOutbound_2 = QMenu(self.menuOperation)
        self.menuOutbound_2.setObjectName(u"menuOutbound_2")
        self.menuAUTOMATION = QMenu(self.menubar)
        self.menuAUTOMATION.setObjectName(u"menuAUTOMATION")
        self.menuSAP = QMenu(self.menuAUTOMATION)
        self.menuSAP.setObjectName(u"menuSAP")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.BottomToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuOperation.menuAction())
        self.menubar.addAction(self.menuAUTOMATION.menuAction())
        self.menu.addAction(self.actionOPERATION)
        self.menu.addAction(self.actionAUTOMATION)
        self.menu.addAction(self.actionREPORTS)
        self.menuOperation.addAction(self.menuInbound.menuAction())
        self.menuOperation.addAction(self.menuOutbound_2.menuAction())
        self.menuInbound.addAction(self.actionCheck_Materials)
        self.menuInbound.addSeparator()
        self.menuOutbound_2.addSeparator()
        self.menuOutbound_2.addAction(self.actionAudit_Materials_2)
        self.menuAUTOMATION.addAction(self.menuSAP.menuAction())
        self.menuSAP.addAction(self.actionPrint_PDF)
        self.menuSAP.addAction(self.actionCreate_Orders)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionTELEFONICA.setText(QCoreApplication.translate("MainWindow", u"TELEFONICA", None))
        self.actionSAMSUNG.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.actionInbound.setText(QCoreApplication.translate("MainWindow", u"Inbound", None))
        self.actionInbound_2.setText(QCoreApplication.translate("MainWindow", u"Inbound", None))
        self.actionOutbound.setText(QCoreApplication.translate("MainWindow", u"Outbound", None))
        self.actionCheck_Materials.setText(QCoreApplication.translate("MainWindow", u"Check Materials", None))
        self.actionPrint_Docs_SAP.setText(QCoreApplication.translate("MainWindow", u"Print Docs SAP", None))
        self.actionCheck_Materials_2.setText(QCoreApplication.translate("MainWindow", u"Check Materials", None))
        self.actionSave_PDF_SAP.setText(QCoreApplication.translate("MainWindow", u"Save PDF SAP", None))
        self.actionAudit_Materials.setText(QCoreApplication.translate("MainWindow", u"Audit Materials", None))
        self.actionSave_PDF_SAP_2.setText(QCoreApplication.translate("MainWindow", u"Save PDF SAP", None))
        self.actionAudit_Materials_2.setText(QCoreApplication.translate("MainWindow", u"Audit Materials", None))
        self.actionPrint_PDF.setText(QCoreApplication.translate("MainWindow", u"Print PDF", None))
        self.actionCreate_Orders.setText(QCoreApplication.translate("MainWindow", u"Create Orders", None))
        self.actionOPERATION.setText(QCoreApplication.translate("MainWindow", u"OPERATION", None))
        self.actionAUTOMATION.setText(QCoreApplication.translate("MainWindow", u"AUTOMATION", None))
        self.actionREPORTS.setText(QCoreApplication.translate("MainWindow", u"REPORTS", None))
        self.actionLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.CreateOrders.setText(QCoreApplication.translate("MainWindow", u"CREATE ORDERS", None))
        self.Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.user_create.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User", None))
        self.pass_create.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_login_create.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.txt_filecreation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Excel File", None))
        self.btn_creation.setText(QCoreApplication.translate("MainWindow", u"Create Orders", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"Close SAP", None))
        ___qtablewidgetitem = self.tb_creation.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"INDICE", None));
        ___qtablewidgetitem1 = self.tb_creation.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PEDIDO", None));
        ___qtablewidgetitem2 = self.tb_creation.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ENTREGA", None));
        ___qtablewidgetitem3 = self.tb_creation.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"PROYECTO", None));
        ___qtablewidgetitem4 = self.tb_creation.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"MATERIAL", None));
        ___qtablewidgetitem5 = self.tb_creation.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CANTIDAD", None));
        ___qtablewidgetitem6 = self.tb_creation.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"FECHA", None));
        ___qtablewidgetitem7 = self.tb_creation.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"CENTRO", None));
        ___qtablewidgetitem8 = self.tb_creation.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ALM.DEST", None));
        ___qtablewidgetitem9 = self.tb_creation.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"LOTE", None));
        ___qtablewidgetitem10 = self.tb_creation.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OT", None));
        ___qtablewidgetitem11 = self.tb_creation.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None));
        self.SavePDF.setText(QCoreApplication.translate("MainWindow", u"SAVE PDF", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.user_save.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User", None))
        self.pass_save.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_login_save.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_openprint.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.txt_fileprint.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Excel File", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Save PDF", None))
        self.btn_opendoc.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.txt_filedoc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Excel File", None))
        self.btn_printdoc.setText(QCoreApplication.translate("MainWindow", u"Create Doc", None))
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"DOCUMENTO", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ENTREGA", None));
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.menuOperation.setTitle(QCoreApplication.translate("MainWindow", u"OPERATION", None))
        self.menuInbound.setTitle(QCoreApplication.translate("MainWindow", u"Inbound", None))
        self.menuOutbound_2.setTitle(QCoreApplication.translate("MainWindow", u"Outbound", None))
        self.menuAUTOMATION.setTitle(QCoreApplication.translate("MainWindow", u"AUTOMATION", None))
        self.menuSAP.setTitle(QCoreApplication.translate("MainWindow", u"SAP", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

