from rest_framework import serializers
from .models import Region, District, Ward


# OopCompanion:suppressRename


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    wards = WardSerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = ['id', 'name', 'wards']


class RegionSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ['id', 'name', 'districts']
