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
]
