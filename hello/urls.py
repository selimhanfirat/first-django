from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("selimhan", views.selimhan, name = "selimhan"),
    path("<str:name>", views.greet, name = "greet")
]
