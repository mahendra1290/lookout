from django.urls import path

from .views import HomePageView, AboutPageView, LoginPageView, SignupPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignupPageView.as_view(), name='signup'),
]