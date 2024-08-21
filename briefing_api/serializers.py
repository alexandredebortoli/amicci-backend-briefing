from rest_framework import serializers
from .models import Vendor, Retailer, Category, Briefing


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = "__all__"
