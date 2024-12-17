from django.core.management.base import BaseCommand
from django.db import transaction

from treemanager import models
import json
from django.apps import apps
from django.contrib.gis.geos import GEOSGeometry


class Command(BaseCommand):
    help = "Import Value Lists from real data export"

    @transaction.atomic
    def handle(self, *args, **options):

        datafiles_to_models_map = {
            "mf_ste_esp.esps_subart_arbre.json": "TypeSubartArbre",
            "mf_ste_esp.esps_arborisation.json": "TypeArborisation",
            "mf_ste_esp.esps_arrosage.json": "TypeArrosage",
            "mf_ste_esp.esps_art_arbre.json": "TypeArtArbre",
            "mf_ste_esp.esps_art_surface.json": "TypeArtSurface",
            "mf_ste_esp.esps_auban_type.json": "TypeAubanType",
            "mf_ste_esp.esps_concept_aggloy.json": "TypeConceptAggloy",
            "mf_ste_esp.esps_cultivar.json": "TypeCultivar",
            "mf_ste_esp.esps_localisation.json": "TypeLocalisation",
            "mf_ste_esp.esps_port.json": "TypePort",
            "mf_ste_esp.esps_protection_castor.json": "TypeProtectionCastor",
            "mf_ste_esp.esps_subart_surface.json": "TypeArtSurface",
            "mf_ste_esp.esps_type_sol.json": "TypeTypeSol",
            "mf_ste_esp.esps_type_sous_sol.json": "TypeTypeSousSol",
            "mf_ste_esp.vl_ste_esp_arbre_commemoratif.json": "TypeSteEspArbreCommemoratif",
            "mf_ste_esp.vl_ste_esp_arbre_remarquable.json": "TypeSteEspArbreRemarquable",
            "mf_ste_esp.vl_ste_esp_public_domain.json": "TypeSteEspPublicDomain",
        }

        dir = "/code/demodata"
        for filename in datafiles_to_models_map.keys():
            if filename.endswith(".json"): 

                with open(f"{dir}/{filename}") as data_file: 
                    
                    # model = apps.get_model('treemanager', datafiles_to_models_map[filename])
                    if filename in datafiles_to_models_map:
                        current_model = apps.get_model('treemanager', datafiles_to_models_map[filename])
                        current_model.objects.all().delete()
 
                        data = json.load(data_file)

                        # TODO: import related value lists: TypeArt / Cultivars / Subarts...
                        for v in data:
                            current_model.objects.create(id=v['id'], name=v['name'])

                continue
            else:
                continue
        
        print(
            f"👥 added value lists"
        )

        # import trees

        with open(f"{dir}/mf_ste_esp.esp_arbre.json") as data_file:
            models.EspArbre.objects.all().delete()
            data = json.load(data_file)
            i = 0
            while i < 2500:
                i+=1
                v = data[i]
                multipoint = GEOSGeometry(v['wkt_geometry'])
                models.EspArbre.objects.create(diam_tronc=v['diam_tronc'], id=v['id'], geom=multipoint)



        print(
            f"👥 added trees"
        )
