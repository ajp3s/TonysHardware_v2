from django import forms
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

