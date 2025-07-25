from django.urls import path

from .views.events import *
from .views.scoreboard import ScoreboardListView
from .views.suggestion import SuggestionListView, SuggestionCreateView, SuggestionUpdateView, SuggestionDeleteView, form_handler, form_handler2, SomeFormView


urlpatterns = [
    path('', index),
    path('path2/',IndexView.as_view()),
    path('OpenRegistrationView/',OpenRegistrationView.as_view(), name='open_registration'),
    path('event/<int:pk>/', EventDetailView.as_view(), name="event-detail"),
    path('ongoing-events/', OngoingEventsView.as_view(), name="ongoing-events"),
    path('upcoming-events/', UpcomingEventsView.as_view(), name="upcoming-events"),
    path('awaiting-for-results-events/', AwaitingForResultsEventsView.as_view(), name="awaiting-for-results-events"),
    path('results-published-events/', ResultsPublishedEventsView.as_view(), name="results-published-events"),

    path('scoreboard/', ScoreboardListView.as_view(), name="scoreboard"),

    path('suggestion-box/', SuggestionListView.as_view(), name="suggestion-box-list"),
    path('suggestion/create/', SuggestionCreateView.as_view(), name="suggestion-box-create"),
    path('suggestion/<int:pk>/', SuggestionUpdateView.as_view(), name="suggestion-box-update"),
    path('suggestion/<int:pk>/delete/', SuggestionDeleteView.as_view(), name="suggestion-box-delete"),

    path('form-handling/', form_handler, name="form-handling"),
    path('form-handling-blog/', form_handler2, name="form-handling-blog"),

    path('form-class/', SomeFormView.as_view(), name="form-class"),
]
