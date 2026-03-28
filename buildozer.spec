[app]
title = Kyoga TV
package.name = kyogatv
package.domain = org.olica1995
source.dir = .
source.include_exts = py,png,jpg,ico
version = 1.0

# Requirements for video playback
requirements = python3,kivy,android,requests

orientation = portrait
fullscreen = 1
android.permissions = INTERNET, ACCESS_NETWORK_STATE
icon.filename = logo.ico

[buildozer]
log_level = 2
