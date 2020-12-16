from django.shortcuts import render
from django.http import HttpResponse

from .models import Questions,  Post


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def questions(request):
    questions_query = Questions.objects.all()
    context = {
        'questions': questions_query
    }
    return render(request, 'blog/questions.html', context)


