[app]
title = Ghost PRO
# Пакет из твоего конфига Google
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 26.0

# Добавил системные 'anchor' библиотеки для веса
requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,certifi,urllib3,openssl,sqlite3,pbr,six

orientation = portrait
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

# Форсируем иконку
icon.filename = %(source.dir)s/icon.png
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.manifest.uses_cleartext_traffic = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
