from rest_framework import viewsets
from .models import Site, SiteType
from sigi_op.serializers import SiteTypeSerializer, SiteSerializer

# Create your views here.


class SiteListViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class SiteTypeListViewSet(viewsets.ModelViewSet):
    queryset = SiteType.objects.all()
    serializer_class = SiteTypeSerializer
