from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from task_manager.models import TaskType, Worker, Task


class RegisterWorkerForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ("username", "position", "email", "password1", "password2",)
        widgets = {
            "position": forms.Select(
                attrs={
                    "class": "choice-select"
                })
        }


class TaskTypeCreate(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ("name", "color")

        widgets = {
            "color": forms.TextInput(
                attrs={
                    "type": "color"
                }
            )
        }


class CreateNewTaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            "id": "cb1",
            "class": "assignees-checkbox",
        }),
        required=False
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


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "position",)
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter username"
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter first name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter last name"
            }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email"
            }),
            "position": forms.Select(attrs={
                "class": "form-control",
            }),

        }
