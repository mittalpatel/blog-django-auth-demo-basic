from django.contrib import admin
from django.urls import path
from users.views import register_user, login_user # New

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_user),
    path('login/', login_user), # New
]
