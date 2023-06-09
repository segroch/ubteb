from django.urls import path, include
from .import views
from ubiteb.views import *
from django.contrib.auth import views as auth_views
from django.urls import re_path as url
from rest_framework import routers

router = routers.DefaultRouter()


#API
router.register(r'alumni',AlumniViewSet, basename='alumni' )

urlpatterns = [

# path('index/', views.index, name = 'index'),
   # path('home/', views.home, name = 'home'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('add-alumni/', views.add_alumni , name='add_alumni'),
    path('edit-alumni/', views.edit_alumni , name='edit_alumni'),
    path('alumni-list/', views.alumni , name='al_list'),
    #path('upload-csv/', views.upload_csv, name='upload_csv'),
    #path('upload-csv/', CsvUploader.as_view(), name='upload-csv'),
    path('api/', include(router.urls), name='api'),
    url('^csv-uploader/$', CsvUploader.as_view(), name='csv-uploader'),
   # path('upload-csv', views.upload , name='upload'),
]
