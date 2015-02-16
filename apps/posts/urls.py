from django.conf.urls import patterns, url

urlpatterns = patterns(
    'posts.views',
    url(r'^$', 'post_list_view', name='list'),
    url(r'^post/like/$', 'like_view', name='like'),
)
