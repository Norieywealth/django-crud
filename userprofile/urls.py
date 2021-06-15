from django.urls import path
from userprofile import views

app_name = 'profile'

urlpatterns = [
    path('', views.index, name='index'),
    path('payment/', views.payment, name='payment'),
    path('profile/', views.user_profile, name='profile'),
    path('edit/<int:id>', views.edit_profile, name='edit'),
    path('delete/<int:id>', views.delete_profile, name='delete'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
]
