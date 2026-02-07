# 🦁 LionOps Automation

LionOps Automation is a local tool developed to automate logistics processes in SAP using SAP GUI Scripting, reducing operational time, manual effort, and human errors.

---

## 🚀 Key Features

- Automation of SAP transactions (ME21N, MB21, MB02, SP02)
- Mass processing based on Excel files
- Automatic generation and storage of PDF documents
- Professional graphical user interface (PySide6 / Qt)
- Local execution (no SAP modifications required)

---

## 🧱 System Architecture

The application follows a layered architecture:

main.py
└── UI (Qt Designer)
└── Controllers (modules/)
└── SapFacade
└── Integrations (SAP GUI Scripting)


This structure ensures maintainability, scalability, and clear separation of responsibilities.

---

## 🧩 Components

### UI Layer
- `ui_main.py`
- Designed using Qt Designer
- Handles visual layout and user interaction only

### Controllers
- Manage UI events, validations, and user experience
- Do not contain SAP automation logic

### Facade Layer
- Centralizes SAP connection and session handling
- Orchestrates automation services
- Acts as an abstraction layer between UI and SAP logic

### Integrations Layer
- Executes SAP transactions
- Contains SAP GUI Scripting logic
- Represents the core automation know-how

---

## 🛠 Technologies Used

- Python
- PySide6 (Qt for Python)
- SAP GUI Scripting
- Pandas
- Windows API (Win32)

---

## 🔐 Security & Compliance

- No SAP standard functionality is modified
- No Z-programs or SAP custom developments are created
- No SAP plugins or add-ons are installed
- No credentials are stored
- Automation replicates standard user actions only

The tool operates entirely on DHL-managed computers.

---

## 📜 Intellectual Property

All source code, automation logic, and architectural design of LionOps Automation are the intellectual property of Brallan Leon.

The customer does not have access to the codebase or automation mechanisms, ensuring that process knowledge and innovation remain under DHL’s control.

---

## ▶️ Execution

To run the application:

```bash
python main.py
