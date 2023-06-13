from django.urls import path
from logic import views

app_name = "logic"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("input-tables", views.InputTables.as_view(), name="input-tables"),
    path("result-table", views.ResultTable.as_view(), name="result-table"),

    # COURSE RELATED ENDPOINTS
    path("delete-course", views.delete_course, name="course-delete"),
    path('edit-course/<str:pk>/', views.edit_course, name = "edit-course"),
    path('create-course/', views.create_course, name = "create-course"),

    # CLASSROOM RELATED ENDPOINTS
    path("delete-classroom", views.delete_classroom, name="delete-classroom"),
    path('edit-classroom/<str:pk>/', views.edit_classroom, name = "edit-classroom"),
    path('create-classroom/', views.create_classroom, name = "create-classroom"),

    path('run-optimization/', views.run_optimization, name="run-optimization"),


    path('chart-data/', views.chart_data, name="chart-data"),


    path('upload-file/', views.upload_file_view, name='upload-file'),
]
