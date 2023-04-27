from django.urls import path
from userinfo import views

urlpatterns = [

    path('user',views.users,name="users"),
]