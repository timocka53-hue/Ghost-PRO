[app]
title = Ghost PRO
# Пакет из твоего google-services.json
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 8.0

# Добавляем кучу библиотек принудительно для веса
requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,certifi,urllib3,openssl,sqlite3

orientation = portrait
# Используем стабильный API 33 как в твоем проекте
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

# Иконка - проверь файл icon.png в репе!
icon.filename = icon.png
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.manifest.uses_cleartext_traffic = True
android.accept_sdk_license = True
android.presplash_color = #000000

[buildozer]
log_level = 2
warn_on_root = 1
