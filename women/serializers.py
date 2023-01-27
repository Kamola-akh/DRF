from rest_framework import serializers
from .models import WomenPost


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomenPost
        fields = ('id', 'title', 'content', 'img')