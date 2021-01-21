from django.urls import path,include
from . import views


urlpatterns = [
    path('registration/', views.registration),
    path('login/',views.user_login,name="login")
]

