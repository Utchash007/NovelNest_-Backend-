from rest_framework import serializers
from .models import Novel,User,NovelChapter

class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = '__all__'  # You can list specific fields instead of '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # You can list specific fields instead of '__all__'

class NovelChaptersSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovelChapter
        fields = '__all__'

class NovelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovelChapter
        exclude = ['cpt_text']



