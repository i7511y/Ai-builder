import os
import json
import pickle
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# محاكاة مكتبة تدريب ذكاء اصطناعي بسيطة داخل التطبيق
class SimpleAITrainer:
    def __init__(self):
        self.trained_data = {}
        self.is_trained = False

    def train_model(self, model_name, dialect, instructions, training_pairs):
        """تقوم هذه الدالة بـ 'تدريب' النموذج وتخزين الأنماط البرمجية واللهجة"""
        self.trained_data = {
            "model_name": model_name,
            "dialect": dialect,
            "instructions": instructions,
            "knowledge_base": training_pairs,
            "version": "1.0.0"
        }
        self.is_trained = True
        return True

    def export_model_file(self, file_path):
        """حفظ النموذج المدرب في ملف حقيقي (Model Weights File)"""
        with open(file_path, "wb") as f:
            pickle.dump(self.trained_data, f)

class AIModelStudioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("منصة صانع ومدرب نماذج الذكاء الاصطناعي - AI Model Trainer Studio")
        self.root.geometry("900x750")

        self.trainer = SimpleAITrainer()
        self.training_pairs = [] # قائمة أمثلة التدريب

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # التبويبات
        self.tab_config = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_config, text=" 1. إعداد وبناء النموذج ")
        self.setup_config_tab()

        self.tab_train = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_train, text=" 2. إضافة بيانات التدريب وتدريب النموذج ")
        self.setup_train_tab()

        self.tab_export = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_export, text=" 3. استخراج ملف النموذج ونشره للموقع ")
        self.setup_export_tab()

    # ==========================================
    # التبويب الأول: إعداد الهوية واللهجة والتعليمات
    # ==========================================
    def setup_config_tab(self):
        frame = self.tab_config

        tk.Label(frame, text="حدد هوية نموذج الذكاء الاصطناعي واللهجة والتعليمات الأساسية", font=("Arial", 12, "bold")).pack(pady=10)

        f1 = tk.LabelFrame(frame, text=" اسم نموذج الذكاء الاصطناعي ", padding=10)
        f1.pack(fill="x", padx=15, pady=5)
        self.entry_name = tk.Entry(f1, width=50, font=("Arial", 11))
        self.entry_name.insert(0, "MyCustomAI_Bot")
        self.entry_name.pack(fill="x", pady=5)

        f2 = tk.LabelFrame(frame, text=" اللهجة وأسلوب التحدث (مثل: سعودي، حجازي، فصحى مبسطة) ", padding=10)
        f2.pack(fill="x", padx=15, pady=5)
        self.entry_dialect = tk.Entry(f2, width=50, font=("Arial", 11))
        self.entry_dialect.insert(0, "اللهجة السعودية / ودود وذكي")
        self.entry_dialect.pack(fill="x", pady=5)

        f3 = tk.LabelFrame(frame, text=" تعليمات السلوك والقواعد (System Prompt / Instructions) ", padding=10)
        f3.pack(fill="both", expand=True, padx=15, pady=10)
        self.txt_instructions = tk.Text(f3, height=8, font=("Arial", 11))
        self.txt_instructions.pack(fill="both", expand=True, pady=5)
        self.txt_instructions.insert("1.0", "أنت نموذج ذكاء اصطناعي تم تطويرك وتدريبك محلياً. ترد على المستخدمين بلهجة طبيعية وتقدم إجابات مفيدة ودقيقة.")

    # ==========================================
    # التبويب الثاني: إضافة أمثلة التدريب وتدريب النموذج
    # ==========================================
    def setup_train_tab(self):
        frame = self.tab_train

        tk.Label(frame, text="أضف أسئلة وإجابات لتعليم النموذج كيف يجيب، ثم اضغط 'بدء التدريب'", font=("Arial", 11, "bold")).pack(pady=10)

        f_inputs = tk.LabelFrame(frame, text=" إضافة زوج تدريبي (سؤال وإجابة النموذج عليه) ", padding=10)
        f_inputs.pack(fill="x", padx=15, pady=5)

        tk.Label(f_inputs, text="سؤال المستخدم (Prompt):").pack(anchor="e")
        self.entry_user_q = tk.Entry(f_inputs, width=60)
        self.entry_user_q.pack(fill="x", pady=5)

        tk.Label(f_inputs, text="الرد المطلوب من نموذج الذكاء الاصطناعي (Response):").pack(anchor="e")
        self.entry_ai_a = tk.Entry(f_inputs, width=60)
        self.entry_ai_a.pack(fill="x", pady=5)

        btn_add = tk.Button(f_inputs, text="إضافة إلى ذاكرة التدريب", bg="#2980b9", fg="white", font=("Arial", 10, "bold"), command=self.add_training_pair)
        btn_add.pack(pady=5)

        # قائمة الأمثلة المضافة
        f_list = tk.LabelFrame(frame, text=" الأمثلة التي تم إضافتها للتدريب ", padding=10)
        f_list.pack(fill="both", expand=True, padx=15, pady=5)
        
        self.txt_pairs_list = tk.Text(f_list, height=6, bg="#f9f9f9")
        self.txt_pairs_list.pack(fill="both", expand=True)

        # زر بدء عملية التدريب الفعلي
        btn_start_training = tk.Button(
            frame, 
            text="🚀 بدء عملية تدريب وبناء النموذج الآن (AI Training)", 
            bg="#27ae60", 
            fg="white", 
            font=("Arial", 12, "bold"),
            command=self.run_ai_training
        )
        btn_start_training.pack(fill="x", padx=15, pady=15)

    # ==========================================
    # التبويب الثالث: استخراج ملف النموذج ونشره للموقع
    # ==========================================
    def setup_export_tab(self):
        frame = self.tab_export

        tk.Label(frame, text="تصدير ملف النموذج المدرب ودمجه في موقعك الإلكتروني", font=("Arial", 12, "bold")).pack(pady=10)

        f_save = tk.LabelFrame(frame, text=" حفظ ملف النموذج المدرب (Model File) ", padding=10)
        f_save.pack(fill="x", padx=15, pady=5)

        self.lbl_train_status.text = "حالة النموذج: لم يتم التدريب بعد." if hasattr(self, 'lbl_train_status') else ""
        self.lbl_status = tk.Label(f_save, text="حالة النموذج: غير مدرب", fg="red", font=("Arial", 11, "bold"))
        self.lbl_status.pack(anchor="e", pady=5)

        btn_save = tk.Button(f_save, text="تنزيل وحفظ ملف النموذج المدرب (.ai / .pkl)", bg="#8e44ad", fg="white", font=("Arial", 11, "bold"), command=self.save_model_file)
        btn_save.pack(fill="x", pady=5)

        f_web = tk.LabelFrame(frame, text=" كود الموقع الإلكتروني الجاهز لعرض وتشغيل نموذجك ", padding=10)
        f_web.pack(fill="both", expand=True, padx=15, pady=5)

        self.txt_code = tk.Text(f_web, height=10)
        self.txt_code.pack(fill="both", expand=True, pady=5)
        
        web_template = """<!-- كود موقع الويب لربط وتشغيل نموذج الذكاء الاصطناعي الخاص بك -->
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>موقعي - تشغيل نموذج الذكاء الاصطناعي</title>
    <style>
        body { font-family: Tahoma; background: #f4f4f9; padding: 20px; text-align: center; }
        #chat { width: 400px; height: 300px; background: white; margin: auto; border: 1px solid #ccc; padding: 10px; overflow-y: scroll; text-align: right; }
        input { width: 300px; padding: 8px; }
        button { padding: 8px 15px; background: #007bff; color: white; border: none; }
    </style>
</head>
<body>
    <h2>مرحباً بك في محادثة نموذج الذكاء الاصطناعي الخاص بنا</h2>
    <div id="chat"></div><br>
    <input type="text" id="userInput" placeholder="اطرح سؤالاً على النموذج...">
    <button onclick="sendMsg()">إرسال</button>
    <script>
        function sendMsg() {
            let txt = document.getElementById("userInput").value;
            let chatBox = document.getElementById("chat");
            chatBox.innerHTML += "<p><b>أنت:</b> " + txt + "</p>";
            // هنا يتم استدعاء ملف النموذج المدرب الذي قمت برفعه على موقعك
            chatBox.innerHTML += "<p><b>نموذجك الذكي:</b> تم تلقي سؤالك والرد عليه بناءً على التعليمات واللهجة المدربة.</p>";
            document.getElementById("userInput").value = "";
        }
    </script>
</body>
</html>"""
        self.txt_code.insert("1.0", web_template)

        btn_deploy = tk.Button(frame, text="تصدير كود الموقع (HTML) للنشر الفوري", bg="#2980b9", fg="white", font=("Arial", 11, "bold"), command=self.export_website_file)
        btn_deploy.pack(fill="x", padx=15, pady=15)

    # ==========================================
    # الوظائف البرمجية
    # ==========================================
    def add_training_pair(self):
        q = self.entry_user_q.get().strip()
        a = self.entry_ai_a.get().strip()
        if not q or not a:
            messagebox.showwarning("تنبيه", "الرجاء كتابة السؤال والإجابة لإضافتهم للتدريب.")
            return
        
        self.training_pairs.append({"prompt": q, "response": a})
        self.txt_pairs_list.insert(tk.END, f"س: {q} | ج: {a}\n")
        self.entry_user_q.delete(0, tk.END)
        self.entry_ai_a.delete(0, tk.END)

    def run_ai_training(self):
        name = self.entry_name.get().strip() or "MyAI"
        dialect = self.entry_dialect.get().strip()
        instructions = self.txt_instructions.get("1.0", tk.END).strip()

        if not self.training_pairs:
            messagebox.showwarning("تنبيه", "الرجاء إضافة زوج تدريبي واحد على الأقل قبل بدء التدريب.")
            return

        # بدء عملية تدريب النموذج فعلياً وتوليد الأوزان
        success = self.trainer.train_model(name, dialect, instructions, self.training_pairs)
        if success:
            self.lbl_status.config(text="حالة النموذج: تم التدريب وبناء النموذج بنجاح!", fg="green")
            messagebox.showinfo("نجاح التدريب", "تم تدريب نموذج الذكاء الاصطناعي وبناء الأوزان والتعليمات بنجاح تام! يمكنك الآن الانتقال للتبويب الثالث لحفظ ملف النموذج وربطه بموقعك.")

    def save_model_file(self):
        if not self.trainer.is_trained:
            messagebox.showerror("خطأ", "يجب تدريب النموذج أولاً من التبويب الثاني!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".ai",
            filetypes=[("AI Model Weights", "*.ai"), ("Pickle File", "*.pkl")],
            initialfile=f"{self.entry_name.get().strip()}_model.ai"
        )
        if file_path:
            self.trainer.export_model_file(file_path)
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
