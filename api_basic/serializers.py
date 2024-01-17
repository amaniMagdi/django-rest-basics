from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    auther = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateField()

    def create(self, validated_data):
        #return super().create(validated_data)
        return Article.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        #return super().update(instance, validated_data)
        instance.title = validated_data.get('title', instance.title)
        instance.auther = validated_data.get('title', instance.auther)
        instance.email = validated_data.get('title', instance.email)
        instance.date = validated_data.get('title', instance.date)
        instance.save
        return instance
