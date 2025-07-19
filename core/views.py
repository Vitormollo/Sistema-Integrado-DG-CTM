def dashboard_view(request):
    return render(request, 'core/dashboard.html')
from django.shortcuts import render

def home_view(request):
    return render(request, 'core/home.html')

# Create your views here.
