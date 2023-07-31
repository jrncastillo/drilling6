from django.urls import path
from .  import views

urlpatterns = [
    #path('', views.IndexPageView.as_view(), name='index'),
    path('add', views.add_view, name='add'),
    path('login', views.login_view, name='login'),
    path('signin', views.signin_view, name='signin'),
    path('logout', views.logout_view, name='logout'),
    path('lista', views.lista_view, name='lista'),
    
]