from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name = "home"),
    path("reg",views.reg, name = "reg"),
    path("cm",views.cm, name = "cm"),
    path("search_of_ingrid",views.search_of_ingrid, name = "search_of_ingrid")
]