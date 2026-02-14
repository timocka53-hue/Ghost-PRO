import flet as ft
import pyrebase
import time

# Твой конфиг
config = {
    "apiKey": "AIzaSyAbiRCuR9egtHKg0FNzzBdL9dNqPqpPLNk",
    "authDomain": "ghost-pro-5aa22.firebaseapp.com",
    "databaseURL": "https://ghost-pro-5aa22-default-rtdb.firebaseio.com",
    "projectId": "ghost-pro-5aa22",
    "storageBucket": "ghost-pro-5aa22.firebasestorage.app",
    "messagingSenderId": "332879455079",
    "appId": "1:332879455079:android:15c36642c62d13e0dd05c2"
}

# Глобальные переменные для работы
firebase = None
auth = None
db = None
user_session = {"uid": None, "name": "Guest"}

def main(page: ft.Page):
    page.title = "Ghost PRO"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
    page.window_width = 400
    page.window_height = 800

    # Элемент ТЕРМИНАЛА (Лог)
    terminal = ft.Column(scroll=ft.ScrollMode.ALWAYS, height=250, spacing=5)
    
    def log(msg, color="#00FF00"):
        terminal.controls.append(ft.Text(f"> {msg}", color=color, font_family="monospace", size=12))
        page.update()

    # ПОПЫТКА ИНИЦИАЛИЗАЦИИ (Чтобы не было черного экрана при ошибке сети)
    global firebase, auth, db
    try:
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        log("SYSTEM: КАНАЛ СВЯЗИ Firebase УСТАНОВЛЕН")
    except Exception as e:
        log(f"CRITICAL ERROR: {str(e)}", "red")

    # Поля ввода
    user_field = ft.TextField(label="USER_NAME", border_color="#00FF00", color="#00FF00", focused_border_color="#55FF55")
    email_field = ft.TextField(label="EMAIL_ADDRESS", border_color="#00FF00", color="#00FF00")
    pass_field = ft.TextField(label="ACCESS_PASSWORD", password=True, can_reveal_password=True, border_color="#00FF00", color="#00FF00")

    # Функция регистрации и логина
    def start_session(e):
        if not email_field.value or not pass_field.value:
            log("ERROR: ПУСТЫЕ ПОЛЯ", "red")
            return
        
        # Админский вход без интернета (для тестов)
        if email_field.value == "adminpan" and pass_field.value == "TimaIssam2026":
            user_session["uid"] = "ADMIN"
            user_session["name"] = "ADMIN_PRO"
            page.go("/chat")
            return

        try:
            log("AUTHENTICATING...")
            user = auth.sign_in_with_email_and_password(email_field.value, pass_field.value)
            user_session["uid"] = user['localId']
            # Пытаемся взять имя из базы
            data = db.child("users").child(user['localId']).get().val()
            user_session["name"] = data.get("username", "Ghost") if data else "Ghost"
            page.go("/chat")
        except:
            log("FAILED: НЕВЕРНЫЙ ЛОГИН ИЛИ ПАРОЛЬ", "red")

    def register_new(e):
        try:
            user = auth.create_user_with_email_and_password(email_field.value, pass_field.value)
            db.child("users").child(user['localId']).set({"username": user_field.value})
            log(f"SUCCESS: АККАУНТ {user_field.value} СОЗДАН", "yellow")
        except Exception as ex:
            log(f"REG_ERROR: {str(ex)}", "red")

    # РОУТИНГ (Переключение экранов)
    def route_change(route):
        page.views.clear()
        
        # ГЛАВНЫЙ ЭКРАН (Твой дизайн)
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Text("GHOST_OS: V.2.0.4", color="#00FF00", size=22, weight="bold"),
                    ft.Container(content=terminal, border=ft.border.all(1, "#00FF00"), padding=10, bgcolor="#000A00", border_radius=5),
                    user_field, email_field, pass_field,
                    ft.Row([
                        ft.ElevatedButton("LOG_IN", on_click=start_session, bgcolor="#228822", color="white", expand=True),
                        ft.ElevatedButton("CREATE", on_click=register_new, bgcolor="#004400", color="#00FF00", expand=True),
                    ])
                ])
            )
        
        # ЭКРАН ПОЛНОЦЕННОГО ЧАТА
        elif page.route == "/chat":
            chat_msg_list = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            msg_input = ft.TextField(placeholder="МЕССЕДЖ...", expand=True, border_color="#00FF00")
            
            def send_to_db(e):
                if msg_input.value:
                    # В реальном приложении тут будет db.child("messages").push(...)
                    chat_msg_list.controls.append(ft.Text(f"{user_session['name']}: {msg_input.value}", color="#00FF00"))
                    msg_input.value = ""
                    page.update()

            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text(f"GHOST_CHAT: {user_session['name']}"), bgcolor="#001100", color="#00FF00"),
                    chat_msg_list,
                    ft.Row([
                        ft.IconButton(ft.icons.IMAGE, icon_color="#00FF00"),
                        msg_input,
                        ft.IconButton(ft.icons.SEND, on_click=send_to_db, icon_color="#00FF00")
                    ])
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    log("[SYSTEM]: ОЖИДАНИЕ ВХОДА...")

ft.app(target=main)
