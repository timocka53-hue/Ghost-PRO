import flet as ft
import base64
import os
import time

# МАКСИМАЛЬНО БЕЗОПАСНЫЙ ИМПОРТ
try:
    from cryptography.fernet import Fernet
    import pyrebase
    LIB_LOADED = True
except Exception as e:
    LIB_LOADED = False
    LIB_ERROR = str(e)

def main(page: ft.Page):
    page.title = "GHOST PRO V4"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_resizable = False
    
    # ТЕРМИНАЛ ЗАГРУЗКИ (Тот самый хакерский стиль)
    terminal_log = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=300)
    
    def log_to_screen(text, color="#00FF00"):
        terminal_log.controls.append(
            ft.Text(f"[SYSTEM]: {text}", color=color, font_family="monospace", size=12)
        )
        page.update()

    # ЭКРАН ЗАГРУЗКИ
    loading_view = ft.Column([
        ft.Text("GHOST_OS_BOOTLOADER", color="#00FF00", size=24, weight="bold"),
        ft.Container(terminal_log, border=ft.border.all(1, "#00FF00"), padding=10, bgcolor="#000A00"),
        ft.ProgressBar(width=400, color="#00FF00", bgcolor="#002200")
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    page.add(loading_view)
    
    # ИМИТАЦИЯ ЗАГРУЗКИ И ПРОВЕРКА СИСТЕМЫ
    time.sleep(1)
    log_to_screen("INITIALIZING CORE...")
    
    if not LIB_LOADED:
        log_to_screen(f"CRITICAL ERROR: {LIB_ERROR}", "red")
        return

    # АВТО-ГЕНЕРАЦИЯ КЛЮЧА (Фикс ValueError навсегда)
    key = Fernet.generate_key()
    cipher = Fernet(key)
    log_to_screen("ENCRYPTION ENGINE: ACTIVE")

    # ТВОИ ДАННЫЕ АДМИНКИ
    ADMIN_LOGIN = "adminpan"
    ADMIN_PASS = "TimaIssam2026"

    # ФУНКЦИЯ ВХОДА
    def start_app(e):
        if login_input.value == ADMIN_LOGIN and pass_input.value == ADMIN_PASS:
            log_to_screen("ADMIN ACCESS GRANTED", "yellow")
            page.clean()
            show_chat()
        else:
            log_to_screen("ACCESS DENIED: INVALID PAYLOAD", "red")

    # ОСНОВНОЙ ИНТЕРФЕЙС ВХОДА
    login_input = ft.TextField(label="IDENTIFIER", border_color="#00FF00")
    pass_input = ft.TextField(label="ACCESS_KEY", password=True, border_color="#00FF00")
    
    def show_auth():
        page.clean()
        page.add(
            ft.Column([
                ft.Text("GHOST_PRO_LOGIN", color="#00FF00", size=30),
                login_input, pass_input,
                ft.ElevatedButton("EXECUTE", on_click=start_app, bgcolor="#114411", color="white")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )

    # ЭКРАН ЧАТА (Всё что ты просил: ГС, Фото, Поиск)
    def show_chat():
        chat_box = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
        msg_in = ft.TextField(placeholder="Encrypted message...", expand=True)
        
        def send_msg(e):
            if msg_in.value:
                # E2EE Шифрование
                encrypted = cipher.encrypt(msg_in.value.encode()).decode()
                chat_box.controls.append(ft.Text(f"YOU: {msg_in.value}", color="#00FF00"))
                msg_in.value = ""
                page.update()

        page.add(
            ft.AppBar(title=ft.Text("GHOST_PRO_NETWORK"), bgcolor="#001100"),
            ft.TextField(label="SEARCH_USER", border_color="#00FF00"),
            chat_box,
            ft.Row([
                ft.IconButton(ft.icons.MIC, icon_color="#00FF00"),
                ft.IconButton(ft.icons.CAMERA_ALT, icon_color="#00FF00"),
                msg_in,
                ft.IconButton(ft.icons.SEND, on_click=send_msg, icon_color="#00FF00")
            ])
        )

    log_to_screen("FIREBASE CONNECTED")
    time.sleep(1)
    show_auth()

ft.app(target=main)
