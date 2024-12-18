from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    template = loader.get_template("home.html")
    context = {
        "message": "Welcome to OGCAPI demo",
        "ogc_endpoint": f"{request.build_absolute_uri('/')}/oapif",
        "admin": f"{request.build_absolute_uri('/')}/admin"
    }
    return HttpResponse(template.render(context, request))