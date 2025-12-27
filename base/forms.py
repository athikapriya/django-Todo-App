from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", 'priority', 'deadline', 'description']   

        label ={
            "name" : "Task Title",
            "priority" : "Priority Level",
            "deadline" : 'Deadline',
            "description" : "Description"
        }

        widget = {
            "description" : forms.Textarea(attrs={
                "rows" : 3,
                'class' : "form-control",
                "placeholder" : 'Write task details...'
            }),

            'name' : forms.TextInput(attrs={
                "class" : "form-control",
                'placeholder' : 'Add a task title'
            }),

            "priority" : forms.Select(attrs={
                "class" : 'form-control'
            }),
            
            "deadline" : forms.DateTimeInput(attrs={
                'class' : "form-control",
                "type" : 'datetime-local',
                "step": 60
            },
            format="%Y-%m-%dT%H:%M"
            ),

        } 


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["deadline"].input_formats = ( "%Y-%m-%dT%H:%M", )