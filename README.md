# 🚀 LionOps Automation

Enterprise-grade automation platform for SAP processes using Python, Qt (PySide6) and SAP GUI Scripting.

---

## 🎯 Purpose

LionOps Automation centralizes and automates operational SAP processes such as:

- 📄 Printing SAP documents
- 🧾 Creating SAP orders
- 📂 Saving PDFs automatically
- ⚙️ Future logistics & WMS automation modules

---

## 🧱 Architecture Overview

This project follows **Clean Architecture + Hexagonal principles**, ensuring:

- Clear separation of concerns
- Scalability
- Safe SAP automation
- Maintainability

---

## 🏗️ High-Level Architecture

```mermaid
flowchart TB
    User[👤 User]
    UI[🪟 Qt UI]
    Controllers[🎮 Controllers]
    Facade[🧱 SapFacade]
    SAPIntegration[🔌 SAP Integration]
    SAP[🏭 SAP System]

    User --> UI --> Controllers --> Facade --> SAPIntegration --> SAP

