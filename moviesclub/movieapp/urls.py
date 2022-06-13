from . import views
from django.urls import path

urlpatterns=[
    path("",views.crud),
    path("<int:pk>",views.crudsingle),
]