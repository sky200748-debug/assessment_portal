from django.contrib import admin
from django.urls import path, include
from .views import home, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('exams/', include('exams.urls')),
]