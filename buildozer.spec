[app]
title = Ghost PRO
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
version = 0.1

# ВАЖНО: добавил hostpython3 и переставил cryptography в начало
requirements = python3, hostpython3, kivy==2.2.1, cryptography, requests, pyrebase4, certifi, urllib3, openssl, pillow, pyjnius, android

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
