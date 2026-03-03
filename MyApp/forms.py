
from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea",  max_length=200, widget=forms.TextInput(attrs={ 'class': 'form-control mb-3'}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={ 'class': 'form-control mb-3'}))