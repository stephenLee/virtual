from django.conf.urls import patterns

urlpatterns = patterns('', 
    (r'^$', 'weibo.views.home'),
    (r'^auth', 'weibo.views.auth'),
    (r'^visualization', 'weibo.views.visualization'),
    (r'^data', 'weibo.views.json_test'),
)
