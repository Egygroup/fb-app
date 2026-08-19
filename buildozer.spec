[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientations
orientation = portrait

# (list) List of service to declare
#services = MyService:main.py:i,

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
# android.sdk = 33

# (int) Android NDK version to use
# android.ndk = 25b

# (bool) Indicate if the application should be fullscreen or not
android.fullscreen = 0

# (string) Automatic acceptance of SDK license
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact, output of the build
bin_dir = ./bin
