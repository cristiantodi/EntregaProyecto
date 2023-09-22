from django.contrib import admin
from proyecto.models import Model_sistem, event, equipment

# Register your models here.

@admin.register(Model_sistem)
class Model_sistem_admin(admin.ModelAdmin):
    list_display = [
                        'id',
                        'model',
                        'os'
                    ]

@admin.register(event)
class even_admin(admin.ModelAdmin):
    list_display = [
                        'id',
                        'event'
                    ]

@admin.register(equipment)
class equipment_admin(admin.ModelAdmin):
    list_display = [
                        'id',
                        'date',
                        'time',
                        'type_equipment',
                        'location',
                        'user',
                        'event'
                    ]