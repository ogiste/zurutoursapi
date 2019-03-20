from rest_framework import serializers
from .models import Tour

class TourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ( 
            'id','title', 'cost', 
            'capacity', 'start_datetime', 
            'end_datetime', 'description', 'createdBy_id')
        read_only_fields = ('updatedOn', 'createdOn')

    def create(self, validated_data):
        tour = Tour(**validated_data)
        tour.createdBy_id = self.context['request'].user.id
        tour.save()
        return tour
