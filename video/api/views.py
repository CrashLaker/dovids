from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from video.api.serializers import VideoSerializer


class VideoViewSet(ViewSet):

    serializer_class = VideoSerializer

    def list(self, request):
        return Response("GET API")


    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = f"POST API and you have uploaded a {content_type} file"
        return Response(response)
