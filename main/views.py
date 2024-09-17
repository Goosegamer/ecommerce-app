from django.shortcuts import render, redirect   # Add import redirect at this line
from main.forms import ProductEntryForm
from main.models import ProductEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_entries = ProductEntry.objects.all()

    context = {
        'npm' : '2406394396',
        'name': 'Guruprasanth Meyyarasu',
        'class': 'PBP E',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)  # Verwende das Formular

    if request.method == "POST" and form.is_valid():  # Überprüfe zuerst die Methode
        form.save()  # Speichert das Produkt
        return redirect('main:show_main')  # Redirect nach dem Speichern

    context = {'form': form}  # Gib das Formular im Kontext weiter
    return render(request, "create_product_entry.html", context)  # Render das Template

def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")