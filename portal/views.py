from django.shortcuts import render
from exams.models import Category, Exam, Question
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    context = {
        'total_categories': Category.objects.count(),
        'total_exams': Exam.objects.count(),
        'total_questions': Question.objects.count(),
    }

    return render(request, 'dashboard.html', context)