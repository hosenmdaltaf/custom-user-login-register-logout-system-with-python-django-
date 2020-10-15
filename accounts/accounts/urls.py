
from django.urls import path
from django.contrib import admin


from accounts.views import (
    home,
    registration_view,
    logout_view,
    login_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home , name="home"),
    path('register/', registration_view, name="register"),
    path('login/',login_view,name="login"),
    path('logout/', logout_view, name="logout"),
   
]
