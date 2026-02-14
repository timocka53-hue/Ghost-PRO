[app]
title = Ghost PRO Ultimate
package.name = ghost_ultimate_v26
package.domain = org.ghost.secure
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0.8

# ЖЕСТКИЙ СПИСОК: добавили либы, которые точно весят 30+ МБ
requirements = python3, hostpython3, kivy==2.2.1, pillow, pyjnius, android, requests, pyrebase4, certifi, urllib3, openssl, sqlite3, pycryptodome

orientation = portrait
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

# Иконка
icon.filename = icon.png

# Разрешения для работы мессенджера
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.manifest.uses_cleartext_traffic = True

[buildozer]
log_level = 2
warn_on_root = 1
