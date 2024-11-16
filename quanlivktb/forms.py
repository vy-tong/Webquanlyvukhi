from django import forms
from .models import VuKhi, TrangBi

class VuKhiForm(forms.ModelForm):
    class Meta:
        model = VuKhi
        fields = '__all__'
        widgets = {
            'tinh_trang': forms.Select(choices=[
                ('tot', 'Tốt'),
                ('hong', 'Hỏng'),
                ('dang_sua', 'Đang sửa')
            ])
        }

class TrangBiForm(forms.ModelForm):
    class Meta:
        model = TrangBi
        fields = '__all__' 