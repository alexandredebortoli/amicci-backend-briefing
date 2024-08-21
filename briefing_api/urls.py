from django.urls import path
from . import views

urlpatterns = [
    path(
        "categories",
        views.CategoryListCreateAPIView.as_view(),
        name="category-list-create",
    ),
    path(
        "categories/<int:pk>",
        views.CategoryRetrieveUpdateAPIView.as_view(),
        name="category-retrieve-update",
    ),
    path(
        "vendors",
        views.VendorListCreateAPIView.as_view(),
        name="vendor-list-create",
    ),
    path(
        "vendors/<int:pk>",
        views.VendorRetrieveUpdateAPIView.as_view(),
        name="vendor-retrieve-update",
    ),
    path(
        "retailers",
        views.RetailerListCreateAPIView.as_view(),
        name="retailer-list-create",
    ),
    path(
        "retailers/<int:pk>",
        views.RetailerRetrieveUpdateAPIView.as_view(),
        name="retailer-retrieve-update",
    ),
    path(
        "briefings",
        views.BriefingListCreateAPIView.as_view(),
        name="briefing-list-create",
    ),
    path(
        "briefings/<int:pk>",
        views.BriefingRetrieveUpdateAPIView.as_view(),
        name="briefing-retrieve-update",
    ),
]
