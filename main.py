from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.toolbar import MDTopAppBar
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
import random
import arabic_reshaper
from bidi.algorithm import get_display

# 🛠️ دالة سحرية لإصلاح الكتابة العربية
def fix_text(text):
    try:
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        return bidi_text
    except:
        return text

class AlmaherApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.store = JsonStore('almaher_data.json')
        
        # الشاشة الرئيسية
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical')
        
        # 1. الشريط العلوي
        toolbar = MDTopAppBar(title=fix_text("الماهر بالقرآن"))
        toolbar.elevation = 10
        layout.add_widget(toolbar)
        
        # 2. مساحة المحتوى
        content = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # رسالة تحفيزية
        quotes = [
            "خيركم من تعلم القرآن وعلمه",
            "اقرأ وارتق ورتل",
            "القرآن ربيع القلوب"
        ]
        quote_txt = random.choice(quotes)
        self.lbl_quote = MDLabel(
            text=fix_text(quote_txt),
            halign="center",
            theme_text_color="Secondary",
            font_style="H6"
        )
        content.add_widget(self.lbl_quote)
        
        # قائمة الورد
        scroll = MDScrollView()
        self.list_view = MDList()
        
        # تحميل البيانات المحفوظة
        self.load_data()
        
        scroll.add_widget(self.list_view)
        content.add_widget(scroll)
        
        layout.add_widget(content)
        screen.add_widget(layout)
        
        # زر الإضافة العائم
        btn_add = MDFloatingActionButton(
            icon="plus",
            pos_hint={"x": 0.8, "y": 0.05},
            on_release=self.add_new_wird
        )
        screen.add_widget(btn_add)
        
        return screen

    def load_data(self):
        self.list_view.clear_widgets()
        # إضافة عناصر تجريبية إذا كانت القائمة فارغة
        if not self.store.exists('wird'):
            self.store.put('wird', items=[])
            
        items = self.store.get('wird')['items']
        if not items:
             # عرض رسالة فارغة
            empty_label = OneLineIconListItem(text=fix_text("لا يوجد ورد حالياً"))
            self.list_view.add_widget(empty_label)
        else:
            for item in items:
                self.add_list_item(item)

    def add_list_item(self, text):
        item = OneLineIconListItem(text=fix_text(text))
        icon = IconLeftWidget(icon="book-open-page-variant")
        item.add_widget(icon)
        self.list_view.add_widget(item)

    def add_new_wird(self, instance):
        # محاكاة إضافة ورد جديد (يمكن تطويرها لنافذة منبثقة لاحقاً)
        new_text = f"حزب {random.randint(1,60)} - ثمن {random.randint(1,8)}"
        
        # حفظ في الذاكرة
        current_items = self.store.get('wird')['items']
        current_items.append(new_text)
        self.store.put('wird', items=current_items)
        
        # تحديث الشاشة
        self.load_data()

if __name__ == "__main__":
    AlmaherApp().run()
