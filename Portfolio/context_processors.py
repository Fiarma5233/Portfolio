from datetime import datetime

def current_year(request):
    return {'current_year': datetime.now().year}


# context_processors.py
from realisations.models import Realisation

def realisations(request):
    return {
        'realisations': Realisation.objects.all().order_by('-created_at')
    }