import flet as ft
import sys

# БЕЗОПАСНЫЙ ИМПОРТ
try:
    import pyrebase
    PYREBASE_READY = True
except ImportError:
    PYREBASE_READY = False

# Твой конфиг
config = {
    "apiKey": "AIzaSyAbiRCuR9egtHKg0FNzzBdL9dNqPqpPLNk",
    "authDomain": "ghost-pro-5aa22.firebaseapp.com",
    "databaseURL": "https://ghost-pro-5aa22-default-rtdb.firebaseio.com",
    "projectId": "ghost-pro-5aa22",
    "storageBucket": "ghost-pro-5aa22.firebasestorage.app",
    "messagingSenderId": "332879455079",
    "appId": "1:332879455079:android:15c36642c62d13e0dd05c2"
}

def main(page: ft.Page):
    page.title = "Ghost PRO"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10

    # ТЕРМИНАЛ
    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=250)
    
    def log(msg, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {msg}", color=color, font_family="monospace", size=12))
        page.update()

    # Поля
    user_field = ft.TextField(label="USER_NAME", border_color="#00FF00", color="#00FF00")
    email_field = ft.TextField(label="EMAIL", border_color="#00FF00", color="#00FF00")
    pass_field = ft.TextField(label="PASSWORD", password=True, border_color="#00FF00", color="#00FF00")

    # Инициализация Firebase внутри main
    auth = None
    db = None
    if PYREBASE_READY:
        try:
            firebase = pyrebase.initialize_app(config)
            auth = firebase.auth()
            db = firebase.database()
            log("SYSTEM: FIREBASE CONNECTED")
        except Exception as e:
            log(f"FIREBASE ERROR: {str(e)}", "red")
    else:
        log("CRITICAL ERROR: MODULE 'pyrebase' NOT FOUND IN APK", "red")

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_OS: ENCRYPTED", color="#00FF00", size=20),
                    ft.Container(content=terminal, border=ft.border.all(1, "#00FF00"), padding=10, bgcolor="#000A00"),
                    user_field, email_field, pass_field,
                    ft.ElevatedButton("LOG_IN", on_click=lambda _: page.go("/chat"), bgcolor="#228822", color="white", width=400)
                ])
            )
        elif page.route == "/chat":
            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_CHAT"), bgcolor="#001100"),
                    ft.Text("MESSENGER ACTIVE", color="#00FF00"),
                    ft.ElevatedButton("BACK", on_click=lambda _: page.go("/"))
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    log("[SYSTEM]: ОЖИДАНИЕ...")

ft.app(target=main)
