from django.http import HttpResponse
from django.views import generic

class PostView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")