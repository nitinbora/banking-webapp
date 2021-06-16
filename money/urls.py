
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('customer',views.custo,name='custo'),
    path('profile',views.profile,name='profile'),
    path("profile/<int:cusid>", views.profile, name="profile"),
    path('profile/transfer/<int:cusid>/<int:amount>',views.transfer,name='transfer'),
    path('profile/window',views.window,name='window'),
    
   

]