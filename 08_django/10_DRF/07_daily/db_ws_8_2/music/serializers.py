from rest_framework import serializers
from .models import Music

class MusicListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title')

class MusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
