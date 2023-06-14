from django.forms import ModelForm
from logic import models

class CourseForm(ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__' #['course_name', 'course_code', 'course_section', 'registered_student']


class ClassroomForm(ModelForm):
    class Meta:
        model = models.Classroom
        fields = '__all__'
