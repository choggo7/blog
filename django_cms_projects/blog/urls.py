from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^home/', views.home,name='home'),
    url(r'^posts/', views.post_all,name='all_posts'),
    url(r'^post/(\d+)?', views.post_id,name='post'),
    url(r'^tst', views.tst,name='tst'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

