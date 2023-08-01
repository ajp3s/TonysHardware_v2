from django.forms import modelform_factory

from TonysHardware_v2.hardware.models import RAMMemory, Cpu, StorageDrive, Psu, NvidiaGPU, AMDRadeonGPU, MotherBoardModel

MODELS = {
    'RAMMemory': RAMMemory,
    'Cpu': Cpu,
    'StorageDrive': StorageDrive,
    'Psu': Psu,
    'NvidiaGPU': NvidiaGPU,
    'AMDRadeonGPU': AMDRadeonGPU,
    'MotherBoard': MotherBoardModel,

}


def get_model_from_model_name(model_name):
    return MODELS.get(model_name, None)
