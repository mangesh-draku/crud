from rest_framework import serializers
from .models import movies

class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movies
        fields = ["name","img","summary"]