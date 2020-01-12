from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('textpost/', views.text_post, name='textpost')
]