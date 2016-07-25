from django.shortcuts import render
from django.views import generic
from .models import Shape


class IndexView(generic.ListView):
    template_name = 'Shape/objects.html'
    context_object_name = 'shape_objects'

    def get_queryset(self):
        return Shape.objects.all()


class DetailView(generic.DetailView):
    model = Shape
    template_name = 'Shape/display_object.html'
    context_object_name = 'shape'
