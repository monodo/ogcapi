# Create your models here.

from django.contrib.gis.db import models
from django.contrib.gis.db import models as geomodels

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_oapif.decorators import register_oapif_viewset


@register_oapif_viewset()
class EspArbre(models.Model):
    art = models.ForeignKey(
        "EspsArtArbre", models.DO_NOTHING, db_column="art", blank=True, null=True
    )
    art_subart = models.ForeignKey(
        "EspsSubartArbre",
        models.DO_NOTHING,
        db_column="art_subart",
        blank=True,
        null=True,
    )
    diam_tronc = models.FloatField(blank=True, null=True)
    circ_tronc = models.FloatField(blank=True, null=True)
    diam_couronne = models.FloatField(blank=True, null=True)
    rayon_couronne = models.FloatField(blank=True, null=True)
    rayon_tronc = models.FloatField(blank=True, null=True)
    rue = models.ForeignKey(
        "EspsRue", models.DO_NOTHING, db_column="rue", blank=True, null=True
    )
    arborisation = models.ForeignKey(
        "EspsArborisation",
        models.DO_NOTHING,
        db_column="arborisation",
        blank=True,
        null=True,
    )
    port = models.ForeignKey(
        "EspsPort", models.DO_NOTHING, db_column="port", blank=True, null=True
    )
    hauteur_arbre = models.FloatField(blank=True, null=True)
    hauteur_tronc = models.FloatField(blank=True, null=True)
    type_sol = models.ForeignKey(
        "EspsTypeSol", models.DO_NOTHING, db_column="type_sol", blank=True, null=True
    )
    type_sous_sol = models.ForeignKey(
        "EspsTypeSousSol",
        models.DO_NOTHING,
        db_column="type_sous_sol",
        blank=True,
        null=True,
    )
    concept_aggloy = models.ForeignKey(
        "EspsConceptAggloy",
        models.DO_NOTHING,
        db_column="concept_aggloy",
        blank=True,
        null=True,
    )
    remarques = models.CharField(max_length=255, blank=True, null=True)
    localisation = models.ForeignKey(
        "EspsLocalisation",
        models.DO_NOTHING,
        db_column="localisation",
        blank=True,
        null=True,
    )
    numfiche = models.IntegerField(blank=True, null=True)
    auban_type = models.ForeignKey(
        "EspsAubanType",
        models.DO_NOTHING,
        db_column="auban_type",
        blank=True,
        null=True,
    )
    auban_nombre = models.IntegerField(blank=True, null=True)
    arrosage = models.ForeignKey(
        "EspsArrosage", models.DO_NOTHING, db_column="arrosage", blank=True, null=True
    )
    date_plantation = models.DateField(blank=True, null=True)
    date_abattage = models.DateField(blank=True, null=True)
    date_auban = models.DateField(blank=True, null=True)
    geom = geomodels.MultiPointField(_("geom"), null=True, srid=2056)
    cultivar_id = models.IntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True, db_comment="1024")
    mf_last_edited_user = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    fk_protection_castor = models.ForeignKey(
        "EspsProtectionCastor",
        models.DO_NOTHING,
        db_column="fk_protection_castor",
        blank=True,
        null=True,
    )
    fk_control_2023 = models.ForeignKey(
        "VlSteEspControl2023",
        models.DO_NOTHING,
        db_column="fk_control_2023",
        blank=True,
        null=True,
    )
    remarque_ctrl_annuel = models.CharField(max_length=255, blank=True, null=True)
    fk_arbre_remarquable = models.ForeignKey(
        "VlSteEspArbreRemarquable",
        models.DO_NOTHING,
        db_column="fk_arbre_remarquable",
        blank=True,
        null=True,
    )
    fk_control_2024 = models.ForeignKey(
        "VlSteEspControl2024",
        models.DO_NOTHING,
        db_column="fk_control_2024",
        blank=True,
        null=True,
    )
    fk_statut = models.IntegerField(blank=True, null=True)
    arbre_commemoratif = models.BooleanField(blank=True, null=True)
    public_domain = models.BooleanField(blank=True, null=True)
    fk_arbre_commemoratif = models.ForeignKey(
        "VlSteEspArbreCommemoratif",
        models.DO_NOTHING,
        db_column="fk_arbre_commemoratif",
        blank=True,
        null=True,
    )
    fk_public_domain = models.ForeignKey(
        "VlSteEspPublicDomain",
        models.DO_NOTHING,
        db_column="fk_public_domain",
        blank=True,
        null=True,
    )
    date_remplacement = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "esp_arbre"


@register_oapif_viewset(geom_field=None)
class EspsArborisation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:

        db_table = "esps_arborisation"


@register_oapif_viewset(geom_field=None)
class EspsArrosage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:

        db_table = "esps_arrosage"


@register_oapif_viewset(geom_field=None)
class EspsArtArbre(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:

        db_table = "esps_art_arbre"


@register_oapif_viewset(geom_field=None)
class EspsArtSurface(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    labeltext = models.CharField(blank=True, null=True)
    keep = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = "esps_art_surface"


@register_oapif_viewset(geom_field=None)
class EspsAubanType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:

        db_table = "esps_auban_type"


@register_oapif_viewset(geom_field=None)
class EspsConceptAggloy(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:

        db_table = "esps_concept_aggloy"


@register_oapif_viewset(geom_field=None)
class EspsCultivar(models.Model):
    name = models.CharField(max_length=255)
    esps_subart_arbre_fkey = models.ForeignKey(
        "EspsSubartArbre",
        models.DO_NOTHING,
        db_column="esps_subart_arbre_fkey",
        blank=True,
        null=True,
    )

    class Meta:

        db_table = "esps_cultivar"


@register_oapif_viewset(geom_field=None)
class EspsLocalisation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:

        db_table = "esps_localisation"


@register_oapif_viewset(geom_field=None)
class EspsPort(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:

        db_table = "esps_port"


@register_oapif_viewset(geom_field=None)
class EspsProtectionCastor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = "esps_protection_castor"


@register_oapif_viewset(geom_field=None)
class EspsRue(models.Model):
    code = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    constraining = models.IntegerField(blank=True, null=True)
    rueid = models.SmallIntegerField(blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = "esps_rue"


@register_oapif_viewset(geom_field=None)
class EspsSubartArbre(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    gn_description_custom = models.TextField(blank=True, null=True)
    art_fkey = models.ForeignKey(
        EspsArtArbre, models.DO_NOTHING, db_column="art_fkey", blank=True, null=True
    )

    class Meta:

        db_table = "esps_subart_arbre"


@register_oapif_viewset(geom_field=None)
class EspsTypeSol(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:

        db_table = "esps_type_sol"


@register_oapif_viewset(geom_field=None)
class EspsTypeSousSol(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:

        db_table = "esps_type_sous_sol"


@register_oapif_viewset(geom_field=None)
class VlSteEspArbreCommemoratif(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = "vl_ste_esp_arbre_commemoratif"


@register_oapif_viewset(geom_field=None)
class VlSteEspArbreRemarquable(models.Model):
    name = models.CharField(max_length=25)

    class Meta:

        db_table = "vl_ste_esp_arbre_remarquable"


@register_oapif_viewset(geom_field=None)
class VlSteEspControl2023(models.Model):
    name = models.CharField(max_length=255)

    class Meta:

        db_table = "vl_ste_esp_control_2023"
        db_table_comment = "Valeurs controles arbres 2023"


@register_oapif_viewset(geom_field=None)
class VlSteEspControl2024(models.Model):
    name = models.CharField(max_length=255)

    class Meta:

        db_table = "vl_ste_esp_control_2024"


@register_oapif_viewset(geom_field=None)
class VlSteEspPublicDomain(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = "vl_ste_esp_public_domain"
