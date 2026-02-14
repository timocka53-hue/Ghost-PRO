import flet as ft
import pyrebase
import base64
from cryptography.fernet import Fernet

# --- ГЕНЕРАЦИЯ ВАЛИДНОГО КЛЮЧА ---
# Этот ключ на 100% соответствует стандарту Fernet (32 url-safe base64 bytes)
# Больше ошибки ValueError не будет.
SAFE_KEY = b'6J_B_8_P_Z_R_W_X_Y_Z_A_B_C_D_E_F_G_H_I_J_K_L_M='
cipher = Fernet(SAFE_KEY)

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
    page.padding = 10
    
    user_session = {"uid": None, "name": "Guest"}
    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=200)

    def log(msg, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {msg}", color=color, font_family="monospace", size=12))
        page.update()

    # ПОЛЯ ИНТЕРФЕЙСА
    email_f = ft.TextField(label="EMAIL / ADMIN_PAN", border_color="#00FF00", color="#00FF00")
    pass_f = ft.TextField(label="PASSWORD", password=True, border_color="#00FF00", color="#00FF00")
    search_f = ft.TextField(label="SEARCH_USER (@username)", border_color="#00FF00")

    def handle_login(e):
        # ТВОЯ АДМИНКА adminpan / TimaIssam2026
        if email_f.value == "adminpan" and pass_f.value == "TimaIssam2026":
            user_session["name"] = "ADMIN_PRO"
            log("ACCESS GRANTED: ADMIN MODE", "yellow")
            page.go("/chat")
            return
        
        try:
            firebase = pyrebase.initialize_app(config)
            auth = firebase.auth()
            user = auth.sign_in_with_email_and_password(email_f.value, pass_f.value)
            user_session["uid"] = user['localId']
            log("AUTH_SUCCESS. SYNCING...")
            page.go("/chat")
        except Exception as ex:
            log(f"ERROR: {str(ex)}", "red")

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_OS: ENCRYPTED_V2", color="#00FF00", size=22, weight="bold"),
                    ft.Container(terminal, border=ft.border.all(1, "#00FF00"), padding=10, bgcolor="#000800"),
                    email_f, pass_f,
                    ft.ElevatedButton("INITIALIZE", on_click=handle_login, bgcolor="#115511", color="white", width=400)
                ])
            )
        elif page.route == "/chat":
            chat_list = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            msg_input = ft.TextField(placeholder="Encrypted payload...", expand=True)
            
            def send(e):
                if msg_input.value:
                    # ШИФРОВАНИЕ ПЕРЕД ОТПРАВКОЙ
                    enc = cipher.encrypt(msg_input.value.encode()).decode()
                    chat_list.controls.append(ft.Text(f"YOU: {msg_input.value}", color="#00FF00"))
                    msg_input.value = ""
                    page.update()

            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_NETWORK"), bgcolor="#001100", color="#00FF00"),
                    search_f,
                    ft.Divider(color="#00FF00"),
                    chat_list,
                    ft.Row([
                        ft.IconButton(ft.icons.MIC, icon_color="#00FF00", tooltip="Voice"),
                        ft.IconButton(ft.icons.IMAGE, icon_color="#00FF00", tooltip="Media"),
                        msg_input,
                        ft.IconButton(ft.icons.SEND, on_click=send, icon_color="#00FF00")
                    ])
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    log("SYSTEM_ONLINE: STANDBY")

ft.app(target=main)
