from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/update/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("user_profile/<int:pk>/",views.user_profile,name="profile")
]