from django.conf.urls import url
from . import views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todo.views import CustomLoginView

app_name = 'todo'

urlpatterns = [
    # /todo/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /todo/71/
    url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name='detail'),
    # /todo/list/add/
    url(r'list/add/$', views.ListCreate.as_view(), name='list-add'),

    # /todo/list/2/
    url(r'list/(?P<pk>[0-9]+)/$', views.ListUpdate.as_view(), name='list-update'),

    # /list/album/2/delete/
    url(r'list/(?P<pk>[0-9]+)/delete/$', views.ListDelete.as_view(), name='list-delete'),

    url(r'^login/$', views.CustomLoginView.as_view(),name='login'),
    
     
]  