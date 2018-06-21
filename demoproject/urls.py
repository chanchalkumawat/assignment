from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include('demoapp.urls')),
    path('admin/', admin.site.urls),
]