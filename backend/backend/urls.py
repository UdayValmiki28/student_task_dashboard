"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse, HttpResponse

# ✅ Simple homepage for Render
def home(request):
    return JsonResponse({
        "message": "✅ Student Task Dashboard API is live and running!",
        "status": "success"
    })

# ✅ Handles /favicon.ico requests to avoid 400 errors
def favicon_view(request):
    return HttpResponse(status=204)  # No Content

urlpatterns = [
    path('', home),  # Homepage route
    path('favicon.ico', favicon_view),  # Favicon fix
    path('admin/', admin.site.urls),
]
