from django.shortcuts import render

from .models import Factura,LineaDeFactura
# Create your views here.


def factura(request):
    facturas = Factura.objects.all()
    context = {"facturas": facturas
                }
    return render(request, "index.html", context)

def linea(request,pk):
    factura = Factura.objects.get(pk=pk)
    lineas_factura = factura.lineadefactura_set.all()
    count = 0
    for e in lineas_factura:
        count = LineaDeFactura.total(e) + count
    
    context = {
        "total_factura": count,
        "lineas_factura": lineas_factura,
    }

    return render(request, "information.html", context)


