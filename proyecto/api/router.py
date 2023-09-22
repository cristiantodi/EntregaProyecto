from rest_framework.routers import DefaultRouter
from proyecto.api.views import Model_sistem_ApiViewSet, event_ApiViewSet, equipment_ApiViewSet

router_proyecto = DefaultRouter()

router_proyecto.register(prefix='Model_sistem', basename='Model_sistem', viewset=Model_sistem_ApiViewSet)
router_proyecto.register(prefix='event', basename='event', viewset=event_ApiViewSet)
router_proyecto.register(prefix='equipment', basename='equipment', viewset=equipment_ApiViewSet)