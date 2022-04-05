from django import forms

from Todo.models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'task_title',
            'task',
            'category',
            'status',
            'begin',
            'end',

        ]
        widgets={
            'task_title': forms.TextInput(attrs={
                'class': "form-control border-info m-2",
                'name':"title",
                'aria-label':"Sizing example input",
                'aria-describedby':"inputGroup-sizing-default",
                'placeholder':'Title',
                
        }),
            'task': forms.TextInput(attrs={
                'class': "form-control border-info m-2",
                'name':"task",
                'aria-label':"Sizing example input",
                'aria-describedby':"inputGroup-sizing-default",
                'placeholder':'Title',
                
        }),
         'end': forms.TimeInput(attrs={
                'class': "form-control border-info m-2",
                'name':"end",
                'type':'time',
                'aria-label':"Sizing example input",
                 'aria-describedby':"inputGroup-sizing-default"
        }),
         'begin': forms.TimeInput(attrs={
                'class': "form-control border-info m-2",
                'name':"begin",
                'type':'time',
                'aria-label':"Sizing example input",
                 'aria-describedby':"inputGroup-sizing-default",
        }),
        'status': forms.Select(attrs={
                'class': "form-select mt-3 m-2",
                'name':'status'        }),
        'category': forms.Select(attrs={
                'class': "form-select mt-3 m-2",
                'name':'category'
        })}
    labels={
        'begin':'',
        'end':'',
        'task_title':'',
        'task':'',}
