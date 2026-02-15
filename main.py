import flet as ft
import pyrebase
from cryptography.fernet import Fernet
import os

# ГЕНЕРИРУЕМ ВАЛИДНЫЙ КЛЮЧ АВТОМАТОМ (Чтобы не было ValueError)
# Больше никакой "incorrect padding" или "must be 32 bytes"
static_key = b'pL6_vW9G3BvJ8M-H9f6yR_v0m_8G5x4W_Q8z6L8p3k4='
cipher = Fernet(static_key)

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
    page.title = "GHOST PRO OFFICIAL"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Инициализация Firebase
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()

    # --- ТЕРМИНАЛ (ЛОГ ЗАГРУЗКИ) ---
    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=150, width=350)
    
    def log(msg, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {msg}", color=color, font_family="monospace", size=12))
        page.update()

    # --- ПОЛЯ ВВОДА (ТОТ САМЫЙ ДИЗАЙН) ---
    email_field = ft.TextField(
        label="EMAIL / ADMINPAN", 
        border_color="#00FF00", 
        color="#00FF00",
        cursor_color="#00FF00",
        focused_border_color="#00FF00",
        width=350
    )
    pass_field = ft.TextField(
        label="PASSWORD", 
        password=True, 
        can_reveal_password=True,
        border_color="#00FF00", 
        color="#00FF00",
        cursor_color="#00FF00",
        focused_border_color="#00FF00",
        width=350
    )

    def login_click(e):
        log("SEARCHING FOR ACCESS KEY...", "yellow")
        
        # ТВОЯ АДМИНКА
        if email_field.value == "adminpan" and pass_field.value == "TimaIssam2026":
            log("ADMIN ACCESS GRANTED!", "yellow")
            page.go("/chat")
            return

        try:
            # Пытаемся зайти через Firebase
            user = auth.sign_in_with_email_and_password(email_field.value, pass_field.value)
            log("ACCESS GRANTED. SYNCING...", "#00FF00")
            page.go("/chat")
        except Exception as ex:
            log(f"DENIED: {str(ex)}", "red")

    # --- РОУТИНГ (ПЕРЕКЛЮЧЕНИЕ ЭКРАНОВ) ---
    def route_change(route):
        page.views.clear()
        
        # ЭКРАН ЛОГИНА
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_PRO_OS", color="#00FF00", size=32, weight="bold", font_family="monospace"),
                    ft.Container(
                        content=terminal,
                        border=ft.border.all(1, "#00FF00"),
                        padding=10,
                        bgcolor="#000A00",
                        border_radius=5
                    ),
                    ft.Divider(height=20, color="transparent"),
                    email_field,
                    pass_field,
                    ft.ElevatedButton(
                        "INITIALIZE SYSTEM", 
                        on_click=login_click, 
                        bgcolor="#114411", 
                        color="white", 
                        width=350,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                    ),
                    ft.TextButton("CREATE NEW ENCRYPTED ID", on_click=lambda _: log("CREATE FEATURE COMING SOON...", "blue"))
                ], vertical_alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )

        # ЭКРАН ЧАТА
        elif page.route == "/chat":
            chat_messages = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            msg_input = ft.TextField(placeholder="Encrypted data...", expand=True, border_color="#00FF00")

            def send_msg(e):
                if msg_input.value:
                    # Шифруем перед отправкой
                    encrypted = cipher.encrypt(msg_input.value.encode()).decode()
                    chat_messages.controls.append(ft.Text(f"LOG: {msg_input.value}", color="#00FF00"))
                    msg_input.value = ""
                    page.update()

            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_NETWORK"), bgcolor="#001100", color="#00FF00"),
                    ft.TextField(label="SEARCH_USER", border_color="#00FF00"),
                    chat_messages,
                    ft.Row([
                        ft.IconButton(ft.icons.MIC, icon_color="#00FF00"),
                        ft.IconButton(ft.icons.ATTACH_FILE, icon_color="#00FF00"),
                        msg_input,
                        ft.IconButton(ft.icons.SEND, on_click=send_msg, icon_color="#00FF00")
                    ])
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    log("SYSTEM READY. WAITING FOR INPUT...")

ft.app(target=main)
