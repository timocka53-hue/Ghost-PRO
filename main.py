import flet as ft
import pyrebase

# Твой конфиг из google-services.json
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
    page.padding = 15

    # --- ЭЛЕМЕНТ ТЕРМИНАЛА ---
    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=280)
    
    def log(msg, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {msg}", color=color, font_family="monospace", size=14))
        page.update()

    # --- ПОЛЯ ВВОДА ---
    reg_user = ft.TextField(label="USER_NAME", border_color="#00FF00", color="#00FF00")
    reg_email = ft.TextField(label="EMAIL", border_color="#00FF00", color="#00FF00")
    reg_pass = ft.TextField(label="PASSWORD", password=True, border_color="#00FF00", color="#00FF00")

    def login_click(e):
        # Твой админский вход
        if reg_email.value == "adminpan" and reg_pass.value == "TimaIssam2026":
            log("ADMIN ACCESS GRANTED", "yellow")
            page.go("/chat")
            return
        try:
            auth.sign_in_with_email_and_password(reg_email.value, reg_pass.value)
            log("SUCCESS: LINK ESTABLISHED")
            page.go("/chat")
        except:
            log("ERROR: ACCESS DENIED", "red")

    def route_change(route):
        page.views.clear()
        # ГЛАВНЫЙ ЭКРАН (Твой дизайн)
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_OS: TERMINAL_BOOT", color="#00FF00", size=20, weight="bold"),
                    ft.Container(content=terminal, border=ft.border.all(1, "#00FF00"), padding=10, bgcolor="#000A00"),
                    reg_user, reg_email, reg_pass,
                    ft.Row([
                        ft.ElevatedButton("LOG_IN", on_click=login_click, bgcolor="#228822", color="white", expand=True),
                    ])
                ])
            )
        # ЭКРАН ЧАТА
        elif page.route == "/chat":
            chat_box = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            msg_input = ft.TextField(placeholder="TYPE_MESSAGE...", expand=True, border_color="#00FF00")
            
            def send(e):
                if msg_input.value:
                    chat_box.controls.append(ft.Text(f"Ghost: {msg_input.value}", color="#00FF00"))
                    msg_input.value = ""
                    page.update()

            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_MESSENGER"), bgcolor="#001100", color="#00FF00"),
                    chat_box,
                    ft.Row([msg_input, ft.IconButton(ft.icons.SEND, on_click=send, icon_color="#00FF00")])
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    log("[SYSTEM]: ОЖИДАНИЕ ВХОДА В СЕТЬ...")

ft.app(target=main)
