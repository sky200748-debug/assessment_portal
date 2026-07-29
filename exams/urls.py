from django.urls import path
from .views import exam_list, take_exam
from .views import exam_list, take_exam, report_list

urlpatterns = [
    path('', exam_list, name='exam_list'),
    path('take/<int:exam_id>/', take_exam, name='take_exam'),
    path('reports/', report_list, name='reports'),
]