from django.urls import path

from staticapp import views
from staticproject import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.staticv,name="staticv"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)