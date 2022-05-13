# for the urls file for the todo app
from django.urls import path
# this line means from this directory, import views
from . import views

urlpatterns = [
    # The views.home, the home can be anything specified in the view as the function
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('log', views.log, name='log'),
    path('edit', views.edit, name='edit'),
    path('profile', views.profile, name='profile'),
    path('sign', views.signup, name='signup'),
    # for the post request
    path('add_task', views.add_task, name='add_task'),
    # for the delete request
    path('delete', views.delete, name='delete'),
    # for the edit request
    path('edit', views.edit, name='edit')
]
