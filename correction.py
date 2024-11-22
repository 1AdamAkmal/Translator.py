from translate import Translator
from spellchecker import SpellChecker
from textblob import TextBlob
import string
import re

class Correcting:
    def __init__(self, text, language):
        self.text = text
        self.language = language
        self.corrected_text = self.correct_text()  # This method will return corrected text
        self.misspelled_words = self.get_misspelled_words()

    def correct_text(self):
        # Use TextBlob or any other library for spelling and grammar correction
        blob = TextBlob(self.text)
        return str(blob.correct())

    def get_misspelled_words(self):
        spell = SpellChecker(language=self.language)
        words = self.text.split()
        misspelled = spell.unknown(words)
        corrections = [(word, spell.correction(word)) for word in misspelled]
        return corrections

    
    
# class Correcting:
#     def __init__(self, text, language='en'):
#         self.language = language
#         self.text = text
#         self.misspelled_words = []  # To store original misspelled words and their corrections
#         self.corrected_text = self.correct_text()

#     def correct_text(self):
#         # First, perform basic spell checking and correction using SpellChecker
#         spell = SpellChecker(language=self.language)
        
#         # Remove punctuation from text and split it into words
#         words = self.text.split()
#         words_without_punctuation = [word.strip(string.punctuation) for word in words]

#         # Find the misspelled words
#         misspelled = spell.unknown(words_without_punctuation)

#         # Correct the misspelled words using SpellChecker
#         corrected_words = []
#         for word in words:
#             clean_word = word.strip(string.punctuation)
#             if clean_word in misspelled:
#                 corrected_word = spell.correction(clean_word)
#                 self.misspelled_words.append((word, corrected_word))  # Store the misspelled and corrected words
#                 corrected_words.append(corrected_word)  # Correct word
#             else:
#                 corrected_words.append(word)  # No correction needed for this word

#         # Join the words back into a sentence
#         corrected_text = ' '.join(corrected_words)
        
#         # Perform grammar correction using TextBlob (after spellchecking)
#         blob = TextBlob(corrected_text)
#         corrected_text = blob.correct()  # Context-aware correction
        
#         return str(corrected_text)  # Convert the corrected blob back to string