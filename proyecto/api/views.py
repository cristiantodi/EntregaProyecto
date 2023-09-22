from rest_framework.viewsets import ModelViewSet
from proyecto.models import Model_sistem, event, equipment
from proyecto.api.serializers import Model_sistem_Serializer, event_Serializer, equipment_Serializer

class Model_sistem_ApiViewSet(ModelViewSet):
    serializer_class = Model_sistem_Serializer
    queryset = Model_sistem.objects.all()

class event_ApiViewSet(ModelViewSet):
    serializer_class = event_Serializer
    queryset = event.objects.all()

class equipment_ApiViewSet(ModelViewSet):
    serializer_class = equipment_Serializer
    queryset = equipment.objects.all()