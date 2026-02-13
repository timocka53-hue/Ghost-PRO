[app]
title = Ghost PRO
# Новое имя пакета для сброса всех глюков
package.name = ghost_v26_final
package.domain = org.ghost.messenger
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 26.9

# Самый стабильный набор либ
requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,certifi,urllib3,openssl,sqlite3

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
