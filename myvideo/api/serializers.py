from rest_framework import serializers

from myvideo.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'image')
        read_only_fields = ('id',)
