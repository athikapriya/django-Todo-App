import django_filters
from .models import Task
from django_filters import CharFilter, ChoiceFilter
from django import forms

class TaskFilter(django_filters.FilterSet):

    priority = ChoiceFilter(choices=Task.PRIORITY_CHOICES, 
                            empty_label="Select Priority",
                            label='',
                            widget = forms.Select(
                                attrs = {
                                    "class" : "form-select",
                                    "onchange" : "this.form.submit();"
                                }
                            )
                        )

    description = CharFilter(field_name='description',
                             lookup_expr='icontains',
                             label="",
                             widget = forms.TextInput(
                                 attrs = {
                                     "placeholder" : 'search anything...',
                                     'class' : 'form-control'
                                 }
                             ) 
                        )

    class Meta:
        model = Task
        fields = ["priority", "description"]