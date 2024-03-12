from django.shortcuts import render
from rest_framework import generics

from .models import Banners,Catalog,Product,Faq
from .serializers import BannerSerializer,CatalogSerializer,ProductSerializer,FaqSerializer

class BannersListView(generics.ListAPIView):
    queryset=Banners.objects.all()
    serializer_class=BannerSerializer

class CatalogListView(generics.ListAPIView):
    queryset=Catalog.objects.all()
    serializer_class=CatalogSerializer

class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class FaqListView(generics.ListAPIView):
    queryset=Faq.objects.all()
    serializer_class=FaqSerializer