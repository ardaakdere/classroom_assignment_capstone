from django.forms import ModelForm
from logic import models

class CourseForm(ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'
