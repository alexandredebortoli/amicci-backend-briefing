from .models import Briefing, Category, Retailer, Vendor
from .serializers import (
    BriefingSerializer,
    CategorySerializer,
    RetailerSerializer,
    VendorSerializer,
)
from rest_framework import generics


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class RetailerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer


class RetailerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer


class BriefingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer


class BriefingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
