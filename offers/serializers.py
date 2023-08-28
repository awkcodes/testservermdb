from rest_framework import serializers
from offers.models import Offer


class OfferSerializer(serializers.Serializer):
    model = Offer
    fields = ["id"]
