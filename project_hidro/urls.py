
from django.contrib import admin
from django.urls import path,include

from .views import Landing, Contacto, QuienesSomos, Sales, ShowData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Landing.as_view(), name="landing"),
    path('contacto/', Contacto.as_view(), name="contacto"),
    path('quienes_somos/', QuienesSomos.as_view(), name="quienes_somos"),
    path('sales/', Sales.as_view(), name="sales"),
    path("productos/", include("app_hidro.urls")),
    path("show_data/", ShowData.as_view(), name="show_data"),
    
]
