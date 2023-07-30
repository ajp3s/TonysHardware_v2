from django.urls import path

from TonysHardware_v2.hardware.views import HardwareAddView, HardwareUpdateView, HardwareDetailView, \
    HardwareDeleteView, HardwareListView

urlpatterns = [
    path('create/<str:model>/', HardwareAddView.as_view(), name='add_hardware'),
    path('update/<str:model>/<int:pk>/', HardwareUpdateView.as_view(), name='edit_hardware'),
    path('details/<str:model>/<int:pk>/', HardwareDetailView.as_view(), name='details_hardware'),
    path('delete/<str:model>/<int:pk>/', HardwareDeleteView.as_view(), name='delete_hardware'),
    path('list/<str:model>/', HardwareListView.as_view(), name='list_hardware')
]
