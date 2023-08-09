from django import forms
from TonysHardware_v2.hardware.models import RAMMemoryModel, CpuModel, StorageDriveModel, PsuModel, NvidiaGPUModel, AMDRadeonGPUModel, MotherBoardModel


MODELS = {
    'RAMMemory': RAMMemoryModel,
    'Cpu': CpuModel,
    'StorageDrive': StorageDriveModel,
    'Psu': PsuModel,
    'NvidiaGPU': NvidiaGPUModel,
    'AMDRadeonGPU': AMDRadeonGPUModel,
    'MotherBoard': MotherBoardModel,

}


def get_model_from_model_name(model_name):
    return MODELS.get(model_name, None)


def create_modelform(model_input):
    class AbstractModelForm(forms.ModelForm):
        class Meta:
            model = model_input
            fields = '__all__'

    return AbstractModelForm


def create_disabled_modelform(model_input):
    class DisabledAbstractModelForm(forms.ModelForm):
        class Meta:
            model = model_input
            fields = '__all__'
    for field in DisabledAbstractModelForm.fields.values():
        field.widget.attrs['disabled'] = True
    return DisabledAbstractModelForm

