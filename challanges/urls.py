from django.urls import path
from . import views
# urlpatterns is a list
urlpatterns = [
    path("<int:month>",views.monthly_challange_number),
    path("<str:month>",views.monthly_challanges, name="month-challanges")
]