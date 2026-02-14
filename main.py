import flet as ft
import pyrebase
import time

# Конфиг из твоего google-services.json
config = {
    "apiKey": "AIzaSyAbiRCuR9egtHKg0FNzzBdL9dNqPqpPLNk",
    "authDomain": "ghost-pro-5aa22.firebaseapp.com",
    "databaseURL": "https://ghost-pro-5aa22-default-rtdb.firebaseio.com",
    "projectId": "ghost-pro-5aa22",
    "storageBucket": "ghost-pro-5aa22.firebasestorage.app",
    "messagingSenderId": "332879455079",
    "appId": "1:332879455079:android:15c36642c62d13e0dd05c2"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def main(page: ft.Page):
    page.title = "Ghost PRO"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
    
    user_data = {"uid": None, "username": None}

    # --- ЭЛЕМЕНТЫ ТЕРМИНАЛА ---
    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=250)
    
    def log(msg, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {msg}", color=color, font_family="monospace", size=12))
        page.update()

    # --- ЛОГИКА ---
    def handle_register(e):
        if not reg_user.value or not reg_email.value:
            log("ERROR: EMPTY FIELDS", "red")
            return
        try:
            user = auth.create_user_with_email_and_password(reg_email.value, reg_pass.value)
            auth.send_email_verification(user['idToken'])
            db.child("users").child(user['localId']).set({"username": reg_user.value})
            log(f"SUCCESS: CONFIRM EMAIL {reg_email.value}", "yellow")
        except Exception as ex:
            log(f"SYSTEM_ERROR: {str(ex)}", "red")

    def handle_login(e):
        if reg_email.value == "adminpan" and reg_pass.value == "TimaIssam2026":
            log("ADMIN ACCESS GRANTED", "yellow")
            page.go("/chat")
            return
        try:
            user = auth.sign_in_with_email_and_password(reg_email.value, reg_pass.value)
            user_data["uid"] = user['localId']
            log("ACCESS GRANTED. LOADING...")
            page.go("/chat")
        except:
            log("INVALID ACCESS KEY", "red")

    # --- ПОЛЯ ВВОДА ---
    reg_user = ft.TextField(label="USER_NAME", border_color="#00FF00", color="#00FF00")
    reg_email = ft.TextField(label="EMAIL", border_color="#00FF00", color="#00FF00")
    reg_pass = ft.TextField(label="PASSWORD", password=True, border_color="#00FF00", color="#00FF00")

    def route_change(route):
        page.views.clear()
        
        # ЭКРАН ВХОДА (Твой дизайн)
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_OS: ENCRYPTED_LINK", color="#00FF00"),
                    ft.Container(content=terminal, border=ft.border.all(1, "#00FF00"), padding=10, bgcolor="#000A00"),
                    reg_user, reg_email, reg_pass,
                    ft.Row([
                        ft.ElevatedButton("REGISTRATION", on_click=handle_register, bgcolor="#55FF55", color="black", expand=True),
                        ft.ElevatedButton("LOG_IN", on_click=handle_login, bgcolor="#228822", color="white", expand=True),
                    ])
                ])
            )
            
        # ЭКРАН МЕССЕНДЖЕРА
        if page.route == "/chat":
            chat_messages = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            search_box = ft.TextField(label="FIND_GHOST_BY_NAME", border_color="#00FF00")
            msg_input = ft.TextField(placeholder="TYPE_MESSAGE...", expand=True)

            def send_msg(e):
                if msg_input.value:
                    chat_messages.controls.append(ft.Text(f"YOU: {msg_input.value}", color="#00FF00"))
                    msg_input.value = ""
                    page.update()

            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_MESSENGER_V1"), bgcolor="#001100", color="#00FF00"),
                    search_box,
                    ft.Divider(color="#00FF00"),
                    chat_messages,
                    ft.Row([
                        ft.IconButton(ft.icons.MIC, icon_color="#00FF00"),
                        ft.IconButton(ft.icons.ATTACH_FILE, icon_color="#00FF00"),
                        msg_input,
                        ft.IconButton(ft.icons.SEND, on_click=send_msg, icon_color="#00FF00")
                    ])
                ], bgcolor="#000000")
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    log("[SYSTEM]: Ожидание авторизации...")

ft.app(target=main)
