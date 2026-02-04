[app]

# (str) Title of your application
title = Almaher
version = 1.0
# (str) Package name
package.name = almaher

# (str) Package domain (needed for android/ios packaging)
package.domain = org.almaher

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# هذه هي المكونات التي سنحتاجها
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,arabic-reshaper,python-bidi
# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Android additional adb arguments
# android.adb_args = -H host.docker.internal

# (list) Android aapt2 compile arguments
# android.aapt2_compile_args =

# (list) Android aapt2 link arguments
# android.aapt2_link_args =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
