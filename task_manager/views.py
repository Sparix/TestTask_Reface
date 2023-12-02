from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import RegisterWorkerForm
from task_manager.models import Worker


def index(request):
    return render(request, "task_manager/index.html")


@login_required
def logout_user(request):
    logout(request)
    return redirect("login")


class RegisterNewWorkerView(generic.CreateView):
    model = Worker
    form_class = RegisterWorkerForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("task_manager:index")
