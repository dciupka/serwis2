from rest_framework.response import Response
from rest_framework.decorators import api_view
from serwis2.models import Geoinfo
from .serializers import GeoinfoSerializer

@api_view(['GET'])
def getData(request):
    items = Geoinfo.objects.all()
    serializer = GeoinfoSerializer(items, many=True)
    return Response(serializer.data)

