from translate import Translator
from spellchecker import SpellChecker
from textblob import TextBlob
import string
import re
from correction import Correcting  # Assuming you have this correction module for spell correction


from translate import Translator
from correction import Correcting
import re

class Trans:
    def __init__(self, text, from_language='en', to_language='en'):
        self.from_language = from_language
        self.text = text
        self.to_language = to_language

        corrector = Correcting(text=self.text, language=self.from_language)
        self.text = corrector.corrected_text
        self.misspelled_words = corrector.misspelled_words

        self.translated_text = self.translate_words()

    def translate_words(self):
        translator = Translator(to_lang=self.to_language, from_lang=self.from_language)
        return translator.translate(self.text)

    def is_arabic(self, text):
        arabic_pattern = re.compile('[\u0600-\u06FF]')
        return bool(arabic_pattern.search(text))




# #Create an instance of the Trans class to perform the translation and notify the user
# class Trans:
#     def __init__(self, text, from_language, to_language):
#         self.from_language = 'ar'  # source language
#         self.trans_text = "انما العلم بالتعلم"  # Example text
#         self.to_language = 'en' # converted text
        
#         # Initialize the Correcting class with the text
#         c = Correcting(text=self.trans_text, language=self.from_language)
#         self.trans_text = c.corrected_text  # Corrected text after spellcheck and grammar correction
#         self.misspelled_words = c.misspelled_words  # Get the list of misspelled words and corrections
        
#         # Now translate to Spanish
#         self.translate_words(to_language=self.to_language)
        
#         # Notify the user about misspelled words
#         self.notify_user_about_corrections()
        
#         # Print the translated text (Spanish)
#         print(f"Translated Text (English):")
#         print(self.translated_text)
        
#         # Process the Arabic text
#         self.arabic(self.trans_text)

#     def translate_words(self, to_language):
#         # Use the translate library to translate text
#         t = Translator(to_lang=to_language, from_lang=self.from_language)
        
#         # Translate the text
#         self.translated_text = t.translate(self.trans_text)

#     def notify_user_about_corrections(self):
#         # Notify the user about misspelled words and their corrections
#         if self.misspelled_words:
#             self.corrections = "\nMisspelled Words and Corrections:"
#             for original, corrected in self.misspelled_words:
#                 print(f"Incorrect: '{original}'")
#                 print(f"Corrected: '{corrected}'")
#         else:
#             print("No spelling mistakes found.")

#     def arabic(self, text):
#   # Check if the original text is in Arabic (before translation)
#         if self.is_arabic(text):
#           print("\nOriginal Arabic Text List (Right-to-Left order):")
#           # Option 1: Use a dedicated Arabic library (e.g., pyarabic)
#           # reversed_text = pyarabic.araby.reverse(text)  # Assuming pyarabic is installed
#           # print(reversed_text)

#           # Option 2: Maintain character order and rely on UI formatting
#           print(text[::-1])  # Reverse the characters for right-to-left order

#         else:
#           pass
        
#     def is_arabic(self, text):
#         # Simple function to check if the text contains Arabic characters using regex
#         arabic_pattern = re.compile('[\u0600-\u06FF]')
#         return bool(arabic_pattern.search(text))


# # Create an instance of the Trans class to perform the translation and notify the user
# tr = Trans()