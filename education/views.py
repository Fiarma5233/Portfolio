from django.shortcuts import render
from .models import Education

# Create your views here.
def education(request):
    educations = Education.objects.all().order_by('-end_year')  # Trier par année décroissante
    return render(request, 'education/education.html', {'educations': educations})