from django import forms
from .models import Setting

class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ('site_name', 'logo', 'admin_login_bg', 'copyright')
