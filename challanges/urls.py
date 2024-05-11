from django.urls import path
from . import views
# urlpatterns is a list
urlpatterns = [
    path("january",views.index),
    path("february",views.february)
]