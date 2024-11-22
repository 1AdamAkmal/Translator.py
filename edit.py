
# import tkinter as tk
# from tkinter import filedialog, colorchooser, simpledialog, messagebox
# import random
# from ttkbootstrap import ttk
# from trans import Trans  # Import the Trans class from trans.py

# class Edit:
#     def __init__(self, screen) -> None:
#         self.screen = screen

#         # Create Text widget in the left sidebar for user input (translation)
#         self.text_widget_input = tk.Text(screen, wrap='word', height=20, width=40)
#         self.text_widget_input.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
#         self.text_widget_input.insert(tk.END, "Write your text here to translate. Note: don't start the sentence with a capital letter, and use it in names.")

#         # Create the right sidebar with editing tools and display translated text
#         self.create_sidebar(screen)

#         # Make the grid rows/columns expand and fill
#         screen.grid_rowconfigure(0, weight=0)  # Row 0 for title (not expanding)
#         screen.grid_rowconfigure(1, weight=1)  # Row 1 for input and sidebars to expand
#         screen.grid_columnconfigure(0, weight=1)  # Column 0 (left sidebar) expand
#         screen.grid_columnconfigure(1, weight=0)  # Column 1 for the Translate button (fixed width)
#         screen.grid_columnconfigure(2, weight=1)  # Column 2 (right sidebar) expand

#     def create_sidebar(self, root):
#         # Create a frame for the right sidebar (to hold the translated text and editing tools)
#         right_sidebar = ttk.Frame(root, width=250, padding=10)
#         right_sidebar.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)  # placed in column 2 (right of the input area)

#         # Add a Text widget to display the translated text in the right sidebar
#         self.translated_text_display = tk.Text(right_sidebar, wrap='word', height=20, width=40)
#         self.translated_text_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
#         self.translated_text_display.insert(tk.END, "Translated text will appear here...")  # Placeholder text
#         self.translated_text_display.config(state=tk.DISABLED)  # Disable editing in the translated text display

#         # Add buttons to the sidebar for text editing tools
#         self.bold_button = ttk.Button(right_sidebar, text="Bold", command=self.toggle_bold)
#         self.bold_button.pack(fill=tk.X, pady=5)

#         self.italic_button = ttk.Button(right_sidebar, text="Italic", command=self.toggle_italic)
#         self.italic_button.pack(fill=tk.X, pady=5)

#         self.color_button = ttk.Button(right_sidebar, text="Text Color", command=self.choose_color)
#         self.color_button.pack(fill=tk.X, pady=5)

#         self.font_button = ttk.Button(right_sidebar, text="Font", command=self.choose_font)
#         self.font_button.pack(fill=tk.X, pady=5)

#         # Create a Translate button and place it in the middle (between left and right sidebars)
#         self.translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
#         self.translate_button.grid(row=1, column=1, padx=10, pady=10)

#     def translate_text(self):
#         try:
#             # Get the text from the left sidebar input area
#             input_text = self.text_widget_input.get("1.0", tk.END).strip()

#             if input_text:
#                 # Create an instance of the Trans class from trans.py to handle the translation logic
#                 translator = Trans(text=input_text, from_language='en', to_language='es')  # Translate from English to Spanish
#                 translated_text = translator.translated_text  # Get the translated text

#                 # Update the translated text display in the right sidebar as well
#                 self.translated_text_display.config(state=tk.NORMAL)  # Re-enable editing for updating text
#                 self.translated_text_display.delete("1.0", tk.END)
#                 self.translated_text_display.insert(tk.END, translated_text)
#                 self.translated_text_display.config(state=tk.DISABLED)  # Disable editing again
#         except Exception as e:
#             print(f"Error during translation: {e}")

#     def toggle_bold(self):
#         try:
#             # Ensure that text is selected
#             current_tags = self.translated_text_display.tag_names("sel.first")
#             if "bold" in current_tags:
#                 self.translated_text_display.tag_remove("bold", "sel.first", "sel.last")
#             else:
#                 self.translated_text_display.tag_add("bold", "sel.first", "sel.last")
#                 self.translated_text_display.tag_configure("bold", font=("Helvetica", 10, "bold"))
#         except tk.TclError:
#             # Handle case where no text is selected
#             pass

#     def toggle_italic(self):
#         try:
#             # Ensure that text is selected
#             current_tags = self.translated_text_display.tag_names("sel.first")
#             if "italic" in current_tags:
#                 self.translated_text_display.tag_remove("italic", "sel.first", "sel.last")
#             else:
#                 self.translated_text_display.tag_add("italic", "sel.first", "sel.last")
#                 self.translated_text_display.tag_configure("italic", font=("Helvetica", 10, "italic"))
#         except tk.TclError:
#             # Handle case where no text is selected
#             pass

#     def choose_color(self):
#         # Ensure that some text is selected before applying a color
#         try:
#             # Open a color picker dialog to choose a color
#             color = colorchooser.askcolor()[1]  # Get the hex color code
#             if color:
#                 # Check if text is selected
#                 if self.translated_text_display.tag_ranges("sel"):
#                     color_tag = f"color_{random.randint(1000, 9999)}"
#                     self.translated_text_display.tag_add(color_tag, "sel.first", "sel.last")
#                     self.translated_text_display.tag_configure(color_tag, foreground=color)
#                 else:
#                     # If no text is selected, show a message
#                     messagebox.showinfo("No Text Selected", "Please select some text first to apply the color.")
#         except Exception as e:
#             print(f"Error applying color: {e}")

#     def choose_font(self):
#         # Open a dialog to choose the font and size
#         font_name = simpledialog.askstring("Font", "Enter Font Name (e.g., Arial, Times New Roman):")
#         font_size = simpledialog.askinteger("Font Size", "Enter Font Size (e.g., 12, 14):", minvalue=6, maxvalue=72)
        
#         if font_name and font_size:
#             try:
#                 self.translated_text_display.tag_add("font", "sel.first", "sel.last")
#                 self.translated_text_display.tag_configure("font", font=(font_name, font_size))
#             except tk.TclError:
#                 # Handle case when no text is selected (apply font to any future text)
#                 self.translated_text_display.config(font=(font_name, font_size))

# # Main part of the code (to run the app)
# if __name__ == "__main__":
#     root = tk.Tk()  # Create the root Tkinter window
#     root.title("Ploto")  # Set the window title to "Ploto"
#     root.geometry("1000x600")  # Adjust the window size to fit the sidebars

#     # Create the Edit object with the root window as the parent
#     edit_tools = Edit(screen=root)

#     # Title label centered at row 0
#     Title = ttk.Label(root, text="PLOTO", font=("Times New Roman", 34, "italic"))
#     Title.grid(row=0, column=0, columnspan=3, pady=10)  # Center it in row 0 across all columns
    
#     root.mainloop()  # Start the Tkinter event loop to run the application

import tkinter as tk
from tkinter import filedialog, colorchooser, simpledialog, messagebox
import random
from ttkbootstrap import ttk
from trans import Trans  # Import the Trans class from trans.py
import pyperclip  # Optional: if you want a more robust clipboard management

class Edit:
    def __init__(self, screen) -> None:
        self.screen = screen

        # Create Text widget in the left sidebar for user input (translation)
        self.text_widget_input = tk.Text(screen, wrap='word', height=20, width=40)
        self.text_widget_input.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.text_widget_input.insert(tk.END, "Write your text here to translate. Note: don't start the sentence with a capital letter, and use it in names.")

        # Create the right sidebar with editing tools and display translated text
        self.create_sidebar(screen)

        # Make the grid rows/columns expand and fill
        screen.grid_rowconfigure(0, weight=0)  # Row 0 for title (not expanding)
        screen.grid_rowconfigure(1, weight=1)  # Row 1 for input and sidebars to expand
        screen.grid_columnconfigure(0, weight=0, minsize=200)  # Left sidebar (fixed width)
        screen.grid_columnconfigure(1, weight=1)  # Middle area (Translate button)
        screen.grid_columnconfigure(2, weight=0, minsize=250)  # Right sidebar (fixed width)

    def create_sidebar(self, root):
        # Create a frame for the right sidebar (to hold the translated text and editing tools)
        right_sidebar = ttk.Frame(root, width=250, padding=10)
        right_sidebar.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)  # placed in column 2 (right of the input area)

        # Add a Text widget to display the translated text in the right sidebar
        self.translated_text_display = tk.Text(right_sidebar, wrap='word', height=20, width=40)
        self.translated_text_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.translated_text_display.insert(tk.END, "Translated text will appear here...")  # Placeholder text
        self.translated_text_display.config(state=tk.DISABLED)  # Disable editing in the translated text display

        # Add buttons to the sidebar for text editing tools
        self.bold_button = ttk.Button(right_sidebar, text="Bold", command=self.toggle_bold)
        self.bold_button.pack(fill=tk.X, pady=5)

        self.italic_button = ttk.Button(right_sidebar, text="Italic", command=self.toggle_italic)
        self.italic_button.pack(fill=tk.X, pady=5)

        self.color_button = ttk.Button(right_sidebar, text="Text Color", command=self.choose_color)
        self.color_button.pack(fill=tk.X, pady=5)

        self.font_button = ttk.Button(right_sidebar, text="Font", command=self.choose_font)
        self.font_button.pack(fill=tk.X, pady=5)

        # Create a Translate button and place it in the middle (between left and right sidebars)
        self.translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=1, column=1, padx=10, pady=10)

        # Add the Copy button to copy the translated text with styles
        self.copy_button = ttk.Button(right_sidebar, text="Copy", command=self.copy_translated_text)
        self.copy_button.pack(fill=tk.X, pady=5)

    def translate_text(self):
        try:
            # Get the text from the left sidebar input area
            input_text = self.text_widget_input.get("1.0", tk.END).strip()

            if input_text:
                # Create an instance of the Trans class from trans.py to handle the translation logic
                translator = Trans(text=input_text, from_language='en', to_language='es')  # Translate from English to Spanish
                translated_text = translator.translated_text  # Get the translated text

                # Update the translated text display in the right sidebar as well
                self.translated_text_display.config(state=tk.NORMAL)  # Re-enable editing for updating text
                self.translated_text_display.delete("1.0", tk.END)
                self.translated_text_display.insert(tk.END, translated_text)
                self.translated_text_display.config(state=tk.DISABLED)  # Disable editing again
        except Exception as e:
            print(f"Error during translation: {e}")

    def toggle_bold(self):
        try:
            # Ensure that text is selected
            current_tags = self.translated_text_display.tag_names("sel.first")
            if "bold" in current_tags:
                self.translated_text_display.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.translated_text_display.tag_add("bold", "sel.first", "sel.last")
                self.translated_text_display.tag_configure("bold", font=("Helvetica", 10, "bold"))
        except tk.TclError:
            # Handle case where no text is selected
            pass

    def toggle_italic(self):
        try:
            # Ensure that text is selected
            current_tags = self.translated_text_display.tag_names("sel.first")
            if "italic" in current_tags:
                self.translated_text_display.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.translated_text_display.tag_add("italic", "sel.first", "sel.last")
                self.translated_text_display.tag_configure("italic", font=("Helvetica", 10, "italic"))
        except tk.TclError:
            # Handle case where no text is selected
            pass

    def choose_color(self):
        # Ensure that some text is selected before applying a color
        try:
            # Open a color picker dialog to choose a color
            color = colorchooser.askcolor()[1]  # Get the hex color code
            if color:
                # Check if text is selected
                if self.translated_text_display.tag_ranges("sel"):
                    color_tag = f"color_{random.randint(1000, 9999)}"
                    self.translated_text_display.tag_add(color_tag, "sel.first", "sel.last")
                    self.translated_text_display.tag_configure(color_tag, foreground=color)
                else:
                    # If no text is selected, show a message
                    messagebox.showinfo("No Text Selected", "Please select some text first to apply the color.")
        except Exception as e:
            print(f"Error applying color: {e}")

    def choose_font(self):
        # Open a dialog to choose the font and size
        font_name = simpledialog.askstring("Font", "Enter Font Name (e.g., Arial, Times New Roman):")
        font_size = simpledialog.askinteger("Font Size", "Enter Font Size (e.g., 12, 14):", minvalue=6, maxvalue=72)
        
        if font_name and font_size:
            try:
                self.translated_text_display.tag_add("font", "sel.first", "sel.last")
                self.translated_text_display.tag_configure("font", font=(font_name, font_size))
            except tk.TclError:
                # Handle case when no text is selected (apply font to any future text)
                self.translated_text_display.config(font=(font_name, font_size))

    def copy_translated_text(self):
        # Copy the translated text including formatting (bold, italics, color, etc.) to the clipboard
        try:
            text = self.translated_text_display.get("1.0", "end-1c")  # Get the text content
            # Example: Using the 'pyperclip' library to handle clipboard management
            pyperclip.copy(text)  # Copies the plain text to clipboard (without formatting)
            # To preserve tags you need a custom clipboard manager, or implement something like RTF/HTML formatting
            messagebox.showinfo("Copy", "Translated text copied to clipboard!")
        except Exception as e:
            print(f"Error copying text: {e}")
            
# Main part of the code (to run the app)
if __name__ == "__main__":
    root = tk.Tk()  # Create the root Tkinter window
    root.title("Ploto")  # Set the window title to "Ploto"
    root.geometry("1000x600")  # Adjust the window size to fit the sidebars

    # Create the Edit object with the root window as the parent
    edit_tools = Edit(screen=root)

    # Title label centered at row 0
    Title = ttk.Label(root, text="PLOTO", font=("Times New Roman", 34, "italic"))
    Title.grid(row=0, column=0, columnspan=3, pady=10)  # Center it in row 0 across all columns
    
    root.mainloop()  # Start the Tkinter event loop to run the application
