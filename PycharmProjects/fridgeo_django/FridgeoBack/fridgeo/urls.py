from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='startpage'),
    path('secondpage/', views.HelloThere, name='seconpage'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('information/', views.information, name='information'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account')
]
