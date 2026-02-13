[app]
title = Ghost PRO
package.name = ghost.pro.messenger
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
# Обязательно меняем на 5.0, чтобы сбросить старый кэш в 17МБ
version = 5.0

# Добавил sqlite3 и openssl - без них 2FA вылетает
requirements = python3,kivy==2.2.1,openssl,sqlite3,requests,pyrebase4,certifi,urllib3,pyjnius,android

orientation = portrait
android.api = 34
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Указываем иконку напрямую
icon.filename = icon.png
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.manifest.uses_cleartext_traffic = True
android.accept_sdk_license = True
android.presplash_color = #000000

[buildozer]
log_level = 2
warn_on_root = 1
