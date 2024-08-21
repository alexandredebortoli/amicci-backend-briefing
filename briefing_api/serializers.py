from rest_framework import serializers
from .models import Vendor, Retailer, Category, Briefing


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class RetailerSerializer(serializers.ModelSerializer):
    vendors = serializers.PrimaryKeyRelatedField(
        queryset=Vendor.objects.all(), many=True, required=False
    )

    class Meta:
        model = Retailer
        fields = ["id", "name", "vendors"]

    def create(self, validated_data):
        vendors = validated_data.pop("vendors", [])
        retailer = Retailer.objects.create(**validated_data)
        retailer.vendors.set(vendors)
        return retailer

    def update(self, instance, validated_data):
        vendors = validated_data.pop("vendors", [])
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        instance.vendors.set(vendors)
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = "__all__"
