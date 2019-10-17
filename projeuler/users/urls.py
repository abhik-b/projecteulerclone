from django.urls import path, include
from .views import homeView, SignUp, profileView
app_name = 'users'
urlpatterns = [
    path('', homeView, name='homeView'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile', profileView, name='profile')

]
