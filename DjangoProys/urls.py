"""DjangoProys URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DjangoProys import views as local_views
from django.conf.urls.static import static
from django.conf import settings

from posts import views as posts_views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('hello-world', local_views.hello_word),
    path('read-params', local_views.read_params),
    path('difparams/<str:name>/<int:age>', local_views.difparams),

    path('posts/', posts_views.list_posts),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
