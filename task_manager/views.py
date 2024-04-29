from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from task_manager.forms import (
    RegisterWorkerForm,
    CreateNewTaskForm,
    SearchForm,
    UserUpdateForm,
    TaskTypeCreate
)
from task_manager.models import Worker, Task


def index(request):
    if request.user.is_authenticated:
        context = {
            "solved_tasks": Task.objects.filter(is_completed=True, assignees=request.user).count(),
            "unsolved_tasks": Task.objects.filter(is_completed=False, assignees=request.user).count()
        }
        return render(request, "task_manager/index.html", context=context)
    return render(request, "task_manager/index.html")


@login_required
def logout_user(request):
    logout(request)
    return redirect("login")


class RegisterNewWorkerView(generic.CreateView):
    model = Worker
    form_class = RegisterWorkerForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class TableUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "tables"
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search_field", "")
        context["form_search"] = SearchForm(
            initial={
                "search_field": search
            }
        )
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        queryset = (
            Task.objects.prefetch_related(
                "assignees").select_related(
                "task_type").filter(
                assignees=self.request.user
            )
        )
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["search_field"])

        return queryset


class TableUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class CreateNewTaskView(generic.TemplateView):
    template_name = "task_manager/task_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_type_form"] = TaskTypeCreate()
        context["form"] = CreateNewTaskForm()
        return context

    def post(self, request):
        form_task_type = TaskTypeCreate()
        form_task = CreateNewTaskForm()
        if request.method == "POST":
            if "type_task_form" in request.POST:
                form_task_type = TaskTypeCreate(request.POST)
                if form_task_type.is_valid():
                    form_task_type.save()
            elif "form_task" in request.POST:
                form_task = CreateNewTaskForm(request.POST)
                if form_task.is_valid():
                    form_task.save()
                    return redirect("task_manager:table-user")

        return render(request, "task_manager/task_form.html",
                      context={'form': form_task, 'task_type_form': form_task_type})


def change_status_tasks(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("task_manager:detail-task", pk=pk)


class UpdateTaskView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = CreateNewTaskForm
    success_url = reverse_lazy("task_manager:table-user")


class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    template_name = "task_manager/user_profile.html"
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse_lazy("task_manager:user-profile", kwargs={"pk": self.request.user.pk})
