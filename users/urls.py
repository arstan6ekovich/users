from django.urls import path, include
from rest_framework import routers
from .views import UserView

router = routers.DefaultRouter()

router.register(r'', UserView, basename='user_list')

urlpatterns = [
    path('', include(router.urls))
]
