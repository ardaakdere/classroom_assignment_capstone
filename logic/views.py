from django.shortcuts import render, redirect
from django.views.generic import View
from logic import models
from django.http import HttpResponse
from logic import forms

# Create your views here.
class Home(View):

    def get(self, request):

        return render(request, 'logic/index.html')


class Table(View):

    def get(self, request):

        search = request.GET.get('s')

        courses = models.Course.objects.all()

        if search:
            courses = courses.filter(course_name__icontains=search)

        return render(request, 'logic/table.html', context = {'courses': courses})



def course_delete(request):

    course_pk = request.GET['course_pk']

    models.Course.objects.get(pk=course_pk).delete()

    return HttpResponse('200')


def update_course(request, pk):
    course = models.Course.objects.get(id=pk)
    form = forms.CourseForm(instance=course)
    
    if request.method == 'POST':
        form = forms.CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('logic:home')
        
    context = {'form' : form}
    return render(request, 'logic/course_form.html', context)


def create_course(request):
    form = forms.CourseForm()
    if request.method == 'POST':
        form = forms.CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logic:home')
            
    context = {'form' : form}
    return render(request, 'logic/course_form.html', context)