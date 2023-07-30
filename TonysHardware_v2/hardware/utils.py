from TonysHardware_v2.hardware.models import NvidiaGPU, AMDRadeonGPU, Psu, Cpu, StorageDrive, RAMMemory, MotherBoard
from django.forms import modelform_factory

def get_model_from_query_params(request):
    model_name = request.GET.get('model')
    MODELS = {
        'NvidiaGPU': NvidiaGPU,
        'AMDRadeonGPU': AMDRadeonGPU,
        'RAMMemory': RAMMemory,
        'Cpu': Cpu,
        'StorageDrive': StorageDrive,
        'MotherBoard': MotherBoard,
        'Psu': Psu,

    }

    model = MODELS.get(model_name)
    if model is None:
        raise ValueError("Invalid model selected.")
    return model


def create_hardware_model_form(request, *args, **kwargs):
    model = get_model_from_query_params(request)
    if model is not None:
        form_class = modelform_factory(model, fields='__all__')
        return form_class(*args, **kwargs)
    raise ValueError("Invalid model specified.")
