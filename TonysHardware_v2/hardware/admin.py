from django.contrib import admin
from TonysHardware_v2.hardware.models import RAMMemory, AMDRadeonGPU, NvidiaGPU, Cpu, StorageDrive, Psu


@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    pass


@admin.register(RAMMemory)
class RamAdmin(admin.ModelAdmin):
    pass
