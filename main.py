from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QLineEdit)
from ui_main import Ui_MainWindow
import sys
from sap import SapGui
import pandas as pd
import win32gui
import win32con
import os


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("LionOps Automation")

        self.sap = SapGui()

    #---------------- BUTTONS MENU -------------#
        #self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))        
        #self.btn_inbound.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_inbound))
        #self.btn_about.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_about))
        self.actionPrint_PDF.triggered.connect(lambda: self.Pages.setCurrentWidget(self.page_savepdf))
        self.actionCreate_Orders.triggered.connect(lambda: self.Pages.setCurrentWidget(self.page_createorders))
    #------------------------------------------#

    #-------------- BUTTONS PAGE CREATE ORDERS ------------#
        self.btn_open.clicked.connect(self.open_filecreation) # button to open file dialog
        self.btn_login_create.clicked.connect(lambda: self.login_sap("user_create", "pass_create", self.btn_login_create)) # button for conection to SAP
        self.btn_creation.clicked.connect(self.creation_clicked) # button for creation of documents
        self.btn_close.clicked.connect(self.close_system)# button for close SAP

    #-------------- BUTTONS PAGE SAVE PDF ------------#
        self.btn_login_save.clicked.connect(lambda: self.login_sap("user_save", "pass_save", self.btn_login_save)) # button for conection to SAP
        self.btn_openprint.clicked.connect(self.open_fileprint) # button to open file of save pdf
        self.btn_print.clicked.connect(self.print_clicked)# button for save documents
        self.btn_opendoc.clicked.connect(self.open_filedoc)# button for open file pdf with identity
        self.btn_printdoc.clicked.connect(self.printdoc_clicked)# button for create pdf with identity for each order
    #-------------------------------------------#

    #--------------- FUNCTIONS -----------------#

    def _get_line_text(self, name: str) -> str: #Obtener nombres de lineEdit en gui
        parent = getattr(self, "ui", self)
        edit = parent.findChild(QLineEdit, name)
        return edit.text().strip() if edit else ""

    def login_sap(self, user_field: str, pass_field: str, btn):
        username = self._get_line_text(user_field) # Get user with def
        password = self._get_line_text(pass_field) # Get user with def

        if not username or not password:# Check if user or password are empty
            QMessageBox.warning(
                self,
                "Missing Data",
                "Please enter both USER and PASSWORD before logging in."
            )
            return
        
        btn.setEnabled(False)

        try:
            ok = self.sap.login_sap(username, password,system_name="EPA [ANDINA_COPA]")
            if ok:
                QMessageBox.information(self, "SAP Login", "Login successfully.")
        except Exception as e:
            QMessageBox.critical(self, "SAP Login", f"Session unsuccessfull:\n{e}")
        finally:
            btn.setEnabled(True)

        getattr(self, user_field).clear()
        getattr(self, pass_field).clear()

    #--------------- CREATION ORDERS -----------------#
    def open_filecreation(self):
        file_path_creation, _ = QFileDialog.getOpenFileName(self, "Select File","","Excel Files (*.xlsx *.xls)")

        if not file_path_creation:
            return

        self.file_path_creation = file_path_creation
        self.txt_filecreation.setText(file_path_creation)
        self.load_excel_creation(file_path_creation, sheet_name='Creation')

    def load_excel_creation(self, file_path_creation: str, sheet_name: str='Creation'):
        try:
            df = pd.read_excel(file_path_creation, sheet_name=sheet_name, dtype=str)
        except FileNotFoundError:
            QMessageBox.warning(self, "File not Found", f"Not Found:\n{self.file_path_creation}")
            return
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Sheet", f"Sheet not Read '{sheet_name}':\n{e}")
            return
        except Exception as e:
            QMessageBox.critical(self, "Wrong Excel Reading", str(e))
            return

        df = df.fillna("") #Clean NaN values

        tbl = self.tb_creation # o self.ui.tableWidget
        tbl.setSortingEnabled(False)
        tbl.clearContents()
        tbl.setRowCount(len(df))
        tbl.setColumnCount(len(df.columns))
        tbl.setHorizontalHeaderLabels([str(c) for c in df.columns])

        for r in range(len(df)):# Change dataframe to table
            for c, col in enumerate(df.columns):
                tbl.setItem(r, c, QTableWidgetItem(str(df.iat[r, c])))

        tbl.resizeColumnsToContents()

        self._df_creation = df #Save DataFrame as attribute for later use

    def creation_clicked(self):
        if not getattr(self, 'file_path_creation', None): # Read file path from txt_filecreation
            QMessageBox.information(self, "No file selected", "Please select a file to create documents from.")
            return

        user = os.getlogin() # Get current user
        file_folder = rf"C:\Users\{user}\Downloads"

        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Creation Documents")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Creation documents")
        msgBox.setInformativeText("Are you sure you want to create the documents?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setModal(True)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:

            try:
                self.showMinimized()
                self.sap.create_documents(self.txt_filecreation.text(), file_folder)# Send file path and pdf folder to create_documents
                msg = QMessageBox(self)
                msg.setWindowTitle("Creation")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Documents created successfully.")
                msg.exec()
            except Exception as e:
                QMessageBox.critical(self, "Creation Error", f"Error creating documents:\n{e}")
                return
    # ------------------------------------------- #

    #--------------- PRINT ORDERS -----------------#
    def open_fileprint(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File","","Excel Files (*.xlsx *.xls)")

        if not file_path:
            return
        
        self.file_path = file_path
        self.txt_fileprint.setText(file_path)
        self.load_excel_print(file_path, sheet_name='Print')

    def load_excel_print(self, file_path: str, sheet_name: str='Print'):
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name, dtype=str)
        except FileNotFoundError:
            QMessageBox.warning(self, "File not Found", f"Not Found:\n{file_path}")
            return
        except ValueError as e:
            QMessageBox.warning(self, "Invalid Sheet", f"Sheet not Read '{sheet_name}':\n{e}")
            return
        except Exception as e:
            QMessageBox.critical(self, "Wrong Excel Reading", str(e))
            return

        df = df.fillna("") #Clean NaN values

        tbl = self.tb_print # o self.ui.tableWidget
        tbl.setSortingEnabled(False)
        tbl.clearContents()
        tbl.setRowCount(len(df))
        tbl.setColumnCount(len(df.columns))
        tbl.setHorizontalHeaderLabels([str(c) for c in df.columns])

        for r in range(len(df)):# Change dataframe to table
            for c, col in enumerate(df.columns):
                tbl.setItem(r, c, QTableWidgetItem(str(df.iat[r, c])))

        tbl.resizeColumnsToContents()

        self._df_print = df #Save DataFrame as attribute for later use

    def print_clicked(self):
        if not getattr(self, 'file_path', None): # Read file path from txt_fileprint
            QMessageBox.information(self, "No file selected", "Please select a file to print documents from.")
            return
        
        user= os.getlogin() # Get current user
        
        pdf_folder = rf"C:\Users\{user}\Downloads" # Define pdf folder path

        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Print Documents")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Print documents")
        msgBox.setInformativeText("Are you sure you want to print the documents?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setModal(True)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:

            try:
                self.showMinimized()
                self.sap.print_documents(self.txt_fileprint.text(), pdf_folder)# Send file path and pdf folder to print_documents
                msg = QMessageBox(self)
                msg.setWindowTitle("Print")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Documents printed successfully.")
                msg.exec()
            except Exception as e:
                QMessageBox.critical(self, "Print Error", f"Error printing documents:\n{e}")
                return
            finally:
            # 🔹 Restore app when print job has finished
                self.showNormal()
                self.raise_()
                self.activateWindow()

            hwnd = self.winId()
            try:
                win32gui.SetForegroundWindow(hwnd)
            except:
                pass

            win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
            win32gui.SetWindowPos(
                hwnd,
                win32con.HWND_TOPMOST,
                0, 0, 0, 0,
                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
            )
            win32gui.SetWindowPos(
                hwnd,
                win32con.HWND_NOTOPMOST,
                0, 0, 0, 0,
                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
            )
    # ------------------------------------------- #

    # --------------- PRINT DOC C.C ------------- #
    def open_filedoc(self):
        file_path_doc, _ = QFileDialog.getOpenFileName(self, "Select File","","PDF Files (*.pdf)")

        if not file_path_doc:
            return
        
        self.file_path_doc = file_path_doc
        self.txt_filedoc.setText(file_path_doc)
        self.sap.file_path_doc = file_path_doc
    
    def printdoc_clicked(self):

        file_path = self.txt_filedoc.text().strip()

        if not file_path:
            QMessageBox.information(
                self,
                "No file selected",
                "Please select a file to create documents"
            )
            return
        
        user= os.getlogin() # Get current user
        
        pdf_folder = rf"C:\Users\{user}\Downloads" # Define pdf folder path

        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Print Documents")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Print documents")
        msgBox.setInformativeText("Are you sure you want to create the documents?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setModal(True)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:

            try:
                self.showMinimized()
                self.sap.save_docs(self._df_print, pdf_folder)
                
                msg = QMessageBox(self)
                msg.setWindowTitle("Print")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Documents Saved successfully.")
                msg.exec()
            except Exception as e:
                QMessageBox.critical(self, "Print Error", f"Error saving documents:\n{e}")
                return
            finally:
            # 🔹 Restore app when print job has finished
                self.showNormal()
                self.raise_()
                self.activateWindow()
    # ------------------------------------------- #

    def close_system(self):
        self.sap.close_sap()
        #-------------------------------------------#

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()