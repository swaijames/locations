from django.contrib import admin
from location_api.models import Region, District, Ward

admin.site.register(Region)
admin.site.register(District)
admin.site.register(Ward)