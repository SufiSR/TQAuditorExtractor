import threading
import time
import webbrowser
import requests
import sys
import os

from pystray import Icon, MenuItem as item, Menu
from PIL import Image, ImageDraw

from app import app  # import your Flask app


def open_browser():
    time.sleep(1)
    webbrowser.open("http://localhost:5000")


def create_icon():
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    icon_path = os.path.join(base_path, "assets", "my_icon.ico")
    return Image.open(icon_path)


def stop_server(icon):
    try:
        requests.post("http://localhost:5000/shutdown")
    except Exception:
        pass
    icon.stop()
    sys.exit(0)


def run_tray():
    icon = Icon("TQAuditor")
    icon.icon = create_icon()
    icon.title = "TQAuditor Extract – Running"  # ← Tooltip text
    icon.menu = Menu(
        item('Open TQAuditor Extract', lambda: webbrowser.open("http://localhost:5000")),
        item('Exit', lambda: stop_server(icon))
    )
    icon.run()


def run_flask():
    app.run(port=5000)


if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    threading.Thread(target=open_browser, daemon=True).start()
    run_tray()
