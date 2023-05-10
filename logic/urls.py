from django.urls import path
from logic import views

app_name = "logic"

urlpatterns = [
    path("", views.Home.as_view()),
    path("table/", views.Table.as_view(), name="table_content"),
    path("delete-course/", views.course_delete, name="delete_course"),
]
