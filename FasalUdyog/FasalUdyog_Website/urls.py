from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register_farmer/", views.registerfarmer, name="registerfarmer"),
    path("check_stock/", views.checkstock, name="checkstock"),
    path("order/", views.order, name="order"),
    path("about_us/", views.about, name="about"),

]
