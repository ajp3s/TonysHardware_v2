from django import forms

from TonysHardware_v2.functionality.funcs import get_model_from_model_name


class HardwareModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        model = get_model_from_model_name(kwargs.get('request'))
        if model is not None:
            self.Meta.model = model
            self.Meta.fields = '__all__'

    class Meta:
        model = None
        fields = '__all__'
