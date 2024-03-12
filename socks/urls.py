from django.urls import path
from .views import BannersListView,CatalogListView,ProductListView,FaqListView

urlpatterns=[
    path("banner-list",BannersListView.as_view()),
    path('catalog-list',CatalogListView.as_view()),
    path('product-list',ProductListView.as_view()),
    path('faq-list',FaqListView.as_view()),
]