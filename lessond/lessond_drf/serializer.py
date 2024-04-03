from rest_framework import serializers
from .models import NewsModel, NewsModelFirst, NewsModelSecond, NewsModelThird

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = (
            'id',
            'add_date',
            'title',
            'text'
        )

class NewsSerializerFirst(serializers.ModelSerializer):
    class Meta:
        model = NewsModelFirst
        fields = (
            'id',
            'add_date',
            'title',
            'text'
        )

class NewsSerializerSecond(serializers.ModelSerializer):
    class Meta:
        model = NewsModelSecond
        fields = (
            'id',
            'add_date',
            'title',
            'text'
        )

class NewsSerializerThird(serializers.ModelSerializer):
    class Meta:
        model = NewsModelThird
        fields = (
            'id',
            'add_date',
            'title',
            'text'
        )