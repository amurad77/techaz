from articles.models import Articles
from articles.api.serializers import ArticleSerializers
from rest_framework.generics import RetrieveAPIView

class ArticlesDetailAPIView(RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = "slug"