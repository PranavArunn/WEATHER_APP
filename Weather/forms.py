from .models import city
from django.forms import ModelForm, TextInput
class cityform(ModelForm):
    class Meta:
        model = city
        fields = ["name"]
        widgets = {"name":TextInput(attrs={"class":"input","placeholder":"#Writecityname"})}
