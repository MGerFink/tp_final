from django.urls import path

from .views import ProductosList\
                              ,ProductosDetail\
                                ,ProductosCreate\
                                  ,ProductosUpdate\
                                      ,ProductosDelete

app_name = "productos"

urlpatterns = [
    path("", ProductosList.as_view(), name = "all"),
    path("<int:pk>/detail/", ProductosDetail.as_view(), name = "detail"),
    path("create/", ProductosCreate.as_view(), name = "create"),
    path("<int:pk>/update/", ProductosUpdate.as_view(), name = "update"),
    path("<int:pk>/delete/", ProductosDelete.as_view(), name = "delete"),
]