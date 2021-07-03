"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include,path
from advisormgmt import views

urlpatterns = [
     path('', views.home, name='home'),
     path('upload/', views.upload,name='upload'),
     path('list_of_advisor/', views.list_of_advisor, name='list_of_advisor'),
     path('add_advisor/', views.add_advisor, name='add_advisor'),
     path('update_advisor/<str:pk>/', views.update_advisor, name="update_advisor"),
     path('delete_advisor/<str:pk>/', views.delete_advisor, name="delete_advisor"),
     path('advisor_detail/<str:pk>/', views.advisor_detail, name="advisor_detail"),
     path('advisor_history/', views.advisor_history, name='advisor_history'),
     path('admin/', admin.site.urls),
     path('accounts/', include('registration.backends.default.urls')),

]

