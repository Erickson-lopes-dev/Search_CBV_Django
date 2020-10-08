from django.views.generic import ListView

from CBV_search.models import Person


class HomePage(ListView):
    model = Person
    template_name = 'home.html'

