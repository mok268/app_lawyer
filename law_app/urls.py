from django.urls import path
from law_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('elements/', views.elements, name='elements'),
    path('contact/', views.contact, name='contact'),

]