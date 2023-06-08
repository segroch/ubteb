from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
# path('index/', views.index, name = 'index'),
   # path('home/', views.home, name = 'home'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('add-alumni/', views.add_alumni , name='add_alumni'),
    path('edit-alumni/', views.edit_alumni , name='edit_alumni'),
    path('alumni-list/', views.alumni , name='al_list'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    #path('add-csv/', views.add_csv, name='add_csv'),
   # path('upload-csv', views.upload , name='upload'),
]
