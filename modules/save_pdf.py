from PySide6.QtWidgets import QMessageBox, QLineEdit, QFileDialog, QTableWidgetItem
from PySide6.QtCore import QObject
import pandas as pd
import os
import win32gui
import win32con

class SavePDFController(QObject):
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = main_window.ui
        self.sap = main_window.sap

        self._df_print = None
        self.file_path = None
        self.file_path_doc = None

        self.connect_signals()

    #--------------- Buttons Page ------------------#
    def connect_signals(self):
        self.ui.btn_login_save.clicked.connect(lambda: self.login_sap("user_save", "pass_save", self.ui.btn_login_save)) # button for conection to SAP
        self.ui.btn_openprint.clicked.connect(self.open_fileprint) # button to open file of save pdf
        self.ui.btn_print.clicked.connect(self.print_clicked)# button for save documents
        self.ui.btn_opendoc.clicked.connect(self.open_filedoc)# button for open file pdf with identity
        self.ui.btn_printdoc.clicked.connect(self.printdoc_clicked)# button for create pdf with identity for each order

    #------------------- Get Line Edit Text ------------------#
    def _get_line_text(self, name: str) -> str: #Obtener nombres de lineEdit en gui
        edit = self.main_window.findChild(QLineEdit, name)
        return edit.text().strip() if edit else ""
    
    #------------------- SAP Login ------------------#
    def login_sap(self, user_field: str, pass_field: str, btn):
        username = self._get_line_text(user_field) # Get user with def
        password = self._get_line_text(pass_field) # Get user with def

        if not username or not password:# Check if user or password are empty
            QMessageBox.warning(
                self.main_window,
                "Missing Data",
                "Please enter both USER and PASSWORD before logging in."
            )
            return

        btn.setEnabled(False)

        try:
            ok = self.sap.login(username, password,system_name="EPA [ANDINA_COPA]")
            if ok:
                QMessageBox.information(self.main_window, "SAP Login", "Login successfully.")
        except Exception as e:
            QMessageBox.critical(self.main_window, "SAP Login", f"Session unsuccessfull:\n{e}")
        finally:
            btn.setEnabled(True)

        edit_user = self.main_window.findChild(QLineEdit, user_field)
        edit_pass = self.main_window.findChild(QLineEdit, pass_field)

        if edit_user:
            edit_user.clear()
        if edit_pass:
            edit_pass.clear()

    #------------------- Print Documents ------------------#
    def open_fileprint(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Select File","","Excel Files (*.xlsx *.xls)")

        if not file_path:
            return
        
        self.file_path = file_path
        self.ui.txt_fileprint.setText(file_path)
        self.load_excel_print(file_path, sheet_name='Print')

    def load_excel_print(self, file_path: str, sheet_name: str='Print'):
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name, dtype=str)
        except FileNotFoundError:
            QMessageBox.warning(self.main_window, "File not Found", f"Not Found:\n{file_path}")
            return
        except ValueError as e:
            QMessageBox.warning(self.main_window, "Invalid Sheet", f"Sheet not Read '{sheet_name}':\n{e}")
            return
        except Exception as e:
            QMessageBox.critical(self.main_window, "Wrong Excel Reading", str(e))
            return

        df = df.fillna("") #Clean NaN values

        tbl = self.ui.tb_print # o self.ui.tableWidget
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
            QMessageBox.information(self.main_window, "No file selected", "Please select a file to print documents from.")
            return
        
        user= os.getlogin() # Get current user
        
        pdf_folder = rf"C:\Users\{user}\Downloads" # Define pdf folder path

        msgBox = QMessageBox(self.main_window)
        msgBox.setWindowTitle("Print Documents")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Print documents")
        msgBox.setInformativeText("Are you sure you want to print the documents?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setModal(True)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:

            try:
                self.main_window.showMinimized()
                self.sap.print_documents(self.file_path, pdf_folder)# Send file path and pdf folder to print_documents
                msg = QMessageBox(self.main_window)
                msg.setWindowTitle("Print")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Documents printed successfully.")
                msg.exec()
            except Exception as e:
                QMessageBox.critical(self.main_window, "Print Error", f"Error printing documents:\n{e}")
                return
            finally:
            # 🔹 Restore app when print job has finished
                self.main_window.showNormal()
                self.main_window.raise_()
                self.main_window.activateWindow()

            hwnd = int(self.main_window.winId())
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

    #------------------- PDF with identity ------------------#

    def open_filedoc(self):
        file_path_doc, _ = QFileDialog.getOpenFileName(self.main_window, "Select File","","PDF Files (*.pdf)")

        if not file_path_doc:
            return
        
        self.file_path_doc = file_path_doc
        self.ui.txt_filedoc.setText(file_path_doc)
        self.sap.file_path_doc = file_path_doc

    def printdoc_clicked(self):
        file_path = getattr(self, "file_path_doc", "")  # Read file path from txt_filedoc

        if not file_path:
            QMessageBox.information(
                self.main_window,
                "No file selected",
                "Please select a file to create documents"
            )
            return
        
        user= os.getlogin() # Get current user
        
        pdf_folder = rf"C:\Users\{user}\Downloads" # Define pdf folder path

        msgBox = QMessageBox(self.main_window)
        msgBox.setWindowTitle("Print Documents")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Print documents")
        msgBox.setInformativeText("Are you sure you want to create the documents?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setModal(True)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:

            try:
                self.main_window.showMinimized()
                self.sap.save_docs(self._df_print, pdf_folder, self.file_path_doc)
                msg = QMessageBox(self.main_window)
                msg.setWindowTitle("Print")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Documents Saved successfully.")
                msg.exec()
            except Exception as e:
                QMessageBox.critical(self.main_window, "Print Error", f"Error saving documents:\n{e}")
                return
            finally:
            # 🔹 Restore app when print job has finished
                self.main_window.showNormal()
                self.main_window.raise_()
                self.main_window.activateWindow()



