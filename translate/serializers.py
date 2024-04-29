from rest_framework import serializers

class TranslateSerializer(serializers.Serializer):
    target_language = serializers.CharField(required=True, max_length=10)
    text = serializers.CharField(required=True, max_length=500)
