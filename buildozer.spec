[app]
title = Clownware
package.name = clownware
package.domain = org.kanha
source.include_exts = py,png,jpg,kv,atlas,mp3,ogg,wav
version = 1.0
requirements = python3,kivy,plyer,pyjnius,android,ffpyplayer
orientation = portrait
fullscreen = 0
android.permissions = POST_NOTIFICATIONS,INTERNET,VIBRATE,SCHEDULE_EXACT_ALARM,WAKE_LOCK

[buildozer]
log_level = 2
warn_on_root = 1