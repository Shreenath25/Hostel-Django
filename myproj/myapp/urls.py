from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.view1),
    path("page1", views.view2),
    path("page2", views.view3),
    path("page3", views.view4),
    path("page4", views.view5),
]
