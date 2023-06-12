from django.shortcuts import render, redirect
from django.views.generic import View
from logic import models
from django.http import HttpResponse, JsonResponse
from logic import forms
import os
from django.conf import settings
from logic.utils import read_excel, gurobi_optimization

# Create your views here.
class Home(View):

    def get(self, request):

        return render(request, 'logic/index.html')
    

class InputTables(View):

    def get(self, request):

        classrooms = models.Classroom.objects.all()
        courses = models.Course.objects.all()

        return render(request, 'logic/input_tables.html', context = {'courses': courses, 'classrooms': classrooms})


class ResultTable(View):
    
    def get(self, request):

        results = models.Result.objects.all()

        return render(request, 'logic/output_table.html', context = {'results': results})



# COURSE RELATED FUNCTIONS START #
def edit_course(request, pk):
    course = models.Course.objects.get(id=pk)
    form = forms.CourseForm(instance=course)
    
    if request.method == 'POST':
        form = forms.CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('logic:home')
        
    context = {'form' : form}
    return render(request, 'logic/edit_form.html', context)


def delete_course(request):

    course_pk = request.GET['course_pk']

    models.Course.objects.get(pk=course_pk).delete()

    return HttpResponse('200')

def create_course(request):
    form = forms.CourseForm()
    if request.method == 'POST':
        form = forms.CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logic:home')
            
    context = {'form' : form}
    return render(request, 'logic/edit_form.html', context)

# COURSE RELATED FUNCTIONS END #

# CLASSROOM RELATED FUNCTIONS START #

def edit_classroom(request, pk):
    classroom = models.Classroom.objects.get(id=pk)
    form = forms.ClassroomForm(instance=classroom)
    
    if request.method == 'POST':
        form = forms.ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect('logic:home')
        
    context = {'form' : form}
    return render(request, 'logic/edit_form.html', context)


def delete_classroom(request):

    classroom_pk = request.GET['classroom_pk']

    models.Classroom.objects.get(pk=classroom_pk).delete()

    return HttpResponse('200')

def create_classroom(request):
    form = forms.ClassroomForm()
    if request.method == 'POST':
        form = forms.ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logic:home')
            
    context = {'form' : form}
    return render(request, 'logic/edit_form.html', context)

# CLASSROOM RELATED FUNCTIONS END #

def upload_file_view(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        
        # Save the file to the "uploads" directory
        file_path = os.path.join(settings.BASE_DIR, 'logic/uploads', file.name)
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        # Perform any additional processing with the saved file
        read_excel.save_excel_to_database(file_path)
        # Example response
        response_data = {'success': True}
        return JsonResponse(response_data, status=200)
    
    # If the request method is not POST or no file is provided
    response_data = {'message': 'Invalid request'}
    return JsonResponse(response_data, status=400)


def run_optimization(request):
    gurobi_optimization.run_optimization()

    return JsonResponse({'success': True}, status=200)