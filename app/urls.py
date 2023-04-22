from django.urls import path

from . import views

urlpatterns=[
    path('product/',views.ProductListCreateAPIView.as_view()),
    path('category/',views.CategoryListCreateAPIView.as_view()),
]