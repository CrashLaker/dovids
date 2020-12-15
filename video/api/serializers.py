from rest_framework import serializers
from video.models import VideoFile


class VideoSerializer(serializers.Serializer):

    video = serializers.FileField()

    class Meta:
        model = VideoFile
        fields = ('id', 'title', 'video')
        read_only_fields = ('id',)
