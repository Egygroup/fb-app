[app]

title = Egy Group
package.name = egyapp
package.domain = org.egygroup
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 0.1
requirements = python3,kivy
android.permissions = INTERNET
orientation = portrait

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 3
bin_dir = ./bin
