from django.urls import path

from . import views

urlpatterns = [
    path('',views.user_home,name='user_home'),
    path('profile_show/',views.profile_show,name='profile_show'),
    path('editdetails/<int:pk>',views.editdetails,name='editdetails'),
    path('edituser/<int:pk>',views.edituser,name='edituser'),
    path('show_product/',views.show_product,name='show_product'),
    path('single_product/',views.single_product,name="single_product"),

    path('pro/',views.pro,name='pro'),
    # path('userapp_logout',views.userapp_logout,name='userapp_logout'),

]