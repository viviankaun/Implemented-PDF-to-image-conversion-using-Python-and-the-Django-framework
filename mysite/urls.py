"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('wefunder/', include('wefunder.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('', views.Home.as_view(), name='home'),
    path('core/', views.core_list, name='core_list'),
    path('core/upload/', views.upload_core, name='upload_core'),
    path('core/<int:pk>/', views.delete_core, name='delete_core'),
    path('core_detail/<int:pk>/', views.core_detail, name='core_detail'),

    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
