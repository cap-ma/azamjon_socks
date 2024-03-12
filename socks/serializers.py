from rest_framework import serializers
from .models import Banners,Catalog,Product,Faq

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banners
        fields="__all__"

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Catalog
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        
class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faq
        fields="__all__"
    