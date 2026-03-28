[app]
title = Kyoga TV
package.name = kyogatv
package.domain = org.olica1995
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Pillow is REQUIRED for the icon to work
requirements = python3,kivy==2.3.0,pillow

orientation = portrait
fullscreen = 1
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Pointing to the new PNG file
icon.filename = icon.png

# Safety settings for 2026 Android standards
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
