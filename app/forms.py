from django import forms
from app.models import donermodel
class addform(forms.ModelForm):
    class Meta:
        model=donermodel
        fields='__all__'