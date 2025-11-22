from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse, HttpResponse

def home(request):
    return JsonResponse({
        "message": "API Running",
        "status": "success"
    })

def favicon_view(request):
    return HttpResponse(status=204)

urlpatterns = [
    path('', home),
    path('favicon.ico', favicon_view),
    path('admin/', admin.site.urls),

    # ✅ Use dashboard (your real app)
    path('api/', include('dashboard.urls')),
]
