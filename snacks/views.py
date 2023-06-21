from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView
from .models import Snack

# Create your views here.
class home_view_Page(TemplateView):
    template_name = 'home.html'

class about_view_Page(TemplateView):
    template_name = 'about.html'
 
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snack_list'

class snack_detail_View(DetailView):
    template_name="snack_detail.html"
    model = Snack
