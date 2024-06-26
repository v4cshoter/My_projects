from django.shortcuts import render

from django.http import HttpResponse

from django.db import models


def index(request):
    return HttpResponse("Hello, world. You're at the to_do index.")


