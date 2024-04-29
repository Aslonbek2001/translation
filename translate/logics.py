from googletrans import Translator
from docx import Document


def detect_text(text: str):
    translator = Translator()
    detected_language = translator.detect(text)
    return detected_language.lang

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


def text_docx(text):
    document = Document()
    document.add_paragraph(text)
    document.save('file.docx')
    return document

doc = text_docx("Salom")
print(doc)

