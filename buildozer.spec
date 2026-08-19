[app]

title = Egy Group
package.name = egyapp
package.domain = org.egygroup
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 0.1

# أضف هنا أي مكتبات تستخدمها في كود بايثون مفصولة بفواصل، مثل requests, bs4 وغيرها
requirements = python3,kivy

android.permissions = INTERNET
orientation = portrait
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
bin_dir = ./bin
