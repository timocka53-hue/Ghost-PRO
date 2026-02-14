import flet as ft
import pyrebase
import requests
import cryptography
from cryptography.fernet import Fernet
import time

# КОРРЕКТНЫЙ КЛЮЧ (32 байта base64) - Исправляет твою прошлую ошибку!
cipher_key = b'pL6_vW9G3BvJ8M-H9f6yR_v0m_8G5x4W_Q8z6L8p3k4='
cipher = Fernet(cipher_key)

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
    page.title = "Ghost PRO Ultra"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    
    # ЭКРАН ЗАГРУЗКИ (Чтобы не было черного экрана)
    loading_text = ft.Text("GHOST_OS: BOOTING...", color="#00FF00", size=20, font_family="monospace")
    progress_bar = ft.ProgressBar(width=400, color="#00FF00", bgcolor="#002200")
    
    status_container = ft.Column([loading_text, progress_bar], alignment=ft.MainAxisAlignment.CENTER)
    page.add(ft.Container(status_container, expand=True, content=status_container, alignment=ft.alignment.center))
    
    time.sleep(1) # Даем системе прогрузить интерфейс
    
    try:
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        loading_text.value = "GHOST_OS: ALL SYSTEMS ONLINE"
        page.update()
    except Exception as e:
        loading_text.value = f"CRITICAL ERROR: {str(e)}"
        loading_text.color = "red"
        page.update()
        return

    # Данные юзера
    user_session = {"name": "Anonymous"}

    # ЭЛЕМЕНТЫ ИНТЕРФЕЙСА
    email_in = ft.TextField(label="LOGIN / ADMIN", border_color="#00FF00", color="#00FF00")
    pass_in = ft.TextField(label="PASSWORD", password=True, border_color="#00FF00", color="#00FF00")
    
    def login_dev(e):
        # ТВОЯ АДМИНКА
        if email_in.value == "adminpan" and pass_in.value == "TimaIssam2026":
            user_session["name"] = "ADMIN_GHOST"
            page.go("/chat")
        else:
            try:
                auth.sign_in_with_email_and_password(email_in.value, pass_in.value)
                page.go("/chat")
            except:
                loading_text.value = "ACCESS DENIED"
                page.update()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.AppBar(title=ft.Text("GHOST_OS"), bgcolor="#001100"),
                    ft.Text("ENTER CREDENTIALS", color="#00FF00"),
                    email_in, pass_in,
                    ft.ElevatedButton("INITIALIZE", on_click=login_dev, bgcolor="#115511")
                ])
            )
        elif page.route == "/chat":
            chat_col = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
            msg_in = ft.TextField(placeholder="Encrypted data...", expand=True)
            
            def send_encrypted(e):
                if msg_in.value:
                    enc = cipher.encrypt(msg_input.value.encode()).decode()
                    db.child("messages").push({"u": user_session["name"], "m": enc})
                    chat_col.controls.append(ft.Text(f"YOU: {msg_in.value}", color="#00FF00"))
                    msg_in.value = ""
                    page.update()

            page.views.append(
                ft.View("/chat", [
                    ft.AppBar(title=ft.Text("SECURE_CHANNEL"), bgcolor="#001100"),
                    ft.TextField(label="SEARCH_USER", border_color="#00FF00"),
                    chat_col,
                    ft.Row([
                        ft.IconButton(ft.icons.MIC, icon_color="#00FF00"),
                        ft.IconButton(ft.icons.ATTACH_FILE, icon_color="#00FF00"),
                        msg_in,
                        ft.IconButton(ft.icons.SEND, on_click=send_encrypted, icon_color="#00FF00")
                    ])
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
