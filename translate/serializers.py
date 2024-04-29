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
