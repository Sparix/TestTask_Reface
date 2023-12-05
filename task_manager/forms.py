from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from task_manager.models import Worker, Task


class RegisterWorkerForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ("username", "email", "password1", "password2",)


class CreateNewTaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            "id": "cb1",
            "class": "assignees-checkbox",
        }),
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "min": datetime.now(),
                    "class": "deadline-input"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "text-area-description",
                }
            ),
            "priority": forms.Select(
                attrs={
                    "class": "choice-select"
                }
            ),
            "task_type": forms.Select(
                attrs={
                    "class": "choice-select"
                }
            ),
        }


class SearchForm(forms.Form):
    search_field = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "search-input",
            "placeholder": "Search field, type name table"
        })
    )
