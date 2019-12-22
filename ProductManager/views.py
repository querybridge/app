from django.shortcuts import render
from .models import Wheel
from django.views.generic import TemplateView



# Create your views here.

class ProductManagerView(TemplateView):
    model = Wheel
    template_name = "productmanager/product_add.html"
