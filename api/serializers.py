from rest_framework import serializers
from  serwis2.models import  Geoinfo


class GeoinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geoinfo
        fields = ['_type',
                  '_id',
                  'name',
                  'type',
                  'latitude',
                  'longitude',
                  ]




