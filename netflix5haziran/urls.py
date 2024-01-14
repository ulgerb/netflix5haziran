"""
URL configuration for netflix5haziran project.

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
from appMy.views import *
from appUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # email
    path('emailsend', emailSendPage, name='emailSendPage'),
    # path('usermySave/<username>/<randomlink>', usermySave, name='usermySave'),
    
    path('emailactive/<elink>', emailActive, name='emailActive'),

    
    path('', indexPage, name='indexPage'),
    path('browsePage/<pid>', browsePage, name='browsePage'),
    path('browsePage', browsePage, name='browsePage2'),
    path('profilePage', profilePage, name='profilePage'),
    path('profileDelete/<pid>', profileDelete, name='profileDelete'), # Profile Delete
    path('profileBrowse/<pid>', profileBrowse, name='profileBrowse'), # Profile Browse
    path('hesapPage', hesapPage, name='hesapPage'),
    path('videoPage', videoPage, name='videoPage'),
    # USER
    path('loginPage', loginPage, name='loginPage'),
    path('registerPage', registerPage, name='registerPage'),
    path('logoutUser', logoutUser, name='logoutUser'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
