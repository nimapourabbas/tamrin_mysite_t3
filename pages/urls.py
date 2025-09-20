from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.home_view),
    path('about/',views.home_about),
]