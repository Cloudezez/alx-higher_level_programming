from django.contrib import admin
from django.urls import path
from myapp.views import route_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('route_3', route_3),
]

