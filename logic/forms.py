from django.forms import ModelForm
from logic import models

class CourseForm(ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'


class ClassroomForm(ModelForm):
    class Meta:
        model = models.Classroom
        fields = '__all__'
