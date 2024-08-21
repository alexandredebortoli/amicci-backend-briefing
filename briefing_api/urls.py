from django.urls import path
from . import views

urlpatterns = [
    path(
        "categories",
        views.CategoryListAPIView.as_view(),
        name="category-list",
    ),
    path(
        "category/<int:pk>/",
        views.CategoryRetrieveUpdateAPIView.as_view(),
        name="category-retrieve-update",
    ),
    path(
        "category/",
        views.CategoryCreateAPIView.as_view(),
        name="category-create",
    ),
    path(
        "vendors/",
        views.VendorListAPIView.as_view(),
        name="vendor-list",
    ),
    path(
        "vendor/<int:pk>/",
        views.VendorRetrieveUpdateAPIView.as_view(),
        name="vendor-retrieve-update",
    ),
    path(
        "vendor/",
        views.VendorCreateAPIView.as_view(),
        name="vendor-create",
    ),
]
