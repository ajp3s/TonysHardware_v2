from django.urls import path

urlpatterns =[
    path('create/<str:model>/', HardwareCreateView.as_view(), name = 'create'),
    path('update/<str:model>/<int:pk>/', HardwareUpdateView.as_view(), name='update'),
    path('details/<str:model>/<int:pk>/', HardwareDetailView.as_view(), name='details'),
    path('delete/<str:model>/<int:pk>/', HardwareDeleteView.as_view(), name='delete'),
    path('list/<str:model>/', HardwareListView.as_view(), name='listHardware')
]
