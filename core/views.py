def dashboard_view(request):
    return render(request, 'core/dashboard.html')
from django.shortcuts import render

from django.shortcuts import redirect

def home_view(request):
    return redirect('usuario:login')

# Create your views here.
