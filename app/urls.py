from django.urls import path
from app.views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),    
    path("search_by_location/", search_location, name="search_location"),
]




 