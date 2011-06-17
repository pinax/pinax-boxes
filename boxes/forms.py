from django import forms

from boxes.models import Box


class BoxEditForm(forms.ModelForm):
    
    class Meta:
        model = Box
        fields = ["content"]
