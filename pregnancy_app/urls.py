
from django.urls import path
from .import views
urlpatterns = [
    path("",views.home,name='home'),
    path("login/",views.LoginPage,name="login"),
    path('signup/',views.SignupPage,name="signup"),
    path('logout/',views.LogoutPage,name="logout"),
    path('biohome/',views.BioHome,name="Biohome"),
]