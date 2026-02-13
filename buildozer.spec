[app]
title = Ghost PRO
# СТРОГО как в твоем google-services.json
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
# Меняем версию на 7.0, чтобы пробить кэш
version = 7.0

requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,urllib3,certifi,openssl

orientation = portrait
# Фиксируем API и инструменты, чтобы не было ошибки Aidl
android.api = 33
android.minapi = 24
android.sdk = 33
android.build_tools = 33.0.0
android.ndk = 25b
android.archs = arm64-v8a

# Иконка
icon.filename = icon.png
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.manifest.uses_cleartext_traffic = True
android.accept_sdk_license = True
android.presplash_color = #000000

[buildozer]
log_level = 2
warn_on_root = 1
