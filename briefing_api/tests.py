from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Category, Vendor
from .serializers import CategorySerializer, VendorSerializer


class CategoryTests(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(
            name="Category 1", description="Description"
        )
        self.category2 = Category.objects.create(name="Category 2")
        self.base_category_count = Category.objects.count()
        self.list_url = reverse("category-list")
        self.retrieve_url = reverse(
            "category-retrieve-update", args=[self.category1.id]
        )
        self.update_url = reverse("category-retrieve-update", args=[self.category1.id])
        self.create_url = reverse("category-create")

    def test_category_list(self):
        response = self.client.get(self.list_url)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_category_retrieve(self):
        response = self.client.get(self.retrieve_url)
        category = Category.objects.get(id=self.category1.id)
        serializer = CategorySerializer(category)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_category_create_valid(self):
        response = self.client.post(
            self.create_url, data={"name": "New Category"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), self.base_category_count + 1)
        self.assertEqual(
            Category.objects.get(id=response.data["id"]).name, "New Category"
        )

    def test_category_create_invalid(self):
        response = self.client.post(self.create_url, data={"name": ""}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), self.base_category_count)

    def test_category_update_valid(self):
        response = self.client.put(
            self.update_url, data={"name": "Updated Category"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category1.refresh_from_db()
        self.assertEqual(self.category1.name, "Updated Category")

    def test_category_update_invalid(self):
        response = self.client.put(self.update_url, data={"name": ""}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.category1.refresh_from_db()
        self.assertEqual(self.category1.name, "Category 1")


class VendorTests(APITestCase):
    def setUp(self):
        self.vendor1 = Vendor.objects.create(name="Vendor 1")
        self.vendor2 = Vendor.objects.create(name="Vendor 2")
        self.base_vendor_count = Vendor.objects.count()
        self.list_url = reverse("vendor-list")
        self.retrieve_url = reverse("vendor-retrieve-update", args=[self.vendor1.id])
        self.update_url = reverse("vendor-retrieve-update", args=[self.vendor1.id])
        self.create_url = reverse("vendor-create")

    def test_vendor_list(self):
        response = self.client.get(self.list_url)
        categories = Vendor.objects.all()
        serializer = VendorSerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_vendor_retrieve(self):
        response = self.client.get(self.retrieve_url)
        vendor = Vendor.objects.get(id=self.vendor1.id)
        serializer = VendorSerializer(vendor)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_vendor_create_valid(self):
        response = self.client.post(
            self.create_url, data={"name": "New Vendor"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), self.base_vendor_count + 1)
        self.assertEqual(Vendor.objects.get(id=response.data["id"]).name, "New Vendor")

    def test_vendor_create_invalid(self):
        response = self.client.post(self.create_url, data={"name": ""}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Vendor.objects.count(), self.base_vendor_count)

    def test_vendor_update_valid(self):
        response = self.client.put(
            self.update_url, data={"name": "Updated Vendor"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor1.refresh_from_db()
        self.assertEqual(self.vendor1.name, "Updated Vendor")

    def test_vendor_update_invalid(self):
        response = self.client.put(self.update_url, data={"name": ""}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.vendor1.refresh_from_db()
        self.assertEqual(self.vendor1.name, "Vendor 1")
