from django.db import models


class Classroom(models.Model):
    classroom_code = models.CharField(max_length=256)
    classroom_quota = models.IntegerField()
    classroom_type = models.IntegerField()

    def __str__(self):
        return str(self.classroom_number)


class Course(models.Model):
    course_name = models.CharField(max_length=256)
    course_code = models.CharField(max_length=256)
    course_section = models.CharField(max_length=1)
    registered_student = models.IntegerField()
    course_type = models.IntegerField()

    def __str__(self):
        return self.course_name


class Result(models.Model):
    course_code = models.CharField(max_length=255)
    course_section = models.CharField(max_length=1)
    course_name = models.CharField(max_length=255)
    classroom = models.CharField(max_length=255)
