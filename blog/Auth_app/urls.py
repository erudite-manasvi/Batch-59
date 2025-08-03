
from django.urls import path

from .views import home,signup, data_view,sud_view

urlpatterns = [
    path('home/', home),
    path('signup/',signup),
    path('data/',data_view),
    path('sud/<int:pk>/',sud_view),
]
