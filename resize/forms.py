

from .models import *
from django import forms


class ResizeForm(forms.ModelForm):
    class Meta:
        model = Resize
        fields = "__all__"

        widgets = {
            'Image': forms.FileInput(attrs={'class': 'wrap-input2 validate-input'}),
            'Width': forms.NumberInput(attrs={'class': 'wrap-input2 validate-input'}),
            'Height': forms.NumberInput(attrs={'class': 'wrap-input2 validate-input'}),
        }
