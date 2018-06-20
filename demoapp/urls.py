# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from . import views
#
# urlpatterns = [
#     url(r'^users/$', views.UserList.as_view()),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#     url(r'^users/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$', views.UserDetail.as_view()),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user'),
    # path('<int:pk>/', views.UserDetail.as_view(), name='detail'),
    # path('<slug:data>', views.UserFilter.as_view()),
   ]