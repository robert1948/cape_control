from django.urls import path
from django.http import HttpResponse

# Placeholder view for testing
def placeholder_view(request):
    return HttpResponse("Hello, world!")

urlpatterns = [
    path('', placeholder_view, name='placeholder'),
]
