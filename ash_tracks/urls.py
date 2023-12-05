from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_me', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('news', views.news, name='news'),
]
