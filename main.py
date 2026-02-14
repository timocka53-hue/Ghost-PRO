import flet as ft
import pyrebase

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
    page.padding = 15

    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=280)
    
    def log(msg, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {msg}", color=color, font_family="monospace"))
        page.update()

    reg_user = ft.TextField(label="USER_NAME", border_color="#00FF00", color="#00FF00")
    reg_email = ft.TextField(label="EMAIL", border_color="#00FF00", color="#00FF00")
    reg_pass = ft.TextField(label="PASSWORD", password=True, border_color="#00FF00", color="#00FF00")

    def login_click(e):
        if reg_email.value == "adminpan" and reg_pass.value == "TimaIssam2026":
            page.go("/chat")
            return
        try:
            auth.sign_in_with_email_and_password(reg_email.value, reg_pass.value)
            page.go("/chat")
        except:
            log("ERROR: ACCESS DENIED", "red")

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_OS: TERMINAL", color="#00FF00", size=20),
                    ft.Container(content=terminal, border=ft.border.all(1, "#00FF00"), padding=10),
                    reg_user, reg_email, reg_pass,
                    ft.ElevatedButton("LOG_IN", on_click=login_click, bgcolor="#228822", color="white", width=page.width)
                ])
            )
        elif page.route == "/chat":
            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_CHAT"), bgcolor="#001100"),
                    ft.Text("CHAT_INTERFACE_ACTIVE", color="#00FF00")
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    log("[SYSTEM]: READY_TO_LINK")

ft.app(target=main)
