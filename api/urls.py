from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router=routers.DefaultRouter(trailing_slash=False)
router.register('users', views.UserList)
urlpatterns = [
    path('api', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view()),
    path('reminders', views.ReminderList.as_view()),
    path('upload', views.FileList.as_view())
]
