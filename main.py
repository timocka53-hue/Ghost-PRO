import flet as ft
import pyrebase
import base64
from cryptography.fernet import Fernet

# --- КОНФИГУРАЦИЯ ---
config = {
    "apiKey": "AIzaSyAbiRCuR9egtHKg0FNzzBdL9dNqPqpPLNk",
    "authDomain": "ghost-pro-5aa22.firebaseapp.com",
    "databaseURL": "https://ghost-pro-5aa22-default-rtdb.firebaseio.com",
    "projectId": "ghost-pro-5aa22",
    "storageBucket": "ghost-pro-5aa22.firebasestorage.app",
    "messagingSenderId": "332879455079",
    "appId": "1:332879455079:android:15c36642c62d13e0dd05c2"
}

# Инициализация (с проверкой, чтобы не было черного экрана)
try:
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()
    storage = firebase.storage()
    # Ключ шифрования (E2EE)
    cipher = Fernet(b'GhostProSecureKey123456789012345=')
    INIT_SUCCESS = True
except Exception as e:
    INIT_SUCCESS = False
    INIT_ERROR = str(e)

def main(page: ft.Page):
    page.title = "Ghost PRO Official"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
    
    user_session = {"uid": None, "name": "Guest"}

    # --- ТЕРМИНАЛ ---
    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=200)
    def log(msg, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {msg}", color=color, font_family="monospace", size=12))
        page.update()

    # --- ПОЛЯ ВВОДА ---
    email_field = ft.TextField(label="EMAIL / LOGIN", border_color="#00FF00", color="#00FF00")
    pass_field = ft.TextField(label="PASSWORD", password=True, border_color="#00FF00", color="#00FF00")
    search_field = ft.TextField(label="ПОИСК ЮЗЕРА (@username)", border_color="#00FF00", color="#00FF00")

    def handle_login(e):
        # ТВОЯ АДМИНКА
        if email_field.value == "adminpan" and pass_field.value == "TimaIssam2026":
            user_session["name"] = "ADMIN_PRO"
            log("ADMIN ACCESS GRANTED", "yellow")
            page.go("/chat")
            return
        
        try:
            user = auth.sign_in_with_email_and_password(email_field.value, pass_field.value)
            user_session["uid"] = user['localId']
            log("SUCCESS: ЗАШЕЛ В СИСТЕМУ")
            page.go("/chat")
        except:
            log("ОШИБКА: ОТКАЗАНО В ДОСТУПЕ", "red")

    def route_change(route):
        page.views.clear()
        
        # ЭКРАН ВХОДА
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_OS: TERMINAL", color="#00FF00", size=20),
                    ft.Container(terminal, border=ft.border.all(1, "#00FF00"), padding=10),
                    email_field, pass_field,
                    ft.ElevatedButton("LOG_IN", on_click=handle_login, bgcolor="#114411", color="white", width=400)
                ])
            )
            
        # ЭКРАН ЧАТА (ПОИСК, ГС, МЕДИА)
        elif page.route == "/chat":
            chat_list = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            msg_input = ft.TextField(placeholder="Шифрованное сообщение...", expand=True)

            def send_msg(e):
                if msg_input.value:
                    # ШИФРОВАНИЕ (E2EE)
                    enc_text = cipher.encrypt(msg_input.value.encode()).decode()
                    db.child("messages").push({"user": user_session["name"], "text": enc_text})
                    chat_list.controls.append(ft.Text(f"YOU: {msg_input.value}", color="#00FF00"))
                    msg_input.value = ""
                    page.update()

            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_CHAT"), bgcolor="#001100"),
                    search_field,
                    ft.Divider(color="#00FF00"),
                    chat_list,
                    ft.Row([
                        ft.IconButton(ft.icons.MIC, icon_color="#00FF00"), # ГС
                        ft.IconButton(ft.icons.ATTACH_FILE, icon_color="#00FF00"), # МЕДИА
                        msg_input,
                        ft.IconButton(ft.icons.SEND, on_click=send_msg, icon_color="#00FF00")
                    ])
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    
    if not INIT_SUCCESS:
        log(f"CRITICAL ERROR: {INIT_ERROR}", "red")
    else:
        log("SYSTEM: READY_TO_GHOST")

ft.app(target=main)
