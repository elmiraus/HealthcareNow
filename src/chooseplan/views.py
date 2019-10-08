from django.shortcuts import render
from django.http import HttpResponse


def chooseplan(request):
    return render(request, 'chooseplan/chooseplan.html')
