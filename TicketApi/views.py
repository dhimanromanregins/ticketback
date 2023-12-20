from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ticket
from rest_framework import generics
from .serializer import TicketSerializer
from rest_framework import status


@api_view(["POST"])
def ticket_info(request):
    ticket_number = request.data.get("ticket_number")
    if ticket_number:
        try:
            ticket = Ticket.objects.get(ticket_number=ticket_number)
            ticket_serializer = TicketSerializer(ticket)
            return Response(ticket_serializer.data, status=status.HTTP_200_OK)
        except Ticket.DoesNotExist:
            return Response(
                {"error": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND
            )
    else:
        return Response(
            {"error": "Please Provide Ticket id"}, status=status.HTTP_400_BAD_REQUEST
        )

class TicketListAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)