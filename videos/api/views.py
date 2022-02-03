# from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
# from .serializers import *
# from ..models import *

# class VideoViewSet(ModelViewSet):
#     permission_classes = [permissions.AllowAny,]
#     queryset = Video.objects.filter(is_published=True)
#     serializers = {
#         'list': VideoSerializers,
#         'default': VideoCreateSerializers
#     }
    
#     def get_serializer_class(self):
#         return self.serializers.get(self.action, self.serializers.get('default'))


from videos.models import Video
from videos.api.serializers import VideoSerializers
from rest_framework.generics import RetrieveAPIView

class VideoDetailAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    lookup_field = "slug"