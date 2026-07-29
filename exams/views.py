from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Exam, Question, Result

def exam_list(request):

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    exams = Exam.objects.all().order_by('id')

    if query:
        exams = exams.filter(title__icontains=query)

    if category_id:
        exams = exams.filter(category_id=category_id)

    categories = Category.objects.all()

    paginator = Paginator(exams, 5)

    page_number = request.GET.get('page')

    exams = paginator.get_page(page_number)

    return render(request, 'exam_list.html', {
        'exams': exams,
        'categories': categories
    })


def take_exam(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)

    questions = Question.objects.filter(exam=exam)

    if request.method == 'POST':

        score = 0

        for question in questions:

            selected_answer = request.POST.get(f'q{question.id}')

            if selected_answer == question.answer:
                score += 1

        Result.objects.create(
            student=request.user,
            exam=exam,
            score=score
        )

        return render(request, 'result.html', {
            'score': score,
            'total': questions.count()
        })

    return render(request, 'take_exam.html', {
        'exam': exam,
        'questions': questions
    })
def report_list(request):
    results = Result.objects.all().order_by('-created_at')

    return render(request, 'report_list.html', {
        'results': results
    })