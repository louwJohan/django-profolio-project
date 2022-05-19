from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})


def detail(request, job_id):
    print(job_id)
    return render(request, 'jobs/home.html')