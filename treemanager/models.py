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
        "TypeArtArbre", models.DO_NOTHING, db_column="art", blank=True, null=True
    )
    art_subart = models.ForeignKey(
        "TypeSubartArbre",
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

    arborisation = models.ForeignKey(
        "TypeArborisation",
        models.DO_NOTHING,
        db_column="arborisation",
        blank=True,
        null=True,
    )
    port = models.ForeignKey(
        "TypePort", models.DO_NOTHING, db_column="port", blank=True, null=True
    )
    hauteur_arbre = models.FloatField(blank=True, null=True)
    hauteur_tronc = models.FloatField(blank=True, null=True)
    type_sol = models.ForeignKey(
        "TypeTypeSol", models.DO_NOTHING, db_column="type_sol", blank=True, null=True
    )
    type_sous_sol = models.ForeignKey(
        "TypeTypeSousSol",
        models.DO_NOTHING,
        db_column="type_sous_sol",
        blank=True,
        null=True,
    )
    concept_aggloy = models.ForeignKey(
        "TypeConceptAggloy",
        models.DO_NOTHING,
        db_column="concept_aggloy",
        blank=True,
        null=True,
    )
    remarques = models.CharField(max_length=255, blank=True, null=True)
    localisation = models.ForeignKey(
        "TypeLocalisation",
        models.DO_NOTHING,
        db_column="localisation",
        blank=True,
        null=True,
    )
    numfiche = models.IntegerField(blank=True, null=True)
    auban_type = models.ForeignKey(
        "TypeAubanType",
        models.DO_NOTHING,
        db_column="auban_type",
        blank=True,
        null=True,
    )
    auban_nombre = models.IntegerField(blank=True, null=True)
    arrosage = models.ForeignKey(
        "TypeArrosage", models.DO_NOTHING, db_column="arrosage", blank=True, null=True
    )
    date_plantation = models.DateField(blank=True, null=True)
    date_abattage = models.DateField(blank=True, null=True)
    date_auban = models.DateField(blank=True, null=True)
    cultivar_id = models.IntegerField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True, db_comment="1024")
    mf_last_edited_user = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    fk_protection_castor = models.ForeignKey(
        "TypeProtectionCastor",
        models.DO_NOTHING,
        db_column="fk_protection_castor",
        blank=True,
        null=True,
    )
    remarque_ctrl_annuel = models.CharField(max_length=255, blank=True, null=True)
    fk_arbre_remarquable = models.ForeignKey(
        "TypeSteEspArbreRemarquable",
        models.DO_NOTHING,
        db_column="fk_arbre_remarquable",
        blank=True,
        null=True,
    )
    fk_statut = models.IntegerField(blank=True, null=True)
    arbre_commemoratif = models.BooleanField(blank=True, null=True)
    public_domain = models.BooleanField(blank=True, null=True)
    fk_arbre_commemoratif = models.ForeignKey(
        "TypeSteEspArbreCommemoratif",
        models.DO_NOTHING,
        db_column="fk_arbre_commemoratif",
        blank=True,
        null=True,
    )
    fk_public_domain = models.ForeignKey(
        "TypeSteEspPublicDomain",
        models.DO_NOTHING,
        db_column="fk_public_domain",
        blank=True,
        null=True,
    )
    date_remplacement = models.DateField(blank=True, null=True)
    geom = geomodels.MultiPointField(_("geom"), null=True, srid=2056)


@register_oapif_viewset(geom_field=None)
class TypeArborisation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeArrosage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeArtArbre(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeArtSurface(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    labeltext = models.CharField(blank=True, null=True)
    keep = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeAubanType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeConceptAggloy(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeCultivar(models.Model):
    name = models.CharField(max_length=255)
    Type_subart_arbre_fkey = models.ForeignKey(
        "TypeSubartArbre",
        models.DO_NOTHING,
        db_column="Type_subart_arbre_fkey",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeLocalisation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypePort(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeProtectionCastor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeSubartArbre(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    gn_description_custom = models.TextField(blank=True, null=True)
    art_fkey = models.ForeignKey(
        TypeArtArbre, models.DO_NOTHING, db_column="art_fkey", blank=True, null=True
    )

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeTypeSol(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeTypeSousSol(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeSteEspArbreCommemoratif(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeSteEspArbreRemarquable(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.id} - {self.name}"


@register_oapif_viewset(geom_field=None)
class TypeSteEspPublicDomain(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"
