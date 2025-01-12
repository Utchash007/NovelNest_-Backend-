from rest_framework import serializers
from .models import *
class BookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
class Read_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadHistory
        fields = '__all__'