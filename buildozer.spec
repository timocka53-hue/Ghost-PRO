[app]
title = Ghost PRO
package.name = ghost.pro.secure
package.domain = org.ghost.dev
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 3.1

# Включаем тяжелые либы, чтобы билд не был 17МБ
requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,urllib3,certifi,openssl,pandas

orientation = portrait
android.api = 34
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.manifest.uses_cleartext_traffic = True
android.accept_sdk_license = True
android.presplash_color = #000000
presplash.filename = 
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1

