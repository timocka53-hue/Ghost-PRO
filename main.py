import flet as ft
import pyrebase
import random

# КОНФИГ ИЗ ТВОЕГО google-services.json
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

def main(page: ft.Page):
    page.title = "Ghost PRO"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.fonts = {"Courier": "monospace"}
    
    # Хранилище сессии
    user_data = {"uid": None, "is_admin": False}

    # Виджет терминала (как в твоем дизайне)
    terminal = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        height=300,
        controls=[ft.Text("[SYSTEM]: Ожидание авторизации...", color="#00FF00", font_family="Courier")]
    )

    def log_to_terminal(text, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {text}", color=color, font_family="Courier"))
        page.update()

    def handle_auth(e):
        email = email_input.value
        password = pass_input.value
        
        # Проверка на Админ-панель (как ты просил)
        if email == "adminpan" and password == "TimaIssam2026":
            log_to_terminal("ДОСТУП В АДМИН-ПАНЕЛЬ РАЗРЕШЕН", color="yellow")
            user_data["is_admin"] = True
            page.go("/admin")
            return

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            user_data["uid"] = user['localId']
            log_to_terminal("АВТОРИЗАЦИЯ УСПЕШНА. ВХОД...")
            page.go("/chat")
        except:
            log_to_terminal("ОШИБКА: ОТКАЗАНО В ДОСТУПЕ", color="red")

    # Поля ввода в стиле Terminal
    email_input = ft.TextField(
        label="EMAIL_ADDRESS", 
        border_color="#00FF00", 
        color="#00FF00", 
        bgcolor="#001100",
        font_family="Courier"
    )
    pass_input = ft.TextField(
        label="ACCESS_PASSWORD", 
        password=True, 
        can_reveal_password=True,
        border_color="#00FF00", 
        color="#00FF00", 
        bgcolor="#001100",
        font_family="Courier"
    )

    def route_change(route):
        page.views.clear()
        
        # ГЛАВНЫЙ ЭКРАН (Твой дизайн с кнопками)
        page.views.append(
            ft.View("/", [
                ft.Text("GHOST_OS: ENCRYPTED_LINK", color="#00FF00", size=12, font_family="Courier"),
                ft.Container(
                    content=terminal,
                    border=ft.border.all(1, "#00FF00"),
                    padding=10,
                    bgcolor="#000A00"
                ),
                ft.VerticalDivider(height=10, opacity=0),
                email_input,
                pass_input,
                ft.ElevatedButton(
                    "REGISTRATION", 
                    on_click=lambda _: log_to_terminal("ЗАПУСК РЕГИСТРАЦИИ..."),
                    bgcolor="#55FF55", color="#000000", width=400
                ),
                ft.ElevatedButton(
                    "LOG_IN", 
                    on_click=handle_auth,
                    bgcolor="#228822", color="#FFFFFF", width=400
                ),
            ])
        )

        # ЭКРАН ЧАТА
        if page.route == "/chat":
            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("GHOST_MESSENGER"), bgcolor="#001100", color="#00FF00"),
                    ft.Text("Зашифрованный канал связи активен", color="#00FF00"),
                    ft.ListView(expand=True, spacing=10),
                    ft.Row([
                        ft.TextField(expand=True, border_color="#00FF00"),
                        ft.IconButton(ft.icons.SEND, icon_color="#00FF00")
                    ])
                ], bgcolor="#000000")
            )

        # АДМИН-ПАНЕЛЬ
        if page.route == "/admin":
            page.views.append(
                ft.View("/admin", [
                    ft.AppBar(title=ft.Text("ADMIN_SYSTEM_V2"), bgcolor="yellow", color="black"),
                    ft.Text("УПРАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯМИ", size=20, color="yellow"),
                    ft.ElevatedButton("ПОЛУЧИТЬ ЛОГИ СИСТЕМЫ", bgcolor="grey"),
                    ft.ElevatedButton("ЗАБЛОКИРОВАТЬ ID", bgcolor="red", color="white"),
                    ft.TextButton("ВЫХОД", on_click=lambda _: page.go("/"))
                ], bgcolor="#000000")
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
