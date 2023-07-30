from django import forms

from TonysHardware_v2.hardware.models import RAMMemory, Cpu, StorageDrive, Psu, NvidiaGPU


class HardwareModelForm(forms.ModelForm):
    model = None  # We'll set this dynamically based on the argument received

    def get_model(self, model_name):
        models = {
            'RAMMemory': RAMMemory,
            'Cpu': Cpu,
            'StorageDrive': StorageDrive,
            'Psu': Psu,
            'NvidiaGPU': NvidiaGPU,
        }
        return models.get(model_name, None)

    def __init__(self, *args, **kwargs):
        model_name = kwargs.pop('model', None)
        self.model = self.get_model(model_name)
        super().__init__(*args, **kwargs)
        if self.model:
            # Set the form fields dynamically based on the model
            self.fields = forms.ALL_FIELDS  # Or you can customize this based on your requirements

    class Meta:
        model = None  # We'll set this dynamically based on the argument received
        fields = '__all__'