from django import forms
from mailapp.models import Student
class studentforms(forms.ModelForm):
    class Meta:
        model = Student
        fields ='__all__'