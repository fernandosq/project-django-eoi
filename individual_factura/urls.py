from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path("factura/", views.factura, name="general"),
    path("factura/<int:pk>", views.linea, name="linea"),

]