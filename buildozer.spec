[app]
title = Kyoga TV
package.name = kyogatv
package.domain = org.olica1995
source.dir = .
source.include_exts = py,png,jpg,ico
version = 1.0

# Keeping requirements minimal for the first successful flow
requirements = python3,kivy==2.3.0,android

orientation = portrait
fullscreen = 1
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Your Icon
icon.filename = logo.ico

# These settings prevent the "License" and "Space" errors
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
