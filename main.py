import flet as ft
import os

def main(page: ft.Page):
    page.title = "GHOST PRO ULTIMATE"
    page.padding = 0
    path = os.path.abspath("index.html")
    wv = ft.WebView(f"file://{path}", expand=True)
    page.add(wv)

ft.app(target=main)
