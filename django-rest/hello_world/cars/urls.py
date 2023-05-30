from django.urls import path

from .views import CarListAPI

urlpatterns = [path("", CarListAPI.as_view(), name="car-list")]
