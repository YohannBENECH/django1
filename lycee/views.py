from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus
from django.template import loader


# Example Simple Text Page
# def index(request):
#     return HttpResponse("Racine de lycée")

# Example URL attrib. Page
def detail(request, cursus_id):
    resp = 'result for cursus {}'.format(cursus_id)
    return HttpResponse(resp)


# Using generated html file
def index(request):
    result_list = Cursus.objects.order_by('name')
    # Chargement du template
    template = loader.get_template('lycee/index.html')

    # Context
    context = {
        "liste": result_list,
    }
    return HttpResponse(template.render(context, request))
