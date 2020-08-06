from django.conf.urls import url
from trial import views
 
urlpatterns = [
    url(r'^api/trial$', views.trial_list),
    url(r'^api/trial/(?P<pk>[0-9]+)$', views.trial_detail),
    url(r'^api/trial/published$', views.trial_list_published)
]



# Create your views here.
