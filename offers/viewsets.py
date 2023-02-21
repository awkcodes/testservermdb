from rest_framework import viewsets
from offers.models import Offer
from offers.serializers import OffersSerializer


class OffersViewSet(viewsets.ModelViewSet):
    serializer_class = OffersSerializer

    def get_queryset(self):
        return Offer.objects.all()
