from django.db import models


class Ticket(models.Model):
    ticket_number = models.CharField(max_length=255, unique=True)  #(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    train_class = models.CharField(max_length=5 ,null=True, blank=True)
    departure_station = models.CharField(max_length=100 ,null=True, blank=True)
    arrival_station = models.CharField(max_length=100, null=True, blank=True)
    departure_time = models.DateTimeField(null=True, blank=True)
    arrival_time = models.DateTimeField(null=True, blank=True)
    passenger_name = models.CharField(max_length=255,null=True, blank=True)
    passenger_age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return self.title
