from django.urls import path

from task_manager.views import (
    index,
    logout_user,
    RegisterNewWorkerView, TableUserListView
)

urlpatterns = [
    path("", index, name="index"),
    path("account/register/", RegisterNewWorkerView.as_view(), name="register"),
    path("logout/", logout_user, name="logout"),
    path("work/tasks/", TableUserListView.as_view(), name="table-user"),

]
app_name = "task_manager"
