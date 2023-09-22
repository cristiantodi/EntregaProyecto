from rest_framework import serializers
from proyecto.models import Model_sistem, event, equipment

class Model_sistem_Serializer(serializers.ModelSerializer):
    class Meta:
        model   = Model_sistem
        fields = [
                            'id',
                            'model',
                            'os'
                        ]


class event_Serializer(serializers.ModelSerializer):
    class Meta:
        model   = event
        fields = [
                            'id',
                            'event'
                        ]
    
class equipment_Serializer(serializers.ModelSerializer):
    class Meta:
        model   = equipment
        fields = [
                            'id',
                            'date',
                            'time',
                            'type_equipment',
                            'location',
                            'user',
                            'event'
                        ]