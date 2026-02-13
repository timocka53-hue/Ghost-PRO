[app]
title = Ghost PRO
# Новое имя пакета, чтобы Android и GitHub подумали, что это новое приложение
package.name = ghost_ultimate_secure
package.domain = org.ghost.pro
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 1.0

# Добавляем тяжелые либы, чтобы вес СТАЛ больше 17 МБ
requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,certifi,urllib3,openssl,sqlite3

orientation = portrait
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

icon.filename = icon.png
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.manifest.uses_cleartext_traffic = True
android.accept_sdk_license = True
