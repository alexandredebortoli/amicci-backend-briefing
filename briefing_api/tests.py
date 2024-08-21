from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Briefing, Category, Retailer, Vendor
from .serializers import (
    BriefingSerializer,
    CategorySerializer,
    RetailerSerializer,
    VendorSerializer,
)


class CategoryTests(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(
            name="Category 1", description="Description"
        )
        self.category2 = Category.objects.create(name="Category 2")
        self.base_category_count = Category.objects.count()
        self.list_url = reverse("category-list-create")
        self.retrieve_url = reverse(
            "category-retrieve-update", args=[self.category1.id]
        )
        self.update_url = reverse("category-retrieve-update", args=[self.category1.id])
        self.create_url = reverse("category-list-create")

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
        self.list_url = reverse("vendor-list-create")
        self.retrieve_url = reverse("vendor-retrieve-update", args=[self.vendor1.id])
        self.update_url = reverse("vendor-retrieve-update", args=[self.vendor1.id])
        self.create_url = reverse("vendor-list-create")

    def test_vendor_list(self):
        response = self.client.get(self.list_url)
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
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


class RetailerTests(APITestCase):
    def setUp(self):
        self.vendor1 = Vendor.objects.create(name="Vendor 1")
        self.vendor2 = Vendor.objects.create(name="Vendor 2")
        self.retailer1 = Retailer.objects.create(name="Retailer 1")
        self.retailer1.vendors.set([self.vendor1.id, self.vendor2.id])
        self.retailer2 = Retailer.objects.create(name="Retailer 2")
        self.base_retailer_count = Retailer.objects.count()
        self.list_url = reverse("retailer-list-create")
        self.retrieve_url = reverse(
            "retailer-retrieve-update", args=[self.retailer1.id]
        )
        self.update_url = reverse("retailer-retrieve-update", args=[self.retailer1.id])
        self.create_url = reverse("retailer-list-create")

    def test_retailer_list(self):
        response = self.client.get(self.list_url)
        retailers = Retailer.objects.all()
        serializer = RetailerSerializer(retailers, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retailer_retrieve(self):
        response = self.client.get(self.retrieve_url)
        retailer = Retailer.objects.get(id=self.retailer1.id)
        serializer = RetailerSerializer(retailer)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retailer_create_valid(self):
        response = self.client.post(
            self.create_url,
            data={
                "name": "New Retailer",
                "vendors": [self.vendor1.id, self.vendor2.id],
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Retailer.objects.count(), self.base_retailer_count + 1)
        new_retailer = Retailer.objects.get(id=response.data["id"])
        self.assertEqual(new_retailer.name, "New Retailer")
        vendor_ids = list(self.retailer1.vendors.values_list("id", flat=True))
        self.assertEqual(vendor_ids, [self.vendor1.id, self.vendor2.id])

    def test_retailer_create_invalid(self):
        response = self.client.post(self.create_url, data={"name": ""}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Retailer.objects.count(), self.base_retailer_count)

    def test_retailer_update_valid(self):
        response = self.client.put(
            self.update_url,
            data={"name": "Updated Retailer", "vendors": [self.vendor1.id]},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.retailer1.refresh_from_db()
        self.assertEqual(self.retailer1.name, "Updated Retailer")
        vendor_ids = list(self.retailer1.vendors.values_list("id", flat=True))
        self.assertEqual(vendor_ids, [self.vendor1.id])

    def test_retailer_update_invalid(self):
        response = self.client.put(self.update_url, data={"name": ""}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.retailer1.refresh_from_db()
        self.assertEqual(self.retailer1.name, "Retailer 1")


class BriefingTests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(name="Vendor 1")
        self.retailer = Retailer.objects.create(name="Retailer 1")
        self.retailer.vendors.set([self.vendor.id])
        self.category = Category.objects.create(
            name="Category 1", description="Description of Category 1"
        )

        self.briefing = Briefing.objects.create(
            name="Briefing 1",
            retailer=self.retailer,
            responsible="John Doe",
            category=self.category,
            release_date="2024-08-21",
            available=100,
        )

        self.base_briefing_count = Briefing.objects.count()
        self.list_url = reverse("briefing-list-create")
        self.retrieve_url = reverse("briefing-retrieve-update", args=[self.briefing.id])
        self.update_url = reverse("briefing-retrieve-update", args=[self.briefing.id])
        self.create_url = reverse("briefing-list-create")

    def test_briefing_list(self):
        response = self.client.get(self.list_url)
        briefings = Briefing.objects.all()
        serializer = BriefingSerializer(briefings, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_briefing_retrieve(self):
        response = self.client.get(self.retrieve_url)
        briefing = Briefing.objects.get(id=self.briefing.id)
        serializer = BriefingSerializer(briefing)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_briefing_create_valid(self):
        response = self.client.post(
            self.create_url,
            data={
                "name": "New Briefing",
                "retailer": self.retailer.id,
                "responsible": "Jane Doe",
                "category": self.category.id,
                "release_date": "2024-09-01",
                "available": 150,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Briefing.objects.count(), self.base_briefing_count + 1)
        new_briefing = Briefing.objects.get(id=response.data["id"])
        self.assertEqual(new_briefing.name, "New Briefing")
        self.assertEqual(new_briefing.retailer.id, self.retailer.id)
        self.assertEqual(new_briefing.category.id, self.category.id)
        self.assertEqual(new_briefing.responsible, "Jane Doe")
        self.assertEqual(str(new_briefing.release_date), "2024-09-01")
        self.assertEqual(new_briefing.available, 150)

    def test_briefing_create_invalid(self):
        response = self.client.post(
            self.create_url,
            data={
                "name": "",
                "retailer": self.retailer.id,
                "category": self.category.id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Briefing.objects.count(), self.base_briefing_count)

    def test_briefing_update_valid(self):
        response = self.client.put(
            self.update_url,
            data={
                "name": "Updated Briefing",
                "retailer": self.retailer.id,
                "responsible": "John Smith",
                "category": self.category.id,
                "release_date": "2024-10-01",
                "available": 200,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.briefing.refresh_from_db()
        self.assertEqual(self.briefing.name, "Updated Briefing")
        self.assertEqual(self.briefing.responsible, "John Smith")
        self.assertEqual(str(self.briefing.release_date), "2024-10-01")
        self.assertEqual(self.briefing.available, 200)

    def test_briefing_update_invalid(self):
        response = self.client.put(
            self.update_url,
            data={
                "name": "",
                "retailer": self.retailer.id,
                "category": self.category.id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.briefing.refresh_from_db()
        self.assertEqual(self.briefing.name, "Briefing 1")
