from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,  TemplateView, DeleteView
from .models import *
from django.urls import reverse_lazy
# Create your views here.

class HomePage(TemplateView):
    template_name = "home.html"

class ShowVakansi(ListView):
    template_name = "showallvakansi.html"
    model = Vakaansi
    context_object_name = "vakansi"

class DetailVakansi(DetailView):
    template_name = "detailvakansi.html"
    model = Vakaansi
    context_object_name = "vakan"

class CreateVakansi(CreateView):
    template_name = "createvakansi.html"
    model = Vakaansi
    fields = ("title","discraption","time_work","time_notwork", "salary","image","cotegory")
    success_url = reverse_lazy("showvakansi")


class UpdateVakansi(UpdateView):
    template_name = "updatevakansi.html"
    model = Vakaansi
    fields = ("title","discraption","time_work","time_notwork", "salary","image","cotegory")
    success_url = reverse_lazy("showvakansi")


class DeleteVakansi(DeleteView):
    model = Vakaansi
    template_name = "deletevakansi.html"
    success_url = reverse_lazy("showvakansi")





class ShowCotegory(ListView):
    template_name = "showallcotegory.html"
    model = Cotegory
    context_object_name = "cotegorys"

class DetailCotegory(DetailView):
    template_name = "detailCotegory.html"
    model = Cotegory 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vakansi"] = Vakaansi.objects.filter(cotegory=self.kwargs['pk'])
        return context
    
    context_object_name = "cotegory"

class CreateCotegory(CreateView):
    template_name = "createcotegory.html"
    model = Cotegory
    fields = ("cotegory_name",)
    success_url = reverse_lazy("showcotegory")


class UpdateCotegory(UpdateView):
    template_name = "updatecotegory.html"
    model = Cotegory
    fields = ("cotegory_name",)
    success_url = reverse_lazy("showcotegory")


class DeleteCotegory(DeleteView):
    template_name = "deletecotegory.html"
    model = Cotegory
    success_url = reverse_lazy("showcotegory")





class ShowApplication(ListView):
    template_name = "showallapplication.html"
    model = Application
    context_object_name = "applications"

class DetailApplication(DetailView):
    template_name = "detailapplication.html"
    model = Application 
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["vakansi"] = Vakaansi.objects.filter(id=self.kwargs['pk'])
    #     return context
    
    context_object_name = "application"

class CreateApplication(CreateView):
    template_name = "createapplication.html"
    model = Application
    fields = ("f_name","l_name","emal","vakansi","discraptions","resume",)
    success_url = reverse_lazy("showapplication")


class UpdateApplication(UpdateView):
    template_name = "updateapplication.html"
    model = Application
    fields = ("f_name","l_name","emal","vakansi","discraptions","resume",)
    success_url = reverse_lazy("showapplication")


class DeleteApplication(DeleteView):
    template_name = "deleteapplication.html"
    model = Application
    success_url = reverse_lazy("showapplication")



