from django.contrib import admin
from django.urls import path
from ToLet_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.property_list, name='property_list'),
    path('add/', views.property_create, name='property_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

