import flet as ft
import random
import time

def main(page: ft.Page):
    page.title = "GHOST PRO V6"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    page.padding = 20
    page.spacing = 0

    # Переменные состояния
    user_data = {"email": "", "uid": "@guest", "is_admin": False}

    # --- КОМПОНЕНТЫ ДИЗАЙНА ---
    
    def ghost_input(label, password=False, icon=ft.icons.LOCK_OUTLINE):
        return ft.TextField(
            label=label,
            password=password,
            can_reveal_password=True,
            border_color="#00FF00",
            color="#00FF00",
            focused_border_color="#00FF00",
            prefix_icon=icon,
            text_size=14,
            height=60,
        )

    def ghost_button(text, on_click, color="#00FF00", bgcolor="#002200"):
        return ft.Container(
            content=ft.Text(text, color=color, weight="bold", size=14),
            on_click=on_click,
            alignment=ft.alignment.center,
            bgcolor=bgcolor,
            border=ft.border.all(1, color),
            height=50,
            border_radius=0,
            animate=ft.animation.Animation(300, "decelerate"),
        )

    # --- ЛОГИКА ПЕРЕКЛЮЧЕНИЯ ЭКРАНОВ ---
    def show_screen(screen_name):
        page.clean()
        if screen_name == "auth":
            page.add(auth_view)
        elif screen_name == "2fa":
            page.add(twofa_view)
        elif screen_name == "chat":
            page.add(chat_view)
        elif screen_name == "admin":
            page.add(admin_view)
        elif screen_name == "profile":
            page.add(profile_view)
        page.update()

    # --- ЭКРАН 1: АВТОРИЗАЦИЯ И РЕГИСТРАЦИЯ ---
    email_inp = ghost_input("ENTER_EMAIL", icon=ft.icons.EMAIL_OUTLINED)
    pass_inp = ghost_input("ENTER_PASSWORD", password=True)

    def start_auth(e):
        if not email_inp.value or not pass_inp.value:
            return
        user_data["email"] = email_inp.value
        # Скрытый вход для админа
        if email_inp.value == "adminpan" and pass_inp.value == "TimaIssam2026":
            user_data["is_admin"] = True
            user_data["uid"] = "@ADMIN_CORE"
            show_screen("chat") # Админ заходит без 2FA
        else:
            show_screen("2fa")

    auth_view = ft.Column([
        ft.Container(height=50),
        ft.Text("GHOST_PRO_V6", size=40, color="#00FF00", weight="bold", letter_spacing=10),
        ft.Text("ENCRYPTED NETWORK ACCESS", size=10, color="#00FF00", opacity=0.5),
        ft.Container(height=40),
        email_inp,
        ft.Container(height=10),
        pass_inp,
        ft.Container(height=20),
        ghost_button("INITIALIZE_SESSION", start_auth),
        ft.Row([ft.Text("VERIFICATION: ACTIVE", size=9, color="#00FF00")], alignment=ft.MainAxisAlignment.CENTER)
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # --- ЭКРАН 2: 2FA И ПОЧТА ---
    code_2fa = ghost_input("CONFIRMATION_CODE", icon=ft.icons.SECURITY)

    def verify_2fa(e):
        user_data["uid"] = "@" + user_data["email"].split("@")[0]
        show_screen("chat")

    twofa_view = ft.Column([
        ft.Text("2FA_VERIFICATION", size=20, color="#00FF00", weight="bold"),
        ft.Text(f"CODE SENT TO: {user_data['email']}", size=10, color="#00FF00"),
        ft.Container(height=20),
        code_2fa,
        ghost_button("VERIFY_IDENTITY", verify_2fa),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # --- ЭКРАН 3: ЧАТ И ПОИСК ---
    chat_list = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    msg_inp = ft.TextField(hint_text="Type payload...", border_color="#004400", expand=True, color="#00FF00")

    def send_msg(e):
        if not msg_inp.value: return
        chat_list.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(user_data["uid"], size=10, color=ft.colors.BLUE_400, weight="bold"),
                    ft.Text(msg_inp.value, color="#00FF00", size=14)
                ]),
                border=ft.border.only(left=ft.BorderSide(2, "#00FF00")),
                padding=ft.padding.only(left=10)
            )
        )
        msg_inp.value = ""
        page.update()

    chat_view = ft.Column([
        ft.Row([
            ft.Text("GHOST_NET", color="#00FF00", weight="bold"),
            ft.Row([
                ft.IconButton(ft.icons.ADMIN_PANEL_SETTINGS, icon_color="red", visible=user_data["is_admin"], on_click=lambda _: show_screen("admin")),
                ft.IconButton(ft.icons.PERSON, icon_color="#00FF00", on_click=lambda _: show_screen("profile")),
            ])
        ], justify=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.TextField(hint_text="SEARCH_UID (@user...)", prefix_icon=ft.icons.SEARCH, border_color="#004400", height=40),
        ft.Container(content=chat_list, expand=True, border=ft.border.all(1, "#002200"), padding=10, bgcolor="#050505"),
        ft.Row([
            ft.IconButton(ft.icons.MIC, icon_color="#00FF00", on_click=lambda _: page.show_snack_bar(ft.SnackBar(ft.Text("REC_AUDIO...")))),
            ft.IconButton(ft.icons.VIDEOCAM, icon_color="#00FF00", on_click=lambda _: page.show_snack_bar(ft.SnackBar(ft.Text("REC_VIDEO...")))),
            msg_inp,
            ft.IconButton(ft.icons.SEND, icon_color="#00FF00", on_click=send_msg),
        ])
    ], expand=True)

    # --- ЭКРАН 4: АДМИНКА (GOD MODE) ---
    admin_view = ft.Column([
        ft.Row([ft.Text("CORE_CONTROL", size=20, color="red", weight="bold"), ft.IconButton(ft.icons.CLOSE, on_click=lambda _: show_screen("chat"))], justify=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Divider(color="red"),
        ft.GridView([
            ghost_button("BAN_USER", lambda _: None, color="red"),
            ghost_button("FREEZE_NET", lambda _: None, color="red"),
            ghost_button("BROADCAST", lambda _: None, color="red"),
            ghost_button("WIPE_LOGS", lambda _: None, color="red"),
        ], runs_count=2, spacing=10, height=120),
        ft.Text("ACTIVE_TICKETS:", size=12, color="red"),
        ft.ListView(expand=True, controls=[
            ft.ListTile(title=ft.Text("FROM: @user_777", color="white"), subtitle=ft.Text("I need help with login", color="gray"), trailing=ft.TextButton("REPLY", on_click=lambda _: show_screen("chat")))
        ])
    ], expand=True)

    # --- ЭКРАН 5: ПРОФИЛЬ ---
    def change_avatar(e):
        page.show_snack_bar(ft.SnackBar(ft.Text("ACCESSING GALLERY...")))

    profile_view = ft.Column([
        ft.Container(height=20),
        ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON, size=60), radius=60, bgcolor="#002200"),
        ft.TextButton("CHANGE_AVATAR", on_click=change_avatar),
        ft.Text(user_data["uid"], size=24, color="#00FF00", weight="bold"),
        ft.Container(height=20),
        ghost_button("CONTACT_TECH_SUPPORT", lambda _: page.show_snack_bar(ft.SnackBar(ft.Text("TICKET_CREATED")))),
        ghost_button("LOGOUT", lambda _: show_screen("auth"), color="red"),
        ft.TextButton("BACK_TO_NETWORK", on_click=lambda _: show_screen("chat"))
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # Запуск
    show_screen("auth")

ft.app(target=main)
