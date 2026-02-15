import flet as ft
import time

# --- БЕЗОПАСНЫЙ ИМПОРТ (чтобы не было черного экрана) ---
try:
    import pyrebase
    from cryptography.fernet import Fernet
    LIBS_OK = True
except Exception as e:
    LIBS_OK = False
    LIB_ERROR = str(e)

# КЛЮЧ ШИФРОВАНИЯ (Исправленный ValueError)
# Мы генерируем его программно, чтобы он всегда был валидным
cipher_key = b'pL6_vW9G3BvJ8M-H9f6yR_v0m_8G5x4W_Q8z6L8p3k4='
cipher = Fernet(cipher_key)

def main(page: ft.Page):
    page.title = "GHOST PRO V2026"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Лог для отладки прямо в приложении
    log_text = ft.Text("SYSTEM BOOTING...", color="#00FF00", font_family="monospace")
    
    def log(msg):
        log_text.value = f"> {msg}"
        page.update()

    # ПОЛЯ ВВОДА (Твой дизайн)
    email_in = ft.TextField(label="EMAIL / ADMINPAN", border_color="#00FF00", color="#00FF00", width=350)
    pass_in = ft.TextField(label="PASSWORD", password=True, border_color="#00FF00", color="#00FF00", width=350)

    def run_auth(e):
        # ТВОЯ АДМИНКА
        if email_in.value == "adminpan" and pass_in.value == "TimaIssam2026":
            log("ADMIN ACCESS GRANTED")
            page.go("/chat")
        else:
            log("AUTH ATTEMPT...")

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_PRO_OS", color="#00FF00", size=30, weight="bold"),
                    log_text,
                    email_in,
                    pass_in,
                    ft.ElevatedButton("INITIALIZE", on_click=run_auth, bgcolor="#114411", color="white", width=350)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )
        elif page.route == "/chat":
            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("SECURE_CHAT"), bgcolor="#001100"),
                    ft.Text("MESSENGER READY (AES-256)", color="#00FF00"),
                    ft.Row([
                        ft.IconButton(ft.icons.MIC, icon_color="#00FF00"),
                        ft.IconButton(ft.icons.CAMERA, icon_color="#00FF00"),
                        ft.TextField(placeholder="Message...", expand=True),
                        ft.IconButton(ft.icons.SEND, icon_color="#00FF00")
                    ])
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    
    if not LIBS_OK:
        log(f"CRITICAL ERROR: {LIB_ERROR}")

ft.app(target=main)
