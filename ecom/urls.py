"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import send_verification_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('join/', views.join, name='join'),
    path('joincourse/', views.join_course, name='join_course'),
    path('read-more/', views.read_more, name='read_more'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('api/verify-email/', views.verify_email, name='verify_email'),
    path('api/send-verification-email/', send_verification_email, name='send_verification_email'),
    path('wtf/', views.wtf, name='wtf'),
    path('userpage/', views.userpage, name='userpage'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
# handler404 = 'ecom.views.custom_404_view'