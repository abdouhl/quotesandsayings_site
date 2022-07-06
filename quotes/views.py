from .models import Quote,Author
from django.views import generic

class IndexView(generic.ListView):
    template_name='quotes/index.html'
    context_object_name = 'authors'
    def get_queryset(self):
        return Author.objects.all()

class DetailView(generic.DetailView):
    model: Author
    template_name='quotes/detail.html'
    