from django.conf.urls import url
# from website import views
from . import views
from django.conf import settings
from django.conf.urls.static import static




app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('login', views.login_user, name='login'),
    url(r'logout$', views.user_logout, name='logout'),
    url(r'register$', views.register, name='register'),
    url(r'day_view$', views.day_view, name='day_view'),
    url(r'schedule_view$', views.schedule_view, name='schedule_view'),
    url(r'user_view$', views.user_view, name="user_view"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
