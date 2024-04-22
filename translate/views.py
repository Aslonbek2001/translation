from django.shortcuts import render
from .logics import translate_text
from django.views import View

class TranslateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        text_to_translate = request.POST['text']
        target_language = request.POST['target_language']
        translated_text = translate_text(text_to_translate, target_language)

        data = {
            'translated_text': translated_text,
        }

        return render(request, 'index.html', context=data)


