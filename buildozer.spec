[app]
title = Ghost PRO
# СТРОГО как в google-services.json:
package.name = ghost_messenger_secure
package.domain = org.ghost
source.dir = .
source.include_exts = py,png,jpg,kv,html,js,json
# Меняем версию на 6.0 для сброса кэша
version = 6.0

requirements = python3,kivy==2.2.1,pyjnius,android,requests,pyrebase4,urllib3,certifi,openssl

# Иконка (проверь, что в репе файл именно icon.png)
icon.filename = icon.png
