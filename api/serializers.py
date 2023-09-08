from rest_framework import serializers
from offers.models import Offer, OfferDate, Category, Subcategory, Pictures, Feedbacks
from companies.models import Location, Company
from orders.models import Order
from registration.models import AdditionalUserInfo
from django.contrib.auth.models import User


class OfferDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDate
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
        fields = [
            "name",
            "location_description",
            "city",
            "review",
            "reviews_count",
        ]


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    Subcategories = SubcategorySerializer()

    class Meta:
        model = Category
        fields = ["id", "name", "Subcategories"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["name", "lng", "lat"]


class OffersSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    company = CompanySerializer()

    # category = CategorySerializer(many=True)

    class Meta:
        model = Offer
        fields = [
            "title",
            "highlights",
            "old_price",
            "new_price",
            "id",
            "location",
            "company",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "id"]


class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    offer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Feedbacks
        fields = ["id", "user_id", "feedback_content", "offer_id", "user"]


class SingleOfferSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    company = CompanySerializer()
    category = CategorySerializer(many=True)
    feedback = FeedbackSerializer(many=True, default="")

    class Meta:
        model = Offer
        fields = "__all__"


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = "__all__"
