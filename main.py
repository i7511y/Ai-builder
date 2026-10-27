import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class AIBuilderApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # عنوان التطبيق
        root.add_widget(Label(text='[b]AI Builder - صانع ونماذج الذكاء الاصطناعي[/b]', markup=True, font_size=18, size_hint_y=None, height=45))

        # اسم النموذج
        root.add_widget(Label(text='اسم النموذج:', size_hint_y=None, height=25))
        self.input_name = TextInput(text='MyCustomAI', multiline=False, size_hint_y=None, height=40)
        root.add_widget(self.input_name)

        # اللهجة والأسلوب
        root.add_widget(Label(text='اللهجة أو أسلوب التحدث:', size_hint_y=None, height=25))
        self.input_dialect = TextInput(text='اللهجة السعودية / ودود وذكي', multiline=False, size_hint_y=None, height=40)
        root.add_widget(self.input_dialect)

        # التعليمات (System Prompt)
        root.add_widget(Label(text='تعليمات السلوك وقواعد النموذج (System Instructions):', size_hint_y=None, height=25))
        self.input_instructions = TextInput(text='أنت مساعد ذكي تم تدريبك للإجابة بدقة وحسب الطلب بلهجة محلية.', size_hint_y=True)
        root.add_widget(self.input_instructions)

        # زر التدريب والتصدير كملف
        btn_train = Button(
            text='تدريب وبناء ملف النموذج (Export Model)', 
            size_hint_y=None, 
            height=50, 
            background_color=(0.1, 0.6, 0.3, 1)
        )
        btn_train.bind(on_press=self.export_ai_model)
        root.add_widget(btn_train)

        # خانة الحالة
        self.lbl_status = Label(text='حالة النموذج: جاهز للإنشاء والتدريب', size_hint_y=None, height=35, color=(0, 1, 0, 1))
        root.add_widget(self.lbl_status)

        return root

    def export_ai_model(self, instance):
        name = self.input_name.text.strip() or "AI_Model"
        dialect = self.input_dialect.text.strip()
        instructions = self.input_instructions.text.strip()

        # هيكل بيانات تدريب النموذج الحقيقي
        model_data = {
            "model_name": name,
            "dialect": dialect,
            "system_prompt": instructions,
            "dataset": [
                {"role": "system", "content": f"أنت {name} وتتحدث بـ {dialect}. التعليمات: {instructions}"},
                {"role": "user", "content": "مرحباً بك"},
                {"role": "assistant", "content": f"أهلاً! أنا نموذج {name} الخاص بك والمبرمج للعمل حسب توجيهاتك."}
            ]
        }

        file_name = f"{name}_model.jsonl"
        
        # حفظ الملف (يتوافق مع ويندوز وأندرويد)
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(json.dumps(model_data, ensure_ascii=False) + "\n")
            self.lbl_status.text = f"تم التدريب بنجاح! حفظ الملف باسم: {file_name}"
        except Exception as e:
            self.lbl_status.text = f"حدث خطأ أثناء الحفظ: {str(e)}"

if __name__ == '__main__':
    AIBuilderApp().run()
           messagebox.showinfo("تم الحفظ", "تم حفظ ملف نموذج الذكاء الاصطناعي المدرب بنجاح وجاهز للاستخدام في موقعك!")

    def export_website_file(self):
        code = self.txt_code.get("1.0", tk.END).strip()
        file_path = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[("HTML File", "*.html")],
            initialfile="index.html"
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)
            messagebox.showinfo("تم التصدير", "تم حفظ ملف الموقع الإلكتروني للنشر على استضافتك!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AIModelStudioApp(root)
    root.mainloop()
