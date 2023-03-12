from django.views.generic import TemplateView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Config, Suscriptor

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config'] = Config.objects.first()
        return context
    
def suscribe(request: HttpRequest):
    
    if request.method == 'POST':
        subscribe_email = request.POST['subscribe_email']
        try:
            Suscriptor.objects.create(email=subscribe_email)
        finally:
            return redirect('home')