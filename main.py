import flet as ft
import time

# --- БЕЗОПАСНАЯ ЗАГРУЗКА КРИПТОГРАФИИ ---
try:
    from cryptography.fernet import Fernet
    # Ключ генерируем прямо в коде, чтобы точно не было ValueError
    cipher_key = Fernet.generate_key()
    cipher = Fernet(cipher_key)
    CRYPTO_STATUS = "ACTIVE"
except Exception as e:
    CRYPTO_STATUS = f"ERROR: {str(e)}"
    cipher = None

def main(page: ft.Page):
    # Настройки страницы
    page.title = "GHOST PRO V4"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # 1. СРАЗУ ПОКАЗЫВАЕМ ИНТЕРФЕЙС (Защита от черного экрана)
    log_text = ft.Text(f"SYSTEM_STATUS: {CRYPTO_STATUS}", color="#00FF00", font_family="monospace")
    
    email_f = ft.TextField(label="IDENTIFIER", border_color="#00FF00", width=350, color="#00FF00")
    pass_f = ft.TextField(label="ACCESS_KEY", password=True, border_color="#00FF00", width=350, color="#00FF00")

    def handle_login(e):
        # ТВОЯ АДМИНКА
        if email_f.value == "adminpan" and pass_f.value == "TimaIssam2026":
            page.go("/chat")
        else:
            log_text.value = "LOGIN_FAILED: UNKNOWN_ID"
            page.update()

    # --- ЭКРАНЫ ПРИЛОЖЕНИЯ ---
    def route_change(route):
        page.views.clear()
        
        # ЭКРАН ВХОДА
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_PRO_OS", color="#00FF00", size=35, weight="bold"),
                    log_text,
                    ft.Divider(color="transparent", height=20),
                    email_f,
                    pass_f,
                    ft.ElevatedButton("INITIALIZE", on_click=handle_login, bgcolor="#114411", color="white", width=350)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, vertical_alignment=ft.MainAxisAlignment.CENTER)
            )
        
        # ЭКРАН ЧАТА
        elif page.route == "/chat":
            chat_messages = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            msg_input = ft.TextField(placeholder="Encrypted data...", expand=True, border_color="#00FF00")

            def send_click(e):
                if msg_input.value:
                    chat_messages.controls.append(ft.Text(f"LOG: {msg_input.value}", color="#00FF00"))
                    msg_input.value = ""
                    page.update()

            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(
                        title=ft.Text("GHOST_NETWORK"), 
                        bgcolor="#001100", 
                        actions=[ft.IconButton(ft.icons.PERSON, on_click=lambda _: page.go("/profile"))]
                    ),
                    ft.TextField(label="SEARCH_USER", prefix_icon=ft.icons.SEARCH, border_color="#00FF00"),
                    chat_messages,
                    ft.Row([
                        ft.IconButton(ft.icons.MIC, icon_color="#00FF00"),
                        msg_input,
                        ft.IconButton(ft.icons.SEND, on_click=send_click, icon_color="#00FF00")
                    ])
                ])
            )

        # ЭКРАН ПРОФИЛЯ
        elif page.route == "/profile":
            page.views.append(
                ft.View("/profile", [
                    ft.AppBar(title=ft.Text("USER_PROFILE"), bgcolor="#001100"),
                    ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON), radius=50),
                    ft.Text("@ADMIN_PRO", color="#00FF00", size=20),
                    ft.ElevatedButton("ТЕХ.ПОДДЕРЖКА", on_click=lambda _: page.go("/support")),
                    ft.ElevatedButton("НАЗАД", on_click=lambda _: page.go("/chat"))
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )

        # ТЕХ ПОДДЕРЖКА
        elif page.route == "/support":
            page.views.append(
                ft.View("/support", [
                    ft.AppBar(title=ft.Text("SUPPORT_TICKET")),
                    ft.TextField(label="ОПИШИТЕ ПРОБЛЕМУ", multiline=True, min_lines=5),
                    ft.ElevatedButton("ОТПРАВИТЬ АДМИНУ", on_click=lambda _: page.go("/chat"))
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
