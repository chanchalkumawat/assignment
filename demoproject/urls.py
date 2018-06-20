#
# from django.conf.urls import url,include
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^',include('demoapp.urls'))
# ]


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include('demoapp.urls')),
    path('admin/', admin.site.urls),
]