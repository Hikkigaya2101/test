from .models import Position,Worker
from django.forms import ModelForm,TextInput,DateInput

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['fio_worker','born_date','work_date','position']


        widgets = {
            'fio_worker': TextInput(attrs={'class':'text'}),
            'born_date': DateInput(attrs={'class': 'text'}),
            'work_date': DateInput(attrs={'class': 'text'}),
            'position': TextInput(attrs={'class': 'text'}),
        }

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['position_name']


        widgets = {
            'position_name': TextInput(attrs={'class':'text'})
        }