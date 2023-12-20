from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "ticket_number",
            "title",
            "description",
            "train_class",
            "departure_station",
            "arrival_station",
            "departure_time",
            "arrival_time",
            "passenger_name",
            "passenger_age",
        ]

    def get_departure_time(self, obj):
        return obj.departure_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_arrival_time(self, obj):
        return obj.arrival_time.strftime("%Y-%m-%d %H:%M:%S")
