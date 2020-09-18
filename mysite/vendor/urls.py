from django.urls import path

from . import views
app_name = 'vendors'
urlpatterns = [
    path('', views.VendorListView.as_view(), name="vendor_index"),
    path('create/', views.VendorCreateView.as_view(), name="vendor_create"), # 新增
    path('<int:pk>/', views.VendorDetailView.as_view(), name='vendor_id'),
    path('<int:pk>/update/', views.VendorUpdateView.as_view(), name='update'), # 新增
]