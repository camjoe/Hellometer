from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VendorClients
from .serializers import VendorClientsSerializer


@api_view(['GET'])
def vendor_dashboard(request):
    return Response({'message': 'Welcome to your dashboard!'})


@api_view(['GET'])
def vendor_clients(request):
    clients = VendorClients.objects.all()[:4] # NOTE: testing with first four data points
    serializer = VendorClientsSerializer(clients, many=True)

    return Response(serializer.data)