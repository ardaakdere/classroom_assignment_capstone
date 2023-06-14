import pandas as pd
from logic.models import Classroom, Course

def save_excel_to_database(file_path):
    Classroom.objects.all().delete()
    Course.objects.all().delete()

    df1 = pd.read_excel(file_path, sheet_name="10062023", usecols="A:D", nrows=30)
    df2 = pd.read_excel(file_path, sheet_name="10062023", usecols="H:J", nrows=66)
    df1.columns = ['course_code', 'course_name', 'student_registered', 'course_type']
    df2.columns = ['classroom_code', 'classroom_capacity', 'classroom_type']

    # Iterate over df1 rows and create Classroom instances
    # Iterate over df1 rows and create Classroom instances
    for index, row in df2.iterrows():
        classroom = Classroom(
            classroom_code=row['classroom_code'],
            classroom_quota=row['classroom_capacity'],
            classroom_type=row['classroom_type']
        )
        classroom.save()

    # Iterate over df2 rows and create Course instances
    for index, row in df1.iterrows():

        # Extract the first word
        course_code, course_section = row['course_code'].split()

        course_section = course_section.replace('(', '')
        course_section = course_section.replace(')', '')

        course = Course(
            course_name=row['course_name'],
            course_code=course_code,
            course_section=course_section,
            registered_student=row['student_registered'],  # You might need to adjust this value
            course_type=row['course_type']
        )
        course.save()
