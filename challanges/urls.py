from django.urls import path
from . import views
# urlpatterns is a list
urlpatterns = [
    path("january",views.january),
    path("february",views.february)
]