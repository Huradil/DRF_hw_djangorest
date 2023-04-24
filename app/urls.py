from django.urls import path

from . import views

urlpatterns=[
    path('product/',views.product_list_create_api_view),
    path('category/',views.category_list_create_api_view),
]