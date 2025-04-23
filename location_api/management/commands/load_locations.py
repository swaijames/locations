import os
import sys
from django.core.management.base import BaseCommand
from location_api.models import Region, District, Ward


# OopCompanion:suppressRename


class Command(BaseCommand):
    help = 'Loads Dar es Salaam regions, districts, and wards into database'

    def handle(self, *args, **options):
        self.stdout.write("Starting to load location data...")

        # Define all location data
        location_data = {
            'regions': [
                {'id': 1, 'name': 'Dar es Salaam'}
            ],
            'districts': [
                {'id': 1, 'region_id': 1, 'name': 'Ilala'},
                {'id': 2, 'region_id': 1, 'name': 'Kinondoni'},
                {'id': 3, 'region_id': 1, 'name': 'Temeke'},
                {'id': 4, 'region_id': 1, 'name': 'Ubungo'},
                {'id': 5, 'region_id': 1, 'name': 'Kigamboni'}
            ],
            'wards': [
                # Ilala District Wards (23 wards)
                {'id': 1, 'district_id': 1, 'name': 'Buguruni'},
                {'id': 2, 'district_id': 1, 'name': 'Bunju'},
                {'id': 3, 'district_id': 1, 'name': 'Gerezani'},
                {'id': 4, 'district_id': 1, 'name': 'Ilala'},
                {'id': 5, 'district_id': 1, 'name': 'Kariakoo'},
                {'id': 6, 'district_id': 1, 'name': 'Kiburugwa'},
                {'id': 7, 'district_id': 1, 'name': 'Kimanga'},
                {'id': 8, 'district_id': 1, 'name': 'Kinyerezi'},
                {'id': 9, 'district_id': 1, 'name': 'Kipawa'},
                {'id': 10, 'district_id': 1, 'name': 'Kitunda'},
                {'id': 11, 'district_id': 1, 'name': 'Kivukoni'},
                {'id': 12, 'district_id': 1, 'name': 'Kiwalani'},
                {'id': 13, 'district_id': 1, 'name': 'Mchafukoge'},
                {'id': 14, 'district_id': 1, 'name': 'Msongola'},
                {'id': 15, 'district_id': 1, 'name': 'Pugu'},
                {'id': 16, 'district_id': 1, 'name': 'Segerea'},
                {'id': 17, 'district_id': 1, 'name': 'Tabata'},
                {'id': 18, 'district_id': 1, 'name': 'Ukonga'},
                {'id': 19, 'district_id': 1, 'name': 'Upanga Mashariki'},
                {'id': 20, 'district_id': 1, 'name': 'Upanga Magharibi'},
                {'id': 21, 'district_id': 1, 'name': 'Vingunguti'},
                {'id': 22, 'district_id': 1, 'name': 'Yombo Vituka'},
                {'id': 23, 'district_id': 1, 'name': 'Chanika'},

                # Kinondoni District Wards (27 wards)
                {'id': 24, 'district_id': 2, 'name': 'Kawe'},
                {'id': 25, 'district_id': 2, 'name': 'Kinondoni'},
                {'id': 26, 'district_id': 2, 'name': 'Mikocheni'},
                {'id': 27, 'district_id': 2, 'name': 'Msasani'},
                {'id': 28, 'district_id': 2, 'name': 'Mwananyamala'},
                {'id': 29, 'district_id': 2, 'name': 'Kijitonyama'},
                {'id': 30, 'district_id': 2, 'name': 'Magomeni'},
                {'id': 31, 'district_id': 2, 'name': 'Makumbusho'},
                {'id': 32, 'district_id': 2, 'name': 'Mbezi'},
                {'id': 33, 'district_id': 2, 'name': 'Mbweni'},
                {'id': 34, 'district_id': 2, 'name': 'Mpakani'},
                {'id': 35, 'district_id': 2, 'name': 'Mwananyamala'},
                {'id': 36, 'district_id': 2, 'name': 'Ndugumbi'},
                {'id': 37, 'district_id': 2, 'name': 'Sinza'},
                {'id': 38, 'district_id': 2, 'name': 'Tandale'},
                {'id': 39, 'district_id': 2, 'name': 'Ubungo'},
                {'id': 40, 'district_id': 2, 'name': 'Goba'},
                {'id': 41, 'district_id': 2, 'name': 'Hananasif'},
                {'id': 42, 'district_id': 2, 'name': 'Kigogo'},
                {'id': 43, 'district_id': 2, 'name': 'Kimara'},
                {'id': 44, 'district_id': 2, 'name': 'Kunduchi'},
                {'id': 45, 'district_id': 2, 'name': 'Makongo'},
                {'id': 46, 'district_id': 2, 'name': 'Makurumla'},
                {'id': 47, 'district_id': 2, 'name': 'Mbezi Luis'},
                {'id': 48, 'district_id': 2, 'name': 'Mburahati'},
                {'id': 49, 'district_id': 2, 'name': 'Mwenge'},
                {'id': 50, 'district_id': 2, 'name': 'Wazo'},

                # Temeke District Wards (22 wards)
                {'id': 51, 'district_id': 3, 'name': 'Temeke'},
                {'id': 52, 'district_id': 3, 'name': 'Kigamboni'},
                {'id': 53, 'district_id': 3, 'name': 'Mbagala'},
                {'id': 54, 'district_id': 3, 'name': 'Azimio'},
                {'id': 55, 'district_id': 3, 'name': 'Chamazi'},
                {'id': 56, 'district_id': 3, 'name': 'Charambe'},
                {'id': 57, 'district_id': 3, 'name': 'Kiburani'},
                {'id': 58, 'district_id': 3, 'name': 'Kijichi'},
                {'id': 59, 'district_id': 3, 'name': 'Kurasini'},
                {'id': 60, 'district_id': 3, 'name': 'Makangarawe'},
                {'id': 61, 'district_id': 3, 'name': 'Majohe'},
                {'id': 62, 'district_id': 3, 'name': 'Mbagala Kuu'},
                {'id': 63, 'district_id': 3, 'name': 'Mbagala Rangitatu'},
                {'id': 64, 'district_id': 3, 'name': 'Mianzini'},
                {'id': 65, 'district_id': 3, 'name': 'Sandali'},
                {'id': 66, 'district_id': 3, 'name': 'Tandika'},
                {'id': 67, 'district_id': 3, 'name': 'Toangoma'},
                {'id': 68, 'district_id': 3, 'name': 'Tungi'},
                {'id': 69, 'district_id': 3, 'name': 'Mtoni'},
                {'id': 70, 'district_id': 3, 'name': 'Kijitonyama'},
                {'id': 71, 'district_id': 3, 'name': 'Keko'},
                {'id': 72, 'district_id': 3, 'name': 'Miburani'},

                # Ubungo District Wards (12 wards)
                {'id': 73, 'district_id': 4, 'name': 'Ubungo'},
                {'id': 74, 'district_id': 4, 'name': 'Goba'},
                {'id': 75, 'district_id': 4, 'name': 'Kibamba'},
                {'id': 76, 'district_id': 4, 'name': 'Kimara'},
                {'id': 77, 'district_id': 4, 'name': 'Kunduchi'},
                {'id': 78, 'district_id': 4, 'name': 'Mburahati'},
                {'id': 79, 'district_id': 4, 'name': 'Saranga'},
                {'id': 80, 'district_id': 4, 'name': 'Soweto'},
                {'id': 81, 'district_id': 4, 'name': 'Tabata'},
                {'id': 82, 'district_id': 4, 'name': 'Ukonga'},
                {'id': 83, 'district_id': 4, 'name': 'Wazo'},
                {'id': 84, 'district_id': 4, 'name': 'Mbezi'},

                # Kigamboni District Wards (10 wards)
                {'id': 85, 'district_id': 5, 'name': 'Kigamboni'},
                {'id': 86, 'district_id': 5, 'name': 'Kisarawe II'},
                {'id': 87, 'district_id': 5, 'name': 'Mbagala Kuu'},
                {'id': 88, 'district_id': 5, 'name': 'Mji Mwema'},
                {'id': 89, 'district_id': 5, 'name': 'Somangila'},
                {'id': 90, 'district_id': 5, 'name': 'Tungi'},
                {'id': 91, 'district_id': 5, 'name': 'Vijibweni'},
                {'id': 92, 'district_id': 5, 'name': 'Kimbiji'},
                {'id': 93, 'district_id': 5, 'name': 'Kisiju'},
                {'id': 94, 'district_id': 5, 'name': 'Pande'}
            ]
        }

        # Clear existing data
        self.stdout.write("Clearing old data...")
        Ward.objects.all().delete()
        District.objects.all().delete()
        Region.objects.all().delete()

        # Create regions
        self.stdout.write("Creating regions...")
        for region in location_data['regions']:
            Region.objects.get_or_create(
                id=region['id'],
                defaults={'name': region['name']}
            )

        # Create districts
        self.stdout.write("Creating districts...")
        for district in location_data['districts']:
            District.objects.get_or_create(
                id=district['id'],
                defaults={
                    'name': district['name'],
                    'region_id': district['region_id']
                }
            )

        # Create wards
        self.stdout.write("Creating wards...")
        for ward in location_data['wards']:
            Ward.objects.get_or_create(
                id=ward['id'],
                defaults={
                    'name': ward['name'],
                    'district_id': ward['district_id']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded all location data!'))
