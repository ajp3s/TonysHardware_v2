from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('TonysHardware_v2.common.urls')),
    path('accounts/', include('TonysHardware_v2.accounts.urls')),
    path('hardware/', include('TonysHardware_v2.hardware.urls')),

]
