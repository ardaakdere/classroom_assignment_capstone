from django.shortcuts import render
from django.views.generic import View
from logic import models
from django.http import HttpResponse

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
