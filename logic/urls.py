from django.urls import path
from logic import views

app_name = "logic"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("input-tables", views.InputTables.as_view(), name="input-tables"),
    # COURSE RELATED ENDPOINTS
    path("delete-course", views.delete_course, name="course-delete"),
    path('edit-course/<str:pk>/', views.edit_course, name = "edit-course"),
    path('create-course/', views.create_course, name = "create-course"),

    # CLASSROOM RELATED ENDPOINTS
    path("delete-classroom", views.delete_classroom, name="delete-classroom"),
    path('edit-classroom/<str:pk>/', views.edit_classroom, name = "edit-classroom"),


    path('upload-file/', views.upload_file_view, name='upload-file'),
]
