from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def vendor_dashboard(request):
    return Response({'message': 'Welcome to your dashboard!'})