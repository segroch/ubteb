from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
# path('index/', views.index, name = 'index'),
   # path('home/', views.home, name = 'home'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('add_alumni/', views.add_alumni , name='add_alumni'),
    path('edit_alumni/', views.edit_alumni , name='edit_alumni'),
    path('alumni_list', views.alumni , name='al_list'),
   # path('addAlu', views.addAlu , name='addAlu'),
]
