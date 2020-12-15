from rest_framework.decorators import action
from rest_framework import viewsets, mixins, status
from myvideo.api.serializers import RecipeSerializer
from myvideo.models import Recipe




class RecipeViewSet(viewsets.ModelViewSet):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    
    #@action(methods=['POST'], detail=True, url_path='upload-image')
    @action(methods=['POST'], detail=True)
    def upload_image(self, request, pk=None):
        recipe = self.get_object()
        serializer = RecipeSerializer(
            recipe,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            )
