from django.urls import path
from logic import views

app_name = "logic"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("table/", views.Table.as_view(), name="table_content"),
    path("delete-course/", views.course_delete, name="delete_course"),
    path('update-course/<str:pk>/', views.update_course, name = "update-course"),
    path('create-course/', views.create_course, name = "create-course"),
]
