from django.contrib import admin
from TonysHardware_v2.hardware.models import RAMMemoryModel, AMDRadeonGPUModel, NvidiaGPUModel, CpuModel, StorageDriveModel, PsuModel


@admin.register(CpuModel)
class CpuAdmin(admin.ModelAdmin):
    pass


@admin.register(RAMMemoryModel)
class RamAdmin(admin.ModelAdmin):
    pass


@admin.register(AMDRadeonGPUModel)
class AMDRadeonGPUModelAdmin(admin.ModelAdmin):
    pass


@admin.register(NvidiaGPUModel)
class NvidiaGPUModelAdmin(admin.ModelAdmin):
    pass


@admin.register(StorageDriveModel)
class StorageDriveModelAdmin(admin.ModelAdmin):
    pass


@admin.register(PsuModel)
class PsuModelAdmin(admin.ModelAdmin):
    pass

