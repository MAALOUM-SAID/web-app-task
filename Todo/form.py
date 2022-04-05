from django import forms

from Todo.models import Task

class TitleForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'task_title',
        ]
        widgets = {
            'task_title': forms.TextInput(attrs={
                'class': "form-control border-info",
                'name':"title",
                'aria-label':"Sizing example input",
                'aria-describedby':"inputGroup-sizing-default",
                'placeholder':'Title',
                
        })
        }
        labels={
            'task_title':''
        }
class ContentForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'task',
        ]
        widgets = {
            'task': forms.TextInput(attrs={
                'class': "form-control border-info",
                'name':"task",
                'aria-label':"Sizing example input",
                 'aria-describedby':"inputGroup-sizing-default",
                 'placeholder':'task content',
        })
        }
        labels={
            'task':''
        }
class BeginForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'begin',
        ]
        widgets = {
            'begin': forms.TimeInput(attrs={
                'class': "form-control border-info",
                'name':"begin",
                'type':'time',
                'aria-label':"Sizing example input",
                'aria-describedby':"inputGroup-sizing-default"
        })
        }
        labels={
            'begin':''
        }
class EndForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'end',
        ]
        widgets = {
            'end': forms.TimeInput(attrs={
                'class': "form-control border-info",
                'name':"end",
                'type':'time',
                'aria-label':"Sizing example input",
                 'aria-describedby':"inputGroup-sizing-default"
        })
        }
        labels={
            'end':''
        }





class CategoryForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'category',
        ]
        widgets = {
            'category': forms.Select(attrs={
                'class': "form-select mt-3",
                'name':'category'
        })
        }
        
class StatusForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'status',
        ]
        widgets = {
            'status': forms.Select(attrs={
                'class': "form-select mt-3",
                'name':'status'        })
        }



