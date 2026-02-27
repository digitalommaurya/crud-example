# records/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('', views.record_list, name='record_list'),
    path('add/', views.record_create, name='record_create'),
    path('<int:pk>/edit/', views.record_update, name='record_update'),
    path('<int:pk>/delete/', views.record_delete, name='record_delete'),
]