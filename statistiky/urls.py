from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile-info/<id>', views.profile_info, name='profile')

]
urlpatterns += staticfiles_urlpatterns()
