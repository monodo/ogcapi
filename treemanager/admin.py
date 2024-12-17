from django.apps import apps

# Register your models here.
from django.contrib import admin

from core.fields import AdminGeometryWidget
from treemanager import models

for model in apps.get_app_config("treemanager").models.values():
    admin.site.register(model)

admin.site.unregister(models.EspArbre)


class TreeAdmin(admin.ModelAdmin):
    class Meta:
        model = models.EspArbre

        widgets = {
            "geom": AdminGeometryWidget(),
        }


admin.site.register(models.EspArbre, TreeAdmin)
