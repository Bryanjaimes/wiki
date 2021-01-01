from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.getpage, name = "getpage"),
    path("search", views.search, name = "search"),
    path("random", views.random, name = "random"),
    path("newpage", views.newpage, name = "newpage"),
    path("editpage/<str:title>", views.editpage, name = "editpage")
]
  