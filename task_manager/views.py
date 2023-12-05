from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import RegisterWorkerForm, CreateNewTaskForm
from task_manager.models import Worker, Task


@login_required
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


class TableUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "tables"

    def get_queryset(self):
        queryset = (
            Task.objects.prefetch_related(
                "assignees").select_related(
                "task_type").filter(
                assignees=self.request.user
            )
        )
        return queryset


class TableUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class CreateNewTaskView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = CreateNewTaskForm
    success_url = reverse_lazy("task_manager:table-user")
