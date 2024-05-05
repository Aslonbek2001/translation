from googletrans import Translator
from docx import Document
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



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
    main_path = 'media/file.docx'
    document.save(main_path)
    path = os.path.join(main_path)
    print(path + ' created')
    return  path








