        import flet as ft
import sys

# Пытаемся импортировать модули так, чтобы не было черного экрана
try:
    import pyrebase
    from cryptography.fernet import Fernet
    STATUS = "SYSTEM_READY: ENCRYPTION ACTIVE"
except Exception as e:
    STATUS = f"SYSTEM_ERROR: {str(e)}"

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
    page.title = "Ghost PRO Official"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    
    # ТЕРМИНАЛ
    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=250)
    def log(msg, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {msg}", color=color, font_family="monospace", size=12))
        page.update()

    # Поля
    email_f = ft.TextField(label="EMAIL", border_color="#00FF00", color="#00FF00")
    pass_f = ft.TextField(label="PASSWORD", password=True, border_color="#00FF00", color="#00FF00")

    def login(e):
        # ТВОЯ АДМИНКА
        if email_f.value == "adminpan" and pass_f.value == "TimaIssam2026":
            log("ADMIN ACCESS GRANTED", "yellow")
            page.go("/chat")
        else:
            log("AUTH ATTEMPT...")

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_OS terminal", color="#00FF00", size=20),
                    ft.Container(terminal, border=ft.border.all(1, "#00FF00"), padding=10),
                    email_f, pass_f,
                    ft.ElevatedButton("EXECUTE", on_click=login, bgcolor="#114411", color="white", width=400)
                ])
            )
        elif page.route == "/chat":
            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_CHAT"), bgcolor="#001100"),
                    ft.Text("MESSENGER ACTIVE (E2EE)", color="#00FF00"),
                    ft.TextField(placeholder="Search user or type..."),
                    ft.Row([ft.IconButton(ft.icons.MIC), ft.IconButton(ft.icons.CAMERA), ft.IconButton(ft.icons.SEND)])
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    log(STATUS)

ft.app(target=main)
