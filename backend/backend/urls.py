
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views


router = routers.DefaultRouter()
router.register(prefix = r'todos', viewset = views.TodoView, basename = 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
