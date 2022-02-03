# from .serializers import *
# from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions, ac
# from ..models import News

# class NewsViewSet(ModelViewSet):
#     permission_classes = [permissions.AllowAny,]
#     queryset = News.objects.filter(is_published=True)
#     serializer_class = NewsSerializers



from news.models import News
from news.api.serializers import NewsSerializers
from rest_framework.generics import RetrieveAPIView

class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    lookup_field = "slug"