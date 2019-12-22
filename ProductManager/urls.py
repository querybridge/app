from django.contrib import admin
from django.urls import path
from .views import ProductManagerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ProductManager/admin/', ProductManagerView.as_view(), name='product_manager')
]
