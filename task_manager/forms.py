from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Worker


class RegisterWorkerForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ("username", "email", "password1", "password2",)
