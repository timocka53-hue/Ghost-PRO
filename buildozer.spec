[app]
# Твое оригинальное название
title = Ghost PRO
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 0.1

# Добавили только критические либы для веса и работы Firebase
requirements = python3, kivy==2.2.1, cryptography, pillow, pyjnius, android, requests, pyrebase4, certifi, urllib3, openssl

orientation = portrait
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
icon.filename = icon.png

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.accept_sdk_license = True
android.manifest.uses_cleartext_traffic = True

[buildozer]
log_level = 2
warn_on_root = 1
