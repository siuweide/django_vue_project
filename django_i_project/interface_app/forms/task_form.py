from django import forms

class TaskForm(forms.Form):
    name = forms.CharField(label='姓名',
                           max_length=200,
                           min_length=1,
                           required=True)
    description = forms.CharField(label='姓名',
                           max_length=200,
                           min_length=1,
                           required=True)