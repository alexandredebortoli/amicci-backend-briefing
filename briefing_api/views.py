from .models import Briefing, Category, Retailer, Vendor
from .serializers import (
    BriefingSerializer,
    CategorySerializer,
    RetailerSerializer,
    VendorSerializer,
)
from rest_framework import generics


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class VendorListAPIView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorCreateAPIView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class RetailerListAPIView(generics.ListAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer


class RetailerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer


class RetailerCreateAPIView(generics.CreateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer


class BriefingListAPIView(generics.ListAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer


class BriefingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer


class BriefingCreateAPIView(generics.CreateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
