from django.views import generic
from .models import List
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect ,render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import Userform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from urllib.parse import urlparse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import AuthenticationForm


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'all_lists'

    def get_queryset(self):
        return List.objects.all()

class DetailView(generic.DetailView):
    model = List
    template_name = 'todo/detail.html'

class ListCreate(CreateView):
    model = List
    fields =['list_name',  'due_date']

class ListUpdate(UpdateView):
    model = List
    fields =['list_name',  'due_date']

class ListDelete(DeleteView):
    model = List
    success_url = reverse_lazy('todo:index')

class UserFormView(View):
    form_class = Userform
    template_name = 'todo/registration_form.html'
    
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned(normalised) data
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('todo:index')

        return render(request, self.template_name, {'form':form})
    
class CustomLoginView(LoginView):

    form_class = LoginForm
    template_name = 'login.html'
    



