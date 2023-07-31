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


def create_hardware_model_form(*args, **kwargs):
    model = kwargs.get('model', None)
    if model is not None:
        form_class = modelform_factory(model, fields='__all__')
        return form_class(*args, **kwargs)
    raise ValueError("Invalid model selected.")


def get_model_from_model_name(model_name):
    return MODELS.get(model_name, None)