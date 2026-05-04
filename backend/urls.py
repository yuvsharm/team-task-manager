from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ProjectViewSet, TaskViewSet, CustomLoginView
from django.http import HttpResponse
from django.shortcuts import render

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)


def home(request):
    return HttpResponse("API is running ")


def ui(request):
    return render(request, "core/index.html")


urlpatterns = [
    path('', ui),

    path('admin/', admin.site.urls),

    path('api/login/', CustomLoginView.as_view()),

    path('api/', include(router.urls)),
]