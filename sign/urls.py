from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login),
    url(r'^test/$', views.test),
    url(r'^test2/$', views.test2)
]