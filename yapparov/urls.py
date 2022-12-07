from type import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path("cre/",views.cre),
]
