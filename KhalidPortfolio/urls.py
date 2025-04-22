from django.contrib import admin
from django.urls import path
from KhalidPortfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.KhalidPortfolio_view, name='home'),  # Add this for the root path
    path('About/', views.About, name='About'), 
     path('contact/', views.contact, name='contact'), # About page
     path('credentials/', views.credentials, name='credentials'), # Credentials page
     path('Home/', views.Home, name='Home'),
     path('MyOffering/', views.MyOffering, name='MyOffering'), 
     path('WorkDetails/', views.WorkDetails, name='WorkDetails'),
      path('ProjectList/', views.ProjectList, name='ProjectList') # My Offerings page

]