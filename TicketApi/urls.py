from django.urls import path
from .views import ticket_info, TicketListAPIView, TicketListCreateAPIView

urlpatterns = [
    path("get-ticket-data", ticket_info, name="ticket_info"),
path('tickets/', TicketListAPIView.as_view(), name='ticket-list'),
path('tickets-post/', TicketListCreateAPIView.as_view(), name='ticket-list-create'),

               ]
