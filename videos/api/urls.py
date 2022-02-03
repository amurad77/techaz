from .routers import router
from .viewsets import *
from django.conf.urls import url

from videos.api.views import VideoDetailAPIView


url(r'video/(?P<pk>\d+)/', view=VideoDetailAPIView.as_view()),
urlpatterns = [ 
    url(r'videos/(?P<pk>\d+)/comments/$', view=VideoViewSet.as_view({'get':'comments', 'post':'comments'})),
    url(r'videos/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=VideoViewSet.as_view({'delete':'remove_comment'})),
    url(r'videos-comments-reply/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', view=VideoViewSet.as_view({'get':'reply_comment', 'post':'reply_comment', 'delete': 'remove_comment'})),
]

urlpatterns += router.urls