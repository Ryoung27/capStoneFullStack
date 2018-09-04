"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
# from . import views
# from .views import User_Viewset
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('user', User_Viewset, base_name='User')
# urlpatterns = router.urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^website/', include('website.urls')),
    # path('mysite/User', views.UserListCreate.as_view() )
    # url(r'^api-auth/', include('rest_framework.urls'))

]
