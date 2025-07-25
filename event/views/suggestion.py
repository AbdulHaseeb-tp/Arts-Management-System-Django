from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from django.views import View
from django.views.generic import RedirectView, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator

from event.models import Event, Registration, SuggestionBox
from django.utils.timezone import now
from django.contrib import messages
from django.urls import reverse
from event.forms import SuggestionBoxForm, BlogForm


@method_decorator(login_required, 'dispatch')
class SuggestionListView(ListView):
    model = SuggestionBox
    template_name = "event/suggestion-box-list.html"

    def get_queryset(self):
        return SuggestionBox.objects.filter(user=self.request.user).select_related('event')
    

@method_decorator(login_required, 'dispatch')
class SuggestionCreateView(CreateView):
    model = SuggestionBox
    fields = ['category', 'description', 'event']
    # success_url = reverse('suggestion-box-list') #Redirect

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SuggestionCreateView, self).form_valid(form)
    

    def get_success_url(self):
        if self.object.category == 'Suggestion':
            msg = "Thank you for your valuable Feedback!"
            messages.success(self.request, msg)
        else:
            msg = "We have recieved Your Complaint! We will look into it and will get back to you soon!"
            messages.info(self.request, msg)   
        return reverse('suggestion-box-list') #Redirect
    



@method_decorator(login_required, 'dispatch')
class SuggestionUpdateView(UpdateView):
    model = SuggestionBox
    fields = ['description', 'event']


    def get_success_url(self):
        msg = f"Your {self.object.category}! has been updated!"
        messages.success(self.request, msg)
        return reverse('suggestion-box-list') #Redirect
    



@method_decorator(login_required, 'dispatch')
class SuggestionDeleteView(DeleteView):
    model = SuggestionBox


    def get_success_url(self):
        msg = f"Your { self.object.category }! has been Deleted!"
        messages.error(self.request, msg)
        return reverse('suggestion-box-list') #Redirect
    



# form FBV

def form_handler(request):
    if request.method == 'POST':
        form = SuggestionBoxForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully created Suggestion Box Entry")
            return redirect('/')
    else:
        form = SuggestionBoxForm()

    context = {
        'form':form
    }

    return render(request , 'index.html', context)



def form_handler2(request):
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully created Suggestion Box Entry")
            return redirect('/')
    else:
        form = BlogForm()

    context = {
        'form':form
    }

    return render(request , 'index.html', context)



# CBV

class SomeFormView(FormView):
    form_class = BlogForm
    template_name = 'index.html'
    # success_url = reverse('form-class') #Redirect

    def form_valid(self, form):
        print(form.cleaned_data)
        messages.success(self.request, "Successfully created a Blog entry form blog class!")
        return super(SomeFormView, self).form_valid(form)
    

    def get_success_url(self):
        return reverse('form-class') #Redirect


# eg
class SomeCreateFormView(CreateView):
    form_class = SuggestionBoxForm
    
