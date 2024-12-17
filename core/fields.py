from django.contrib.gis import forms as geoforms


class AdminGeometryWidget(geoforms.OSMWidget):
    template_name = "admin-geometry-widget.html"
    map_srid = (
        3857  # Avoids to load proj4 and keep as close a possible to native widget
    )
