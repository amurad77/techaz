from django.urls import path, include, re_path
from django.conf.urls import url
from .routers import router
from .viewsets import ArticleViewSets, MixDataViewSets, AllData
from .views import *
from articles.api.views import ArticlesDetailAPIView



urlpatterns = [
    path('tinymce/', include('tinymce.urls')),


    path('alldata/', AllData.as_view()),
    path('mixdata/', MixDataViewSets.as_view()),
    re_path(r'^articles/(?P<pk>\d+)/$', view=ArticlesDetailAPIView.as_view()),
    re_path(r'^articles/(?P<pk>)/comments/$', view=ArticleViewSets.as_view({'get':'comments', 'post':'comments'})),
    re_path(r'^articles/(?P<pk>)/comments/(?P<comment>\d+)/$', view=ArticleViewSets.as_view({'delete':'remove_comment'})),
    # re_path(r'^articles/(?P<pk>\d+)/comments/$', view=ArticleViewSets.as_view({'get':'comments', 'post':'comments'})),
    # re_path(r'^articles/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=ArticleViewSets.as_view({'delete':'remove_comment'})),
    re_path(r'^articles-comments-reply/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=ArticleViewSets.as_view({'get':'reply_comment', 'post':'reply_comment', 'delete': 'remove_comment'})),
    re_path(r'^articles-comments-remove/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=ArticleViewSets.as_view({'delete':'remove_comment'})),
    re_path(r'^articles-comments/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=ArticleViewSets.as_view({'get':'reply_comment', 'post': 'reply_comment'})),
    
]

urlpatterns += router.urls
# urlpatterns += routerS.urls
