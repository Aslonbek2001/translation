from django.http import JsonResponse
from django.shortcuts import render
from .logics import translate_text, detect_text, text_docx
from rest_framework import status
from .serializers import TranslateSerializer, DocumentSerializer, StarsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Stars



class IndexView(APIView):
    def get(self, request):
        count = Stars.objects.all().count()
            
        stars = Stars.objects.all()
        surat = 0
        for item in stars:
            surat += item.stars
        
        if count == 0:
            data = {
                'stars': surat/1,
                'srars_count': count,
            }
        else:
            data = {
                'stars': surat/count,
                'srars_count': count,
            }

        return Response(data, status=status.HTTP_200_OK)
   


def index(request):
    
    if request.method == 'GET':
        count = Stars.objects.all().count()
            
        stars = Stars.objects.all()
        surat = 0
        for item in stars:
            surat += item.stars
        
        if count == 0:
            data = {
                'stars': surat/1,
                'srars_count': count,
            }
        else:
            data = {
                'stars': surat/count,
                'srars_count': count,
            }

        return JsonResponse(data, status=status.HTTP_200_OK)


class TranslateView(APIView):
    def post(self, request):
        serializer = TranslateSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            target_language = serializer.validated_data['target_language']
            language_old = detect_text(text)

            if language_old == target_language:
                answer = {
                        'old_text': text,
                        'language': target_language,
                        'translated_text': text
                    }
                return Response(answer, status=status.HTTP_200_OK)

            if language_old == 'kk' or language_old == 'ky' or language_old == 'uz':

                if target_language == 'kk' or target_language == 'ky' or target_language == 'uz':
                    answer = {
                        'old_text': text,
                        'language': target_language,
                        'translated_text': translate_text(text=text, target_language=target_language)
                    }
                    return Response(answer, status=status.HTTP_200_OK)
                else:
                    message = "Error: 'target_language' is not True"
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                message = "Error: 'Language' is not True"
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(" Xatolik ", status=status.HTTP_400_BAD_REQUEST)
    

class DocumentView(APIView):
    def post(self, request):
        serializer = TranslateSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            target_language = serializer.validated_data['target_language']
            language_old = detect_text(text)

            if language_old == target_language:
                
                docs = text_docx(text=text)
                
                answer = {
                    'old_text': text,
                    'language': target_language,
                    "docs": docs,
                    'translated_text': text
                    }
                return Response(answer, status=status.HTTP_200_OK)

            if language_old == 'kk' or language_old == 'ky' or language_old == 'uz':

                if target_language == 'kk' or target_language == 'ky' or target_language == 'uz':
                    
                    translated_text =  translate_text(text=text, target_language=target_language)
                    docs = text_docx(text=translated_text)

                    answer = {
                        'old_text': text,
                        'language': target_language,
                        'docs': docs,
                        'translated_text': translated_text
                    }
                    return Response(answer, status=status.HTTP_200_OK)
                else:
                    message = "Error: 'target_language' is not True"
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                message = "Error: 'Language' is not True"
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(" Xatolik ", status=status.HTTP_400_BAD_REQUEST)


class StarsApiView(APIView):
    def post(self, request):
        serializer = StarsSerializer(data=request.data)

        if serializer.is_valid():
            stars = serializer.validated_data['stars']
            comment = serializer.validated_data['comment']

            if stars > 5 or stars < 1:
                message = "Error: 'Stars' is not True"
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                Stars.objects.create(stars=stars, comment=comment)
                answer = {
                    'stars': stars,
                    'comment': comment
                }
                return Response(answer, status=status.HTTP_200_OK)
