from django import forms
from event.models import SuggestionBox, Registration, Event

from django.core.exceptions import ValidationError


class SuggestionBoxForm(forms.ModelForm):

    def clean_description(self):
        description = self.cleaned_data["description"].strip()
        
        if len(description) < 20:
            raise ValidationError("Atleast 20 characters are required for description", code='invalid')
        return description
    


    def clean(self):
        super(SuggestionBoxForm, self).clean()

        category = self.cleaned_data['category']
        description = self.cleaned_data['description']
        event = self.cleaned_data['event']
        user = self.cleaned_data['user']

        position = self.cleaned_data['position']

        if category == 'Complaint':     #user not register the event case not permit to complai
            if not Registration.objects.filter(event=event, user=user).exists():
                raise ValidationError(f'You can only raise  a complaint against {event}, only if you are registered to that event!', code='invalid')
            # elif Registration.objects.filter(event=event, position=position['first']).exists():
            #     raise ValidationError(f'You can only raise  a complaint against {event}, only if you are registered to that event!', code='invalid')
        return self.cleaned_data
    

    class Meta:
        model = SuggestionBox
        fields = ['category', 'description', 'event']





class BlogForm(forms.Form):
    title = forms.CharField(max_length=256, required=True)
    description = forms.CharField(widget=forms.Textarea)
    event = forms.ModelChoiceField(queryset=Event.objects.all())
    date = forms.DateField()
    time = forms.TimeField()
    datetime = forms.DateTimeField()
    file = forms.FileField()
    quantity = forms.IntegerField()
    choice = forms.ChoiceField(choices=[
        ('A','a'),
        ('B','b'),
        ('C','c')       #forms.MultipleChoiceField()
    ])


