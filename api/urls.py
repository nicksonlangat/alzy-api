from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from .views import CustomObtainAuthToken


router=routers.DefaultRouter(trailing_slash=False)
# router.register('users', views.UserList)
urlpatterns = [
    # path('api', include(router.urls)),
    
    path('reminders', views.ReminderList.as_view()),
    path('upload', views.FileList.as_view()),
    path('', views.index),
    path('api/users', views.UserView.as_view()),
    path('authenticate', CustomObtainAuthToken.as_view()),
]
