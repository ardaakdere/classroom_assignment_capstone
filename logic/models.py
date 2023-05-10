from django.db import models

class Campus(models.Model):
    campus_name = models.CharField(max_length=256)

    def __str__(self):
        return self.campus_name


class Building(models.Model):
    building_name = models.CharField(max_length=256)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.building_name


class Classroom(models.Model):
    classroom_number = models.CharField(max_length=256)
    classroom_quota = models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.classroom_number)


class Course(models.Model):
    course_name = models.CharField(max_length=256)
    course_code = models.CharField(max_length=256)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="classrooms") # OneToMany
    students_quota = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.course_name + " - " + str(self.classroom.classroom_number)

