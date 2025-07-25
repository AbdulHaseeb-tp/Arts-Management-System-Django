from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.views import View
from django.views.generic import RedirectView, TemplateView, ListView, DetailView
from django.utils.decorators import method_decorator

from event.models import Event, Registration
from django.utils.timezone import now
from django.contrib import messages


User = get_user_model()

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')



# class IndexView(View):

#     def get(self, request, *args, **kwargs):
#         return render(request, 'index.html')
    


# class IndexView(RedirectView):

#     url = '/ahsgdgbdhdjdjd/'

#     def get(self, request, *args, **kwargs):
#         .....
#         .....
#         return super(IndexView, self).get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'


    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
    
        cxt = super(IndexView, self).get_context_data(**kwargs)
        cxt['new'] = 'title'
        return cxt


@method_decorator(login_required, 'dispatch')
class OpenRegistrationView(ListView):
    model = Event
    context_object_name = 'events'
    template_name='event/event_list.html'


    def get_queryset(self):
        return Event.objects.all().filter(registration_close_at__gt=now()).order_by('registration_close_at')
    


@method_decorator(login_required, 'dispatch')
class OngoingEventsView(ListView):
    model = Event
    template_name = 'event/ongoing_event_list.html'

    def get_queryset(self):
        return Event.objects.all().filter(start_at__lt=now(), ends_at__gt=now()).order_by('start_at')    
    


@method_decorator(login_required, 'dispatch')
class UpcomingEventsView(ListView):
    model = Event
    template_name = 'event/upcoming_event_list.html'

    def get_queryset(self):
        return Event.objects.all().filter(registration_close_at__lte=now(), start_at__gt=now(),).order_by('registration_close_at')    
    


@method_decorator(login_required, 'dispatch')
class AwaitingForResultsEventsView(ListView):
    model = Event
    template_name = 'event/awaiting_for_results_event_list.html'

    def get_queryset(self):
        regn_with_price_declared = Registration.objects.filter(position__isnull=False).values_list('event_id', flat=True)
        return Event.objects.all().filter(ends_at__lt=now()).exclude(id__in=regn_with_price_declared).order_by('registration_close_at')
    


@method_decorator(login_required, 'dispatch')
class ResultsPublishedEventsView(ListView):
    model = Event
    template_name = 'event/results_published_event_list.html'

    def get_queryset(self):
        regn_with_price_declared = Registration.objects.filter(position__isnull=False).values_list('event_id', flat=True)
        return Event.objects.all().filter(ends_at__lt=now()).filter(id__in=regn_with_price_declared).order_by('registration_close_at')


@method_decorator(login_required, 'dispatch')
class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'

    def get_context_data(self, **kwargs):
        cxt = super(EventDetailView, self).get_context_data(**kwargs)
        cxt['is_registered'] = Registration.objects.filter(event=self.object, user=self.request.user).exists()
        return cxt

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        reg, created = Registration.objects.get_or_create(event=self.object, user=request.user)
        if created:
            messages.success(request,  f"You have successfully registered to {self.object.title}")
        else:
            messages.info(request, f"You already have registered to {self.object.title}")

        return self.get(request, *args, **kwargs)
    


    