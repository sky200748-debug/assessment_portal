from django.contrib import admin
from .models import Category, Exam, Question, Result

admin.site.register(Category)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Result)