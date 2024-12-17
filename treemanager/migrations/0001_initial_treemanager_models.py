# Generated by Django 5.1.4 on 2024-12-17 11:05

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EspsArborisation',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'esps_arborisation',
            },
        ),
        migrations.CreateModel(
            name='EspsArrosage',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'esps_arrosage',
            },
        ),
        migrations.CreateModel(
            name='EspsArtArbre',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'esps_art_arbre',
            },
        ),
        migrations.CreateModel(
            name='EspsArtSurface',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('labeltext', models.CharField(blank=True, null=True)),
                ('keep', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'esps_art_surface',
            },
        ),
        migrations.CreateModel(
            name='EspsAubanType',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'esps_auban_type',
            },
        ),
        migrations.CreateModel(
            name='EspsConceptAggloy',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'esps_concept_aggloy',
            },
        ),
        migrations.CreateModel(
            name='EspsLocalisation',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'esps_localisation',
            },
        ),
        migrations.CreateModel(
            name='EspsPort',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'esps_port',
            },
        ),
        migrations.CreateModel(
            name='EspsProtectionCastor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'esps_protection_castor',
            },
        ),
        migrations.CreateModel(
            name='EspsRue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('constraining', models.IntegerField(blank=True, null=True)),
                ('rueid', models.SmallIntegerField(blank=True, null=True)),
                ('short_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'esps_rue',
            },
        ),
        migrations.CreateModel(
            name='EspsTypeSol',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'esps_type_sol',
            },
        ),
        migrations.CreateModel(
            name='EspsTypeSousSol',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'esps_type_sous_sol',
            },
        ),
        migrations.CreateModel(
            name='VlSteEspArbreCommemoratif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'vl_ste_esp_arbre_commemoratif',
            },
        ),
        migrations.CreateModel(
            name='VlSteEspArbreRemarquable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'vl_ste_esp_arbre_remarquable',
            },
        ),
        migrations.CreateModel(
            name='VlSteEspControl2023',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vl_ste_esp_control_2023',
                'db_table_comment': 'Valeurs controles arbres 2023',
            },
        ),
        migrations.CreateModel(
            name='VlSteEspControl2024',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vl_ste_esp_control_2024',
            },
        ),
        migrations.CreateModel(
            name='VlSteEspPublicDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'vl_ste_esp_public_domain',
            },
        ),
        migrations.CreateModel(
            name='EspsSubartArbre',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gn_description_custom', models.TextField(blank=True, null=True)),
                ('art_fkey', models.ForeignKey(blank=True, db_column='art_fkey', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espsartarbre')),
            ],
            options={
                'db_table': 'esps_subart_arbre',
            },
        ),
        migrations.CreateModel(
            name='EspsCultivar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('esps_subart_arbre_fkey', models.ForeignKey(blank=True, db_column='esps_subart_arbre_fkey', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espssubartarbre')),
            ],
            options={
                'db_table': 'esps_cultivar',
            },
        ),
        migrations.CreateModel(
            name='EspArbre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diam_tronc', models.FloatField(blank=True, null=True)),
                ('circ_tronc', models.FloatField(blank=True, null=True)),
                ('diam_couronne', models.FloatField(blank=True, null=True)),
                ('rayon_couronne', models.FloatField(blank=True, null=True)),
                ('rayon_tronc', models.FloatField(blank=True, null=True)),
                ('hauteur_arbre', models.FloatField(blank=True, null=True)),
                ('hauteur_tronc', models.FloatField(blank=True, null=True)),
                ('remarques', models.CharField(blank=True, max_length=255, null=True)),
                ('numfiche', models.IntegerField(blank=True, null=True)),
                ('auban_nombre', models.IntegerField(blank=True, null=True)),
                ('date_plantation', models.DateField(blank=True, null=True)),
                ('date_abattage', models.DateField(blank=True, null=True)),
                ('date_auban', models.DateField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(null=True, srid=2056, verbose_name='geom')),
                ('cultivar_id', models.IntegerField(blank=True, null=True)),
                ('photo', models.TextField(blank=True, db_comment='1024', null=True)),
                ('mf_last_edited_user', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('remarque_ctrl_annuel', models.CharField(blank=True, max_length=255, null=True)),
                ('fk_statut', models.IntegerField(blank=True, null=True)),
                ('arbre_commemoratif', models.BooleanField(blank=True, null=True)),
                ('public_domain', models.BooleanField(blank=True, null=True)),
                ('date_remplacement', models.DateField(blank=True, null=True)),
                ('arborisation', models.ForeignKey(blank=True, db_column='arborisation', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espsarborisation')),
                ('arrosage', models.ForeignKey(blank=True, db_column='arrosage', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espsarrosage')),
                ('art', models.ForeignKey(blank=True, db_column='art', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espsartarbre')),
                ('auban_type', models.ForeignKey(blank=True, db_column='auban_type', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espsaubantype')),
                ('concept_aggloy', models.ForeignKey(blank=True, db_column='concept_aggloy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espsconceptaggloy')),
                ('localisation', models.ForeignKey(blank=True, db_column='localisation', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espslocalisation')),
                ('port', models.ForeignKey(blank=True, db_column='port', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espsport')),
                ('fk_protection_castor', models.ForeignKey(blank=True, db_column='fk_protection_castor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espsprotectioncastor')),
                ('rue', models.ForeignKey(blank=True, db_column='rue', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espsrue')),
                ('art_subart', models.ForeignKey(blank=True, db_column='art_subart', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espssubartarbre')),
                ('type_sol', models.ForeignKey(blank=True, db_column='type_sol', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espstypesol')),
                ('type_sous_sol', models.ForeignKey(blank=True, db_column='type_sous_sol', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.espstypesoussol')),
                ('fk_arbre_commemoratif', models.ForeignKey(blank=True, db_column='fk_arbre_commemoratif', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.vlsteesparbrecommemoratif')),
                ('fk_arbre_remarquable', models.ForeignKey(blank=True, db_column='fk_arbre_remarquable', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.vlsteesparbreremarquable')),
                ('fk_control_2023', models.ForeignKey(blank=True, db_column='fk_control_2023', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.vlsteespcontrol2023')),
                ('fk_control_2024', models.ForeignKey(blank=True, db_column='fk_control_2024', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.vlsteespcontrol2024')),
                ('fk_public_domain', models.ForeignKey(blank=True, db_column='fk_public_domain', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treemanager.vlsteesppublicdomain')),
            ],
            options={
                'db_table': 'esp_arbre',
            },
        ),
    ]
