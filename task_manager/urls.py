from django.urls import path

from task_manager.views import (
    index,
    logout_user,
    RegisterNewWorkerView
)

urlpatterns = [
    path("", index, name="index"),
    path("account/register/", RegisterNewWorkerView.as_view(), name="register"),
    path("logout/", logout_user, name="logout"),
]
app_name = "task_manager"
