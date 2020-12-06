from django.urls import path
from quiz import views
urlpatterns = [
    path('login', views.Login.as_view(), name="login"),
    path('dashboard', views.Dashboard.as_view(), name="dashboard"),
    path('', views.Main.as_view(), name="main"),
]