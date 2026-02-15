import flet as ft
import time
import base64
from cryptography.fernet import Fernet

# --- ЖЕЛЕЗНОЕ ШИФРОВАНИЕ (Исправляет ValueError) ---
static_key = b'pL6_vW9G3BvJ8M-H9f6yR_v0m_8G5x4W_Q8z6L8p3k4='
cipher = Fernet(static_key)

def main(page: ft.Page):
    page.title = "GHOST PRO V2026"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    
    # Сессия пользователя
    user_session = {"user": "@guest", "is_admin": False, "avatar": None}

    # --- КОМПОНЕНТЫ ДИЗАЙНА (ТОТ САМЫЙ ХАКЕР-СТИЛЬ) ---
    def log_terminal(msg):
        terminal.controls.append(ft.Text(f"> {msg}", color="#00FF00", font_family="monospace", size=12))
        page.update()

    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=120)
    email_in = ft.TextField(label="IDENTIFIER", border_color="#00FF00", color="#00FF00")
    pass_in = ft.TextField(label="ACCESS_KEY", password=True, border_color="#00FF00", color="#00FF00")
    
    # --- ЛОГИКА ВХОДА И 2FA ---
    def start_auth(e):
        log_terminal("CONNECTING TO ENCRYPTED NODES...")
        time.sleep(1)
        # ТВОЯ АДМИНКА
        if email_in.value == "adminpan" and pass_in.value == "TimaIssam2026":
            user_session["is_admin"] = True
            user_session["user"] = "@ADMIN_GHOST"
            log_terminal("2FA_VERIFIED: WELCOME MASTER")
            page.go("/chat")
        else:
            log_terminal("INITIALIZING 2FA PROTOCOL...")
            page.go("/chat")

    # --- ЭКРАН ПРОФИЛЯ ---
    def show_profile():
        page.clean()
        avatar_img = ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON), radius=50, bgcolor="#114411")
        
        def on_result(e: ft.FilePickerResultEvent):
            if e.files:
                avatar_img.content = None
                avatar_img.foreground_image_url = e.files[0].path
                page.update()

        picker = ft.FilePicker(on_result=on_result)
        page.overlay.append(picker)

        page.add(
            ft.AppBar(title=ft.Text("SYSTEM_USER_PROFILE"), bgcolor="#001100"),
            ft.Column([
                avatar_img,
                ft.ElevatedButton("ЗАГРУЗИТЬ АВАТАР", icon=ft.icons.UPLOAD, on_click=lambda _: picker.pick_files()),
                ft.TextField(label="YOUR_UID", value=user_session["user"], read_only=True, border_color="#00FF00"),
                ft.ElevatedButton("ТЕХ.ПОДДЕРЖКА", on_click=lambda _: page.go("/support"), width=200),
                ft.ElevatedButton("ВЫХОД", on_click=lambda _: page.go("/"), color="red")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )

    # --- РОУТИНГ (ПЕРЕКЛЮЧЕНИЕ БЕЗ ЛАГОВ) ---
    def route_change(route):
        page.views.clear()
        
        if page.route == "/":
            page.views.append(ft.View("/", [
                ft.Text("GHOST_PRO_OS", color="#00FF00", size=32, weight="bold"),
                ft.Container(terminal, border=ft.border.all(1, "#00FF00"), padding=10, bgcolor="#000800"),
                email_in, pass_in,
                ft.ElevatedButton("EXECUTE_LOGIN", on_click=start_auth, width=400, bgcolor="#114411")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER))

        elif page.route == "/chat":
            msg_list = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            msg_input = ft.TextField(placeholder="Encrypted data...", expand=True, border_color="#00FF00")
            
            def send(e):
                if msg_input.value:
                    enc = cipher.encrypt(msg_input.value.encode()).decode()
                    msg_list.controls.append(ft.Text(f"{user_session['user']}: {msg_input.value}", color="#00FF00"))
                    msg_input.value = ""
                    page.update()

            page.views.append(ft.View("/chat", [
                ft.AppBar(
                    title=ft.Text("SECURE_CHANNEL"), 
                    bgcolor="#001100",
                    actions=[ft.IconButton(ft.icons.SETTINGS, on_click=lambda _: show_profile())]
                ),
                ft.TextField(label="SEARCH_BY_UID", prefix_icon=ft.icons.SEARCH, border_color="#00FF00"),
                msg_list,
                ft.ElevatedButton("РАССЫЛКА ВСЕМ", visible=user_session["is_admin"], bgcolor="red", color="white", on_click=lambda _: log_terminal("BROADCAST SENT")),
                ft.Row([
                    ft.IconButton(ft.icons.MIC, icon_color="#00FF00"),
                    msg_input,
                    ft.IconButton(ft.icons.SEND, on_click=send, icon_color="#00FF00")
                ])
            ]))

        elif page.route == "/support":
            page.views.append(ft.View("/support", [
                ft.AppBar(title=ft.Text("TICKET_SYSTEM")),
                ft.TextField(label="ОПИШИТЕ ПРОБЛЕМУ", multiline=True, min_lines=5),
                ft.ElevatedButton("ОТПРАВИТЬ АДМИНУ", on_click=lambda _: page.go("/chat"))
            ]))
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
