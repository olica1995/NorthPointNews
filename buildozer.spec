[app]
title = Kyoga TV
package.name = kyogatv
package.domain = org.olica1995
source.dir = .
source.include_exts = py,png,jpg,ico
version = 1.0

# Essential requirements only to ensure a smooth flow
requirements = python3,kivy==2.3.0,android,requests,certifi

orientation = portrait
fullscreen = 1
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Your Logo Config
icon.filename = logo.ico

# Critical settings to skip license prompts and errors
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
