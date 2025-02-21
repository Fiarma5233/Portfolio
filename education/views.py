from django.shortcuts import render
from .models import Education

# Create your views here.
def education(request):
    educations = Education.objects.all()
    return render(request, 'education/education.html', {'educations': educations})