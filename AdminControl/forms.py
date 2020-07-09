from django import forms
from .models import AdminUser


class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ('name',)
