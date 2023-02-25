from rest_framework import serializers
from offers.models import (Offer, OfferDate,
                           Category, Subcategory,
                            Pictures)
from companies.models import Location, Company
from orders.models import Order
from registration.models import AdditionalUserInfo


class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"


class OfferDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDate
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalUserInfo
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = "__all__"
