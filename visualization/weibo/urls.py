from django.conf.urls import patterns

urlpatterns = patterns('', 
    (r'^$', 'weibo.views.home'),
    (r'^auth', 'weibo.views.auth'),
    (r'^json_test', 'weibo.views.json_test'),
    (r'^xhr_test', 'weibo.views.xhr_test'),
    (r'^visualization', 'weibo.views.visualization'),
    (r'^data', 'weibo.views.json_test'),
)
