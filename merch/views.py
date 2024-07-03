from django.shortcuts import render
from .models import*
from .forms import*

def inicio(request):
    return render(request, "paginas/inicio.html")

def proximamente(request):
    return render(request, "paginas/proximamente.html")

def cosoSecreto(request):
    return render(request, "paginas/algo.html")

def productos(request):
    contexto = {"Productos": Productos.objects.all()}
    return render(request, "paginas/productos.html", contexto)

def DVD(request):
    contexto = {"DVDs": DVDs.objects.all()}
    return render(request, "paginas/dvds.html", contexto)

def distribuidores(request):
    contexto = {"Distribuidores": Distribuidor.objects.all()}
    return render(request, "paginas/distribuidores.html", contexto)

def productosForm(request):
    if request.method == "POST":
        miForm =ProductosForm(request.POST)
        if miForm.is_valid():
            productos_nombre = miForm.cleaned_data.get("nombre")
            productos_codigo = miForm.cleaned_data.get("codigo")
            productos_precio = miForm.cleaned_data.get("precio")
            productos_fabric = miForm.cleaned_data.get("fabricante")
            producto = Productos(nombre = productos_nombre, 
                                 codigo = productos_codigo, 
                                 precio = productos_precio, 
                                 fabricante = productos_fabric)
            producto.save()
            contexto = {"producto": Productos.objects.all()}
            return render(request, "paginas/productos.html", contexto)
    else:
        miForm = ProductosForm()
    
    return render(request, "paginas/productosFormulario.html", {"form":miForm})

def DVDsForm(request):
    if request.method == "POST":
        miForm =DVDForm(request.POST)
        if miForm.is_valid():
            DVDnombre = miForm.cleaned_data.get("nombre")
            DVDcodigo = miForm.cleaned_data.get("codigo")
            DVDprecio = miForm.cleaned_data.get("precio")
            DVDtipo = miForm.cleaned_data.get("tipo")
            DVDstock =miForm.cleaned_data.get("en_stock")
            dvds= DVDs(nombre = DVDnombre,
                       codigo = DVDcodigo,
                       precio = DVDprecio,
                       tipo = DVDtipo,
                       en_stock = DVDstock)
            dvds.save()
            contexto = {"DVDs": DVDs.objects.all()}
            return render(request, "paginas/dvds.html", contexto)
    else:
        miForm = DVDForm()
    
    return render(request, "paginas/dvdsFormulario.html ", {"form":miForm})

def distForm(request):
    if request.method == "POST":
        miForm = DistribuidorForm(request.POST)
        if miForm.is_valid():
            dist_Empresa = miForm.cleaned_data.get("empresa")
            dist_Repartidor = miForm.cleaned_data.get("repartidor")
            dist_apellido = miForm.cleaned_data.get("apellido")
            dist_edad = miForm.cleaned_data.get("edad")
            distribucion = Distribuidor(
                nombre = dist_Empresa,
                repartido =dist_Repartidor,
                apellido = dist_apellido,
                edad = dist_edad)
            distribucion.save()
            contexto = {"Distribuidor": Distribuidor.objects.all()}

            return render(request, "paginas/distribuidores.html", contexto)
    else:
        miForm = DistribuidorForm()
        return render(request, "paginas/distribuidoresFormulario.html", {"form":miForm})
  

def buscar(request):
    return render(request, "paginas/buscar.html")

def encontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        produc = Productos.objects.filter(nombre__itcontains=patron)
        dvds   = DVDs.objects.filter(nombre__itcontains = patron)  
        contexto = {"productos":produc, "dvds":dvds}
    else:
        contexto = {"productos":Productos.objects.all()}
        return render(request, "paginas/encontrar.html", contexto)