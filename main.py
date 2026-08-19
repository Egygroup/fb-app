from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests
from bs4 import BeautifulSoup
import json
import re

class FBGroupsApp(App):
    def build(self):
        self.title = "Facebook Groups Extractor"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # حقل إدخال الـ Cookie
        self.cookie_input = TextInput(
            hint_text='الصق الـ Cookie هنا (c_user=...; xs=...;)',
            size_hint_y=None,
            height=100,
            multiline=True
        )
        layout.add_widget(self.cookie_input)
        
        # زر التنفيذ
        btn = Button(
            text='جلب الجروبات',
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        btn.bind(on_press=self.get_groups)
        layout.add_widget(btn)
        
        # شاشة العرض للنتائج
        self.result_label = Label(
            text='النتيجة ستظهر هنا...',
            halign='center',
            valign='middle'
        )
        self.result_label.bind(texture_size=self.result_label.setter('texture_size'))
        layout.add_widget(self.result_label)
        
        return layout

    def get_groups(self, instance):
        cookie_string = self.cookie_input.text.strip()
        if not cookie_string:
            self.result_label.text = "الرجاء إدخال الـ Cookie أولاً!"
            return

        self.result_label.text = "جاري الاتصال وجلب الجروبات..."
        
        try:
            clean_cookie = cookie_string.encode('ascii', 'ignore').decode('ascii')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'Cookie': clean_cookie,
                'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8'
            }

            url = 'https://mbasic.facebook.com/groups/?category=membership'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            groups = []
            ignore_list = ['create', 'category', 'search', 'center', 'create_post', 'joins', 'help']

            for a in soup.find_all('a', href=True):
                href = a['href']
                text = a.get_text().strip()
                
                if '/groups/' in href and len(text) > 1:
                    match = re.search(r'/groups/([^/?#]+)', href)
                    if match:
                        group_id = match.group(1)
                        if group_id.lower() not in ignore_list:
                            if not any(g['id'] == group_id for g in groups):
                                groups.append({'name': text, 'id': group_id})

            if not groups:
                self.result_label.text = "❌ لم يتم العثور على جروبات. تأكد من صحة الـ Cookie."
            else:
                self.result_label.text = f"✅ تم العثور على {len(groups)} جروب بنجاح!"
                # يمكنك طباعة أول 3 أسماء كعينة
                names = "\n".join([g['name'] for g in groups[:5]])
                self.result_label.text += f"\n\nعينة من الجروبات:\n{names}"

        except Exception as e:
            self.result_label.text = f"❌ حدث خطأ: {str(e)}"

if __name__ == '__main__':
    FBGroupsApp().run()