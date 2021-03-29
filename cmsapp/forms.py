from django import forms
from .models import DepartmentModel
from .models import StudentModel
from .models import SportModel
from .models import InfoModel

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentModel
        fields= '__all__'
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields='__all__'

class SportForm(forms.ModelForm):
    class Meta:
        model = SportModel
        fields='__all__'

class InfoForm(forms.ModelForm):
    class Meta:
        model = InfoModel
        fields='__all__'