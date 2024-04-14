"""vente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include,re_path
from gestion.views import home,CommandeCreateView,recup,search
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path('commande/<int:id_article>', CommandeCreateView.as_view(), name='commande'),
    path('afficher/<int:id_commande>/', recup, name='afficher'),
    path("auth/",include("app_auth.urls")),
    path("my-admin/",include("app_admin.urls")),
    path("article/recherche",search,name="search"),# tu vas dans article tu va cliquer sur recherche et on va appeler la fonctions search depuis views
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT} ), # pour les fichiers de MEDIA
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT} ), # pour les fichiers de STATIC
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # obligatoire 
