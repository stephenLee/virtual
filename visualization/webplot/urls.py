from django.conf.urls import patterns

urlpatterns = patterns('', 
    (r'^$', 'webplot.views.graph'),
)
