from django.db import models
from django.conf import settings
# Create your models here.

class Event(models.Model):
    # id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    registration_close_at = models.DateTimeField()
    start_at = models.DateTimeField()
    ends_at = models.DateTimeField()

    # created_at = models.DateTimeField(auto_now=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'ModelName'
    #     verbose_name_plural = 'ModelNames'



class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=10, null=True, blank=True, choices=[
        ('First', 'First Place'),
        ('Second', 'Second Place'),
        ('Third', 'Third Place')
    ])
    point = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.user.username.upper()} - registered for {self.event.title}'
    

class SuggestionBox(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=35, choices=[
        ('Suggestions', 'Suggestions'),
        ('Complaint', 'Complaint'),
    ], default="Suggestions", help_text="Please select the nature of your suggestion")
    description = models.TextField(help_text="Share your Experience With us! We Would like to hear from you!")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True,  help_text="if you are sharing something reguarding some event, please select that event "
                                        "here!")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.description