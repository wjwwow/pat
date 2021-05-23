from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='home'),
    path('login/',views.login_page,name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("findpwd/",views.findpsView,name='findpwd'),
    path("register/",views.register,name='register'),
    path('change/',views.modify_pwd,name='change'),
    path('dog/',views.dog,name='dog'),
    path('cat/',views.cat,name='cat'),
    path('dog/<str:pk>/',views.dog_detail,name='dog_detail'),
    path('cat/detail/<str:pk>/', views.cat_detail, name='cat_detail'),
    path('dog/detail/<str:pk>/', views.dog_detail, name='dog/dog/detail/30/_detail'),
    path('userinfo/<str:id>/',views.userinfo,name='userinfo'),
    path('tx/<str:id>/',views.xgtx,name='tx')
]