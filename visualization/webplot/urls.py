from django.conf.urls import patterns

urlpatterns = patterns('', 
    (r'^$', 'webplot.views.graph'),
    (r'^test_networkx', 'webplot.views.draw_network'),
    (r'^force', 'webplot.views.force'),
)
