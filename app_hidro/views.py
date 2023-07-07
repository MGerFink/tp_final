from django.urls import reverse_lazy
from .models import Producto
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

class ProductosBaseView(View):
    template_name   ="productos.html"
    model           = Producto
    fields          ="__all__"
    success_url     = reverse_lazy("productos:all")

class ProductosList(ProductosBaseView, ListView):
    ...

class ProductosDetail(ProductosBaseView, DetailView):
    template_name="producto_detail.html"
   
class ProductosCreate(ProductosBaseView, CreateView):
    template_name = "producto_create.html"
extra_content = {
        "tipo" : "Crear Producto"

    }

class ProductosUpdate(ProductosBaseView, UpdateView):
    template_name = "producto_update.html"
    extra_content = {
        "tipo" : "Actualizar Producto"

    }

class ProductosDelete(ProductosBaseView, DeleteView):
    template_name = "producto_delete.html"
    extra_content = {
        "tipo" : "Borrar Producto"

    }

