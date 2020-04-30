from .views import GoogleView, HelloView, FacebookView
from django.urls import path
urlpatterns = [
    path('social/', HelloView.as_view()),
    path('social/authenticate/google', GoogleView.as_view()),
    path('social/authenticate/facebook', FacebookView.as_view())
]
