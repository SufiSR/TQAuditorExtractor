# TQAuditor Extract Tool

A lightweight, offline-friendly, no-installation-needed viewer for TQAuditor project data — built with 💻 Python, 🚀 Flask, and ☁️ PyInstaller.  

Includes a modern web interface, system tray integration, and graceful shutdown. Just double-click and use it in your browser!

---

## 📦 Features

- ✅ View TQAuditor project data in a simple web interface
- ✅ Filter projects by ID, Client, Name, or Status (live client-side filtering)
- ✅ Click a project to view full details
- ✅ Download DOCX reports with evaluation summaries and mistake counts
- ✅ System tray icon with tooltip + exit button
- ✅ Launches automatically in browser
- ✅ Bundled `.exe` — **no Python required**

---

## 🚀 Getting Started

### 🔸 For Non-Technical Users

1. Download `TQAuditorApp.exe` from [Releases](https://github.com/SufiSR/TQAuditorExtractor/releases/tag/Executable)
2. Double-click the `.exe`
3. Your browser will open `http://localhost:5000`
4. Use the app
5. To quit, right-click the red dot in the system tray → `Exit`

> 💡 If you don't see the icon, check the tray overflow (`^` next to the clock)



### 🔹 For Developers

#### 📁 Folder Structure


````
project/
├── app.py               # Flask API logic
├── run\_server.py        # Tray app + launcher
├── templates/
│   └── index.html       # Web UI
├── static/
│   └── styles.css       # Styles
├── assets/
│   ├── icon.ico         # App window icon
│   └── icon.png         # Tray icon
├── requirements.txt     # Used for local dev

````

#### 🧪 Run in Dev Mode

```bash
pip install -r requirements.txt
python run_server.py
````

Then visit [http://localhost:5000](http://localhost:5000)

---

## 🛠️ Building the Executable

### ✅ Requirements

* Python 3.10+
* `pyinstaller`, `pystray`, `pillow`, `flask`, `requests`

Install dependencies:

```bash
pip install -r requirements.txt
```

### 🔧 Build Command (Windows PowerShell)

```powershell
pyinstaller --onefile --noconsole --clean `
  --icon=assets/icon.ico `
  --add-data "assets;assets" `
  --add-data "templates;templates" `
  --add-data "static;static" `
  run_server.py
```

This creates `dist/run_server.exe`

> 💡 Rename it to `tqauditor_extractor.exe` for end users

---

## 📎 Known Limitations

* **No auto-updates** — replace `.exe` for new versions
* Runs only on **localhost** by design (no remote access)
* Flask must run on port `5000` — configurable if needed

---

## 💡 Tips for Distribution

* Bundle the `.exe` with a short `README.txt` for non-tech users
* Optional: sign the `.exe` if distributing externally
* Avoid changing directory structure — `assets/icon.png` is required for the tray

---

## ❤️ Made with Love in Berlin by SR

This project was designed to help non-technical users easily browse project data in a clean, web-like experience — without installing Python or touching the terminal.

---

## 📃 License

MIT License — do whatever you want, just don’t blame me 😄

---
