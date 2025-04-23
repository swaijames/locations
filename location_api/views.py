from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Region, District, Ward
from .serializers import RegionSerializer, DistrictSerializer, WardSerializer


@api_view(['GET'])
def get_locations(request):
    level = request.GET.get('level', None)
    parent_id = request.GET.get('parentId', None)

    if level == 'regions':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)

    elif level == 'districts' and parent_id:
        districts = District.objects.filter(region_id=parent_id)
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)

    elif level == 'wards' and parent_id:
        wards = Ward.objects.filter(district_id=parent_id)
        serializer = WardSerializer(wards, many=True)
        return Response(serializer.data)

    return Response([])
