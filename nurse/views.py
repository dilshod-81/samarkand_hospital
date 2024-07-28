from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import People
from .forms import PeopleForm  # Assuming you have a form for the People model

class PeopleListView(ListView):
    model = People
    template_name = 'people_list.html'
    context_object_name = 'people'

class PeopleDetailView(DetailView):
    model = People
    template_name = 'people_detail.html'
    context_object_name = 'person'

class PeopleCreateView(CreateView):
    model = People
    form_class = PeopleForm
    template_name = 'people_form.html'
    success_url = reverse_lazy('people_list')

class PeopleUpdateView(UpdateView):
    model = People
    form_class = PeopleForm
    template_name = 'people_form.html'
    success_url = reverse_lazy('people_list')

class PeopleDeleteView(DeleteView):
    model = People
    template_name = 'people_confirm_delete.html'
    success_url = reverse_lazy('people_list')
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)