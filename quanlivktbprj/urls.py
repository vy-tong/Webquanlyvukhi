"""
URL configuration for quanlivktbprj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from vktbapp import views



from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.viewpage, name='base'),
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('vukhi/', views.vukhipage, name='vukhi'),
    path('trangbi/', views.trangbipage, name='trangbi'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logout_func, name='logout'),
    path('profile/', views.profilepage, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
