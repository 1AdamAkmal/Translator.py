# import tkinter as tk
# from tkinter import filedialog, colorchooser, simpledialog, messagebox
# import random
# from ttkbootstrap import Style, ttk
# import pyperclip  # For clipboard management
# from trans import Trans  # Import the Trans class (ensure trans.py is available)

import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
from ttkbootstrap import Style
from trans import Trans
import arabic_reshaper
from bidi.algorithm import get_display
import random


class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translation App")
        self.root.geometry("1020x600")

        # Language options
        self.languages = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Arabic": "ar",
        }
        self.from_language = tk.StringVar(value="English")
        self.to_language = tk.StringVar(value="Arabic")

        # Title
        title_label = ttk.Label(root, text="Translation App", font=("Helvetica", 24, "bold"))
        title_label.place(x=350, y=10)

        # Language selectors
        ttk.Label(root, text="From:", font=("Helvetica", 12)).place(x=200, y=60)
        from_lang_menu = ttk.Combobox(root, textvariable=self.from_language, values=list(self.languages.keys()))
        from_lang_menu.place(x=300, y=60, width=120)

        ttk.Label(root, text="To:", font=("Helvetica", 12)).place(x=500, y=60)
        to_lang_menu = ttk.Combobox(root, textvariable=self.to_language, values=list(self.languages.keys()))
        to_lang_menu.place(x=540, y=60, width=120)

        # Input Text Box
        self.input_text = tk.Text(root, wrap="word", height=10, width=30, font=("Helvetica", 12))
        self.input_text.place(x=170, y=185)
        self.input_text.insert(tk.END, "Write in the source language here.")

        # Translated Text Box
        self.translated_text = tk.Text(root, wrap="word", height=10, width=30, font=("Helvetica", 12), state=tk.DISABLED)
        self.translated_text.place(x=585, y=185)

        # Translate Button
        translate_button = ttk.Button(root, text="Translate", command=self.translate_text, bootstyle="warning")
        translate_button.place(x=475, y=260)

        # Correction Button
        correction_button = ttk.Button(root, text="Correction Words", command=self.correct_text)
        correction_button.place(x=460, y=420)

        # Formatting Buttons
        bold_button = ttk.Button(root, text="Bold", command=self.toggle_bold, bootstyle="danger")
        bold_button.place(x=870, y=200)

        italic_button = ttk.Button(root, text="Italic", command=self.toggle_italic)
        italic_button.place(x=870, y=260)

        color_button = ttk.Button(root, text="Color", command=self.choose_color)
        color_button.place(x=870, y=320)

    def translate_text(self):
        try:
            input_text = self.input_text.get("1.0", tk.END).strip()
            if input_text:
                from_lang = self.languages[self.from_language.get()]
                to_lang = self.languages[self.to_language.get()]
                translator = Trans(text=input_text, from_language=from_lang, to_language=to_lang)
                translated_text = translator.translated_text

                if to_lang == "ar":
                    reshaped_text = arabic_reshaper.reshape(translated_text)
                    rtl_text = get_display(reshaped_text)
                    self.display_text(self.translated_text, rtl_text)
                else:
                    self.display_text(self.translated_text, translated_text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during translation: {e}")

    def display_text(self, text_box, text):
        text_box.config(state=tk.NORMAL)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)
        text_box.config(state=tk.DISABLED)

    def toggle_bold(self):
        try:
            current_tags = self.translated_text.tag_names("sel.first")
            if "bold" in current_tags:
                self.translated_text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.translated_text.tag_add("bold", "sel.first", "sel.last")
                self.translated_text.tag_configure("bold", font=("Helvetica", 12, "bold"))
        except tk.TclError:
            pass

    def toggle_italic(self):
        try:
            current_tags = self.translated_text.tag_names("sel.first")
            if "italic" in current_tags:
                self.translated_text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.translated_text.tag_add("italic", "sel.first", "sel.last")
                self.translated_text.tag_configure("italic", font=("Helvetica", 12, "italic"))
        except tk.TclError:
            pass

    def choose_color(self):
        try:
            color = colorchooser.askcolor()[1]
            if color and self.translated_text.tag_ranges("sel"):
                color_tag = f"color_{random.randint(1000, 9999)}"
                self.translated_text.tag_add(color_tag, "sel.first", "sel.last")
                self.translated_text.tag_configure(color_tag, foreground=color)
        except Exception as e:
            print(f"Error applying color: {e}")

    def correct_text(self):
        messagebox.showinfo("Correction", "Spell correction is done automatically during translation.")


if __name__ == "__main__":
    root = tk.Tk()
    style = Style(theme="cosmo")
    TranslationApp(root)
    root.mainloop()




# import tkinter as tk
# from tkinter import ttk, messagebox, colorchooser
# from ttkbootstrap import Style
# from trans import Trans
# import arabic_reshaper
# from bidi.algorithm import get_display
# import random


# class TranslationApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Translation App")
#         self.root.geometry("1020x600")
#         #self.root.resizable(False, False)

#         # Language options
#         self.languages = {
#             "English": "en",
#             "Spanish": "es",
#             "French": "fr",
#             "German": "de",
#             "Arabic": "ar",
#         }
#         self.from_language = tk.StringVar(value="English")
#         self.to_language = tk.StringVar(value="Arabic")

#         # Title
#         title_label = ttk.Label(root, text="Translation App", font=("Helvetica", 24, "bold"))
#         title_label.place(x=350, y=10)

#         # Language selectors
#         ttk.Label(root, text="From:", font=("Helvetica", 12)).place(x=200, y=60)
#         from_lang_menu = ttk.Combobox(root, textvariable=self.from_language, values=list(self.languages.keys()))
#         from_lang_menu.place(x=300, y=60, width=120)

#         ttk.Label(root, text="To:", font=("Helvetica", 12)).place(x=500, y=60)
#         to_lang_menu = ttk.Combobox(root, textvariable=self.to_language, values=list(self.languages.keys()))
#         to_lang_menu.place(x=540, y=60, width=120)

#         # Input Text Box
#         self.input_text = tk.Text(root, wrap="word", height=10, width=30, font=("Helvetica", 12))
#         self.input_text.place(x=170, y=185)
#         self.input_text.insert(tk.END, "Write in the source language here.")

#         # Translated Text Box
#         self.translated_text = tk.Text(root, wrap="word", height=10, width=30, font=("Helvetica", 12), state=tk.DISABLED)
#         self.translated_text.place(x=585, y=185)

#         # Translate Button
#         translate_button = ttk.Button(root, text="Translate", command=self.translate_text, width=10, bootstyle = "warning")
#         translate_button.place(x=475, y=260)

#         # Correction Button
#         correction_button = ttk.Button(root, text="Correction Words", command=self.correct_text, width=10)
#         correction_button.place(x=475, y=380)

#         # Formatting Buttons
#         bold_button = ttk.Button(root, text="Bold", command=self.toggle_bold, width=10, bootstyle = "danger")
#         bold_button.place(x=870, y=200)

#         italic_button = ttk.Button(root, text="Italic", command=self.toggle_italic, width=10)
#         italic_button.place(x=870, y=260)

#         color_button = ttk.Button(root, text="Text Color", command=self.choose_color, width=10)
#         color_button.place(x=870, y=320)

#     def translate_text(self):
#         try:
#             # Get the input text from the input text box
#             input_text = self.input_text.get("1.0", tk.END).strip()

#             if input_text:
#                 # Get the selected source and target languages
#                 from_lang = self.languages[self.from_language.get()]
#                 to_lang = self.languages[self.to_language.get()]

#                 # Translate the text using the Trans class
#                 translator = Trans(text=input_text, from_language=from_lang, to_language=to_lang)
#                 translated_text = translator.translated_text

#                 # Check if the target language is Arabic
#                 if to_lang or from_lang == "ar":
#                     # Use arabic_reshaper and Bidi to prepare the text for proper RTL display
#                     reshaped_text = arabic_reshaper.reshape(translated_text)
#                     rtl_text = get_display(reshaped_text)

#                     # Configure the text box for Arabic display
#                     self.translated_text.config(state=tk.NORMAL, wrap="word", font=("Arial", 12))
#                     self.translated_text.delete("1.0", tk.END)
#                     self.translated_text.insert(tk.END, rtl_text)  # Insert reshaped RTL text
#                     self.translated_text.config(state=tk.DISABLED)
                    
#                     # Use arabic_reshaper and Bidi to prepare the text for textinput RTL display
#                     reshaped_text2 = arabic_reshaper.reshape(translated_text)
#                     rtl_text2 = get_display(reshaped_text2)

#                     # Configure the text box for Arabic display
#                     self.input_text.config(state=tk.NORMAL, wrap="word", font=("Arial", 12))
#                     self.input_text.delete("1.0", tk.END)
#                     self.input_text.insert(tk.END, rtl_text2)  # Insert reshaped RTL text
#                     self.input_text.config(state=tk.DISABLED)
#                 else:
#                     # Handle left-to-right languages (e.g., English, Spanish)
#                     self.translated_text.config(state=tk.NORMAL, wrap="word", font=("Helvetica", 12))
#                     self.translated_text.delete("1.0", tk.END)
#                     self.translated_text.insert(tk.END, translated_text)
#                     self.translated_text.config(state=tk.DISABLED)
#         except Exception as e:
#             # Show error message in case of failure
#             messagebox.showerror("Error", f"An error occurred during translation: {e}")
#             print(f"Error details: {e}")  # Log error for debugging

#     def toggle_bold(self):
#         try:
#             current_tags = self.translated_text.tag_names("sel.first")
#             if "bold" in current_tags:
#                 self.translated_text.tag_remove("bold", "sel.first", "sel.last")
#             else:
#                 self.translated_text.tag_add("bold", "sel.first", "sel.last")
#                 self.translated_text.tag_configure("bold", font=("Helvetica", 12, "bold"))
#         except tk.TclError:
#             pass

#     def toggle_italic(self):
#         try:
#             current_tags = self.translated_text.tag_names("sel.first")
#             if "italic" in current_tags:
#                 self.translated_text.tag_remove("italic", "sel.first", "sel.last")
#             else:
#                 self.translated_text.tag_add("italic", "sel.first", "sel.last")
#                 self.translated_text.tag_configure("italic", font=("Helvetica", 12, "italic"))
#         except tk.TclError:
#             pass

#     def choose_color(self):
#         try:
#             color = colorchooser.askcolor()[1]
#             if color:
#                 if self.translated_text.tag_ranges("sel"):
#                     color_tag = f"color_{random.randint(1000, 9999)}"
#                     self.translated_text.tag_add(color_tag, "sel.first", "sel.last")
#                     self.translated_text.tag_configure(color_tag, foreground=color)
#         except Exception as e:
#             print(f"Error applying color: {e}")

#     def correct_text(self):
#         pass


# # Run the app
# if __name__ == "__main__":
#     root = tk.Tk()
#     style = Style(theme="cosmo")  # Ttkbootstrap theme
#     TranslationApp(root)
#     root.mainloop()