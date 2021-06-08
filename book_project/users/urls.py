from django.contrib.auth import urls
from  .views import  signUpPage
from django.urls import path
urlpatterns = [
    path('signup/',signUpPage.as_view(),name='signup')
]