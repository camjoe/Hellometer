from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VendorClients
from .serializers import VendorClientsSerializer


@api_view(['GET'])
def vendor_dashboard(request):
    return Response({'message': 'Welcome to your dashboard!'})


@api_view(['GET'])
def vendor_clients(request):
    clients = VendorClients.objects.all()
    serializer = VendorClientsSerializer(clients)

    return Response(serializer.data)