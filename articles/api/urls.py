from django.urls import path, include
from django.conf.urls import url
from .routers import router
from .viewsets import ArticleViewSets, MixDataViewSets, AllData
from .views import *
from articles.api.views import ArticlesDetailAPIView



urlpatterns = [
    path('tinymce/', include('tinymce.urls')),


    path('alldata/', AllData.as_view()),
    path('mixdata/', MixDataViewSets.as_view()),
    url(r'articles/(?P<pk>\d+)/', view=ArticlesDetailAPIView.as_view()),
    path('articles/(?P<pk>)/comments/', view=ArticleViewSets.as_view({'get':'comments', 'post':'comments'})),
    path('articles/(?P<pk>)/comments/(?P<comment>\d+)/', view=ArticleViewSets.as_view({'delete':'remove_comment'})),
    url(r'articles/(?P<pk>\d+)/comments/$', view=ArticleViewSets.as_view({'get':'comments', 'post':'comments'})),
    url(r'articles/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=ArticleViewSets.as_view({'delete':'remove_comment'})),
    url(r'articles-comments-reply/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=ArticleViewSets.as_view({'get':'reply_comment', 'post':'reply_comment', 'delete': 'remove_comment'})),
    url(r'articles-comments-remove/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=ArticleViewSets.as_view({'delete':'remove_comment'})),
    url(r'articles-comments/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=ArticleViewSets.as_view({'get':'reply_comment', 'post': 'reply_comment'})),
    
]

urlpatterns += router.urls
# urlpatterns += routerS.urls
