from rest_framework import serializers
from drf_yasg import openapi

class TranslateSerializer(serializers.Serializer):
    target_language = serializers.CharField(required=True, max_length=10)
    text = serializers.CharField(required=True, max_length=500)

    class Meta:
        swagger_schema_fields = {
            "required": ["target_language", "text"],
            "type": "object",
            "properties": {
                "target_language": {
                    "type": "string",
                    "maxLength": 10,
                    "description": "The target language for translation (e.g., 'en' for English)",
                },
                "text": {
                    "type": "string",
                    "maxLength": 500,
                    "description": "The text to be translated",
                },
            },
        }

class DocumentSerializer(serializers.Serializer):
    target_language = serializers.CharField(required=True, max_length=10)
    text = serializers.CharField(required=True, max_length=500)
    class Meta:
        extra_kwargs = {
            'target_language': {'required': True},
            'text': {'required': False}
        }

class StarsSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=30, default="User", required=False)
    stars = serializers.IntegerField(min_value=1, max_value=5, required=True)
    comment = serializers.CharField(max_length=200, required=False)


class FAQ_Serializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100, required=True)
    question = serializers.CharField(max_length=500, required=True)

    class Meta:
        extra_kwargs = {
            'full_name': {'required': True},
            'question': {'required': False}
        }

