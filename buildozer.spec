[app]

# (str) Title of your application
title = Egy Group

# (str) Package name
package.name = egyapp

# (str) Package domain (needed for android packaging)
package.domain = org.egygroup

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Directory where the source code is located
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (string) Automatic acceptance of SDK license
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact, output of the build
bin_dir = ./bin
