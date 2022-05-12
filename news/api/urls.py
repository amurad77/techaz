
from django.urls import path, include
from django.conf.urls import url
from .routers import router
from .viewsets import NewsViewSets

from news.api.views import NewsDetailAPIView




urlpatterns = [
    path('tinymce/', include('tinymce.urls')),

    url(r'news/(?P<pk>\d+)/', view=NewsDetailAPIView.as_view()),
    # path('news/<int:pk/', NewsViewSets.as_view({'get': 'list'}), name = 'news_detail'),
    url(r'news/(?P<pk>\d+)/comments/$', view=NewsViewSets.as_view({'get':'comments', 'post':'comments'})),
    url(r'news/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=NewsViewSets.as_view({'delete':'remove_comment'})),
    url(r'news-comments-reply/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=NewsViewSets.as_view({'get':'reply_comment', 'post':'reply_comment', 'delete': 'remove_comment'})),

]

urlpatterns += router.urls