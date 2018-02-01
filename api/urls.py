from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserView, UserDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^datalists/$', CreateView.as_view(), name="create"),
    url(r'^datalists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'^users/(?P<pk>[0-9]+)/$',UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),

}

urlpatterns = format_suffix_patterns(urlpatterns)

"""
Format_suffix_pattern memungkinkan kita untuk menentukan 
format data (raw json atau bahkan html) 
saat kita menggunakan URL. 
Ini menambahkan format yang akan digunakan 
untuk setiap URL dalam polanya.
"""