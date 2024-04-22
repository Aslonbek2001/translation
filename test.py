from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Example usage:
text_to_translate = "Hello, how are you?"
target_language = "ky"  # "uz" stands for Uzbek language, you can use "kk" for Kazakh and "ky" for Kyrgyz
translated_text = translate_text(text_to_translate, target_language)
print("Translated text:", translated_text)
