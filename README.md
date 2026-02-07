# 🦁 LionOps Automation

LionOps Automation es una herramienta local desarrollada para automatizar procesos logísticos en SAP mediante SAP GUI Scripting, reduciendo tiempos operativos y errores manuales.

---

## 🚀 Características principales

- Automatización de transacciones SAP (ME21N, MB21, MB02, SP02)
- Procesamiento masivo desde archivos Excel
- Generación y guardado automático de documentos PDF
- Interfaz gráfica profesional (PySide6 / Qt)
- Ejecución local (sin modificar SAP)

---

## 🧱 Arquitectura del sistema

La aplicación está organizada en capas:

main.py
└── UI (Qt Designer)
└── Controllers (modules/)
└── SapFacade
└── Integrations (SAP GUI Scripting)


## 🧩 Componentes

### UI
- `ui_main.py`
- Diseñada en Qt Designer

### Controllers
- Manejan eventos, validaciones y experiencia de usuario
- No contienen lógica SAP

### Facade
- Centraliza la conexión y sesión SAP
- Orquesta las automatizaciones

### Integrations
- Ejecutan las transacciones SAP
- Contienen el know-how de automatización

---

## 🛠 Tecnologías

- Python
- PySide6 (Qt for Python)
- SAP GUI Scripting
- Pandas
- Win32 API

---

## 🔐 Seguridad

- No se modifica SAP
- No se instalan componentes adicionales
- No se almacenan credenciales
- Automatización basada en acciones estándar del usuario

---

## 📜 Propiedad intelectual

Este proyecto es propiedad intelectual de Brallan Leon.
El código y la lógica de automatización no están destinados a ser utilizados ni replicados por terceros sin autorización.

---

## ▶️ Ejecución

```bash
python main.py


