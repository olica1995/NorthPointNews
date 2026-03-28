[app]
title = Kyoga TV
package.name = kyogatv
package.domain = org.olica1995
source.dir = .
source.include_exts = py,png,jpg,ico
version = 1.0
requirements = python3,kivy,android,requests
orientation = portrait
fullscreen = 1
android.permissions = INTERNET, ACCESS_NETWORK_STATE
icon.filename = logo.ico

# --- ADD THESE TWO LINES ---
android.accept_sdk_license = True
android.api = 33
# ---------------------------

[buildozer]
log_level = 2
