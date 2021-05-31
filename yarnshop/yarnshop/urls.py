from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from .views import contact, main

app_name = "yarnshop"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('', main, name='index'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', contact, name='contact'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

