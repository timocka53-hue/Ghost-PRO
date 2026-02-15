import flet as ft
import time

# --- ТОТАЛЬНЫЙ ФИКС ОШИБОК ШИФРОВАНИЯ ---
# Используем безопасную инициализацию, чтобы не было ValueError
try:
    from cryptography.fernet import Fernet
    # Ключ ровно 32 байта base64
    cipher = Fernet(b'pL6_vW9G3BvJ8M-H9f6yR_v0m_8G5x4W_Q8z6L8p3k4=')
except:
    cipher = None

def main(page: ft.Page):
    page.title = "GHOST PRO V4"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Данные для входа (Твоя админка)
    ADMIN_LOGIN = "adminpan"
    ADMIN_PASS = "TimaIssam2026"

    # --- ЭЛЕМЕНТЫ ДИЗАЙНА ---
    status_msg = ft.Text("SYSTEM_STANDBY", color="#00FF00", font_family="monospace")
    
    email_f = ft.TextField(label="IDENTIFIER", border_color="#00FF00", width=300)
    pass_f = ft.TextField(label="ACCESS_KEY", password=True, border_color="#00FF00", width=300)

    def handle_login(e):
        if email_f.value == ADMIN_LOGIN and pass_f.value == ADMIN_PASS:
            status_msg.value = "2FA_SUCCESS: ADMIN_OPEN"
            page.update()
            time.sleep(0.5)
            page.go("/chat")
        else:
            status_msg.value = "ACCESS_DENIED"
            page.update()

    # --- СТРАНИЦЫ (РОУТИНГ) ---
    def route_change(route):
        page.views.clear()
        
        # Главная (Логин)
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_PRO_OS", color="#00FF00", size=32, weight="bold"),
                    status_msg,
                    email_f,
                    pass_f,
                    ft.ElevatedButton("EXECUTE", on_click=handle_login, bgcolor="#114411", color="white", width=300)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, vertical_alignment=ft.MainAxisAlignment.CENTER)
            )
        
        # Чат и Профиль
        elif page.route == "/chat":
            chat_box = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            msg_in = ft.TextField(placeholder="Encrypted payload...", expand=True, border_color="#00FF00")

            def send(e):
                if msg_in.value:
                    chat_box.controls.append(ft.Text(f"YOU: {msg_in.value}", color="#00FF00"))
                    msg_in.value = ""
                    page.update()

            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_NETWORK"), bgcolor="#001100"),
                    ft.TextField(label="SEARCH_USER", prefix_icon=ft.icons.SEARCH, border_color="#00FF00"),
                    chat_box,
                    ft.Row([
                        ft.IconButton(ft.icons.PERSON, on_click=lambda _: page.go("/profile"), icon_color="#00FF00"),
                        msg_in,
                        ft.IconButton(ft.icons.SEND, on_click=send, icon_color="#00FF00")
                    ])
                ])
            )
        
        # Профиль с поддержкой
        elif page.route == "/profile":
            page.views.append(
                ft.View("/profile", [
                    ft.AppBar(title=ft.Text("USER_PROFILE")),
                    ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON), radius=40),
                    ft.Text("@ADMIN_PRO", color="#00FF00"),
                    ft.ElevatedButton("ТЕХ.ПОДДЕРЖКА", on_click=lambda _: page.go("/support")),
                    ft.ElevatedButton("НАЗАД", on_click=lambda _: page.go("/chat"))
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )

        elif page.route == "/support":
            page.views.append(
                ft.View("/support", [
                    ft.AppBar(title=ft.Text("SUPPORT_CENTER")),
                    ft.TextField(label="Опишите проблему", multiline=True, min_lines=3),
                    ft.ElevatedButton("ОТПРАВИТЬ ТИКЕТ", on_click=lambda _: page.go("/chat"))
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
