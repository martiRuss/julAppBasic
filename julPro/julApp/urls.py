from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("post", views.index, name="Post"),
    path("calculate/", views.calculate_dom, name="calculate_dom"),
]
