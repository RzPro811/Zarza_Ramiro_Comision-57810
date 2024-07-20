from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#Principal
def home(request):
    return render(request, "tienda/index.html")
def acerca_de(request):
    return render(request, "tienda/acerca_de.html")
@login_required
def buscar(request):
    return render(request, "tienda/buscar.html")
@login_required
def encontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        peluches = Peluches.objects.filter(producto__icontains=patron)
        cartas   = Cartas.objects.filter(juego__icontains=patron)
        mesa     = Juegos_de_Mesa.objects.filter(juego__icontains=patron)
        figuras  = Figura_de_Accion.objects.filter(figura__icontains=patron)    
        contexto = {
            "peluches":peluches,
            "figuras" :figuras,
            "cartas"  :cartas,
            "mesa"    :mesa
        }
    else:
        contexto = {
            "peluches":Peluches.objects.all(),
            "figuras" :Figura_de_Accion.objects.all(),
            "cartas"  :Cartas.objects.all(),
            "mesa"    :Juegos_de_Mesa.objects.all()
        }
    return render(request, "tienda/encontrar.html", contexto)

#login
def iniciar_sesion(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave   = request.POST["password"]
        user    = authenticate(request, username = usuario, password = clave)
        if user is not None:
            login(request, user)
            try:
                avatar = Avatar.objects.get(user = request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            return render(request, "tienda/index.html")
        else:
            return redirect(reverse_lazy("login"))
    else:
        miForm = AuthenticationForm()
    return render(request, "tlogin/login.html", {"form":miForm})
def registrar_usuario(request):
    if request.method == "POST":
        miForm = Registrar_Usuario(request.POST)
        if miForm.is_valid():
           
            miForm.save()
            return redirect(reverse_lazy("home"))        
    else:
        miForm = Registrar_Usuario()
    return render(request, "tlogin/registro.html", {"form":miForm})
@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        miForm = Editar_Usuario(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username = usuario)
            user.email      = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name  = miForm.cleaned_data.get("last_name")
            user.password   = miForm.cleaned_data.get("password")
            miForm.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = Editar_Usuario(instance = usuario)
    return render(request, "tlogin/editar_usuario.html", {"form":miForm})
@login_required
def agregar_avatar(request):
    if request.method == "POST":
        miForm = Crear_Avatar_Form(request.POST, request.FILES)
        if miForm.is_valid:
            usuario = User.objects.get(username = request.user)
            imagen  = miForm.cleaned_data["imagen"]
            avatarViejo = Avatar.objects.filter(user = usuario)
            if len(avatarViejo)>0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user = usuario, imagen = imagen)
            avatar.save()
            imagen = Avatar.objects.get(user = usuario).imagen.url
            request.session["avatar"] = imagen
            return redirect(reverse_lazy("home"))
    else:
        miForm = Crear_Avatar_Form()
    return render(request, "tlogin/avatar.html", {"form":miForm})
@login_required
def cerrar_sesion(request):
    logout(request)
    return render(request, "tlogin/logout.html")

#Peluches
@login_required
def peluches(request):
    contexto = {"Peluche":Peluches.objects.all()}
    return render(request, "Peluches/inicio.html", contexto)
@login_required
def peluchesAdd(request):
    if request.method == "POST":
        miForm = PeluchesForm(request.POST, request.FILES)
        if miForm.is_valid():
            peluche_producto    = miForm.cleaned_data.get("producto")
            peluche_precio      = miForm.cleaned_data.get("precio")
            peluche_disponibles = miForm.cleaned_data.get("disponibles")
            if peluche_disponibles > 0:
                peluche_stock = True
            else:
                peluche_stock = False
            peluche = Peluches(
                producto    = peluche_producto,
                precio      = peluche_precio,
                disponibles = peluche_disponibles,
                en_stock    = peluche_stock
            )
            peluche.save()
            contexto = {"Peluche":Peluches.objects.all()}
            return render(request, "Peluches/inicio.html", contexto)
    else:
        miForm = PeluchesForm
        
    return render(request, "Peluches/formulario.html", {"form": miForm}) 
@login_required
def peluchesUpdate(request, id_peluche):
    peluche = Peluches.objects.get(id=id_peluche)
    if request.method == "POST":
        miForm = PeluchesForm(request.POST, request.FILES)
        if miForm.is_valid():
            peluche.producto    = miForm.cleaned_data.get("producto")
            peluche.precio      = miForm.cleaned_data.get("precio")
            peluche.disponibles = miForm.cleaned_data.get("disponibles")
            if peluche.disponibles > 0:
                peluche.en_stock = True
            else:
                peluche.en_stock = False
            peluche.save()
            contexto = {"Peluche":Peluches.objects.all()}
            return render(request, "Peluches/inicio.html", contexto)
    else:
        miForm = PeluchesForm(initial={
            "producto"   :peluche.producto,
            "precio"     :peluche.precio,
            "disponibles":peluche.disponibles,
        })
    return render(request, "Peluches/formulario.html", {"form":miForm})
@login_required
def peluchesDelete(request,id_peluche):
    peluche = Peluches.objects.get(id=id_peluche)
    peluche.delete()
    contexto = {"Peluche":Peluches.objects.all()}
    return render(request, "Peluches/inicio.html", contexto)
@login_required
def peluchesComprar(request,id_peluche):
    compra     = Peluches.objects.get(id=id_peluche)
    estantería = Peluches.objects.all()
    contexto   = {"compra":compra,"Peluche":estantería}
    return render(request, "Peluches/compra.html", contexto)
@login_required
def peluchesComprado(request,id_peluche):
    peluche = Peluches.objects.get(id=id_peluche)
    peluche.disponibles -= 1
    if peluche.disponibles == 0:
        peluche.en_stock = False
    peluche.save()
    return render(request, "Peluches/venta.html", {"compra":peluche})
    
#Figuras de Accion
@login_required
def figuras_de_accion(request):
    contexto = {"figura":Figura_de_Accion.objects.all()}
    return render(request, "FigurasACC/inicio.html", contexto)
@login_required
def figurasAdd(request):
    if request.method == "POST":
        miForm = FigurasAccionForm(request.POST)
        if miForm.is_valid():
            figuras_figura      = miForm.cleaned_data.get("figura")
            figuras_origen      = miForm.cleaned_data.get("origen")
            figuras_fabricante  = miForm.cleaned_data.get("fabricante")
            figuras_precio      = miForm.cleaned_data.get("precio")
            figuras_disponible  = miForm.cleaned_data.get("disponibles")
            if figuras_disponible > 0:
                figuras_stock = True
            else:
                figuras_stock = False
            figuras = Figura_de_Accion(
                figura      = figuras_figura,
                origen      = figuras_origen,
                fabricante  = figuras_fabricante,
                precio      = figuras_precio,
                disponibles = figuras_disponible,
                en_stock    = figuras_stock
            )
            figuras.save()
            contexto = {"figura":Figura_de_Accion.objects.all()}
            return render(request, "FigurasACC/inicio.html", contexto)
    else:
        miForm = FigurasAccionForm
    return render(request, "FigurasACC/formulario.html", {"form":miForm})
@login_required
def figurasUpdate(request, id_figura):
    figuras = Figura_de_Accion.objects.get(id=id_figura) 
    if request.method == "POST":
        miForm = FigurasAccionForm(request.POST)
        if miForm.is_valid():
            figuras.figura       = miForm.cleaned_data.get("figura")
            figuras.origen       = miForm.cleaned_data.get("origen")
            figuras.fabricante   = miForm.cleaned_data.get("fabricante")
            figuras.precio       = miForm.cleaned_data.get("precio")
            figuras.disponibles  = miForm.cleaned_data.get("disponibles")
            if figuras.disponibles > 0:
                figuras.en_stock = True
            else:
                figuras.en_stock = False
            figuras.save()
            contexto = {"figura":Figura_de_Accion.objects.all()}
            return render(request, "FigurasACC/inicio.html", contexto)
    else:
        miForm = FigurasAccionForm(initial={
            "figura"     :figuras.figura,
            "origen"     :figuras.origen,
            "fabricante" :figuras.fabricante,
            "precio"     :figuras.precio,
            "disponibles":figuras.disponibles,
        })
    return render(request, "FigurasACC/formulario.html", {"form":miForm})
@login_required
def figurasDelete(request,id_figura):
    figuras = Figura_de_Accion.objects.get(id=id_figura)
    figuras.delete()
    contexto = {"figura":Figura_de_Accion.objects.all()}
    return render(request, "FigurasACC/inicio.html", contexto)
@login_required
def figurasComprar(request,id_figura):
    compra     = Figura_de_Accion.objects.get(id=id_figura)
    estantería = Figura_de_Accion.objects.all()
    contexto   = {"compra":compra,"figura":estantería}
    return render(request, "FigurasACC/compra.html", contexto)
@login_required
def figurasComprado(request,id_figura):
    figuras = Figura_de_Accion.objects.get(id=id_figura)
    figuras.disponibles -= 1
    if figuras.disponibles == 0:
        figuras.en_stock = False
    figuras.save()
    return render(request, "FigurasAcc/venta.html", {"compra":figuras})
   

#Cartas
@login_required
def cartas(request):
    contexto = {"cartas":Cartas.objects.all()}
    return render(request, "Cartas/inicio.html", contexto)
@login_required
def cartasAdd(request):
    if request.method == "POST":
        miForm = CartasForm(request.POST)
        if miForm.is_valid():
            cartas_juego      = miForm.cleaned_data.get("juego")
            cartas_adultos    = miForm.cleaned_data.get("adultos")
            cartas_cantidad   = miForm.cleaned_data.get("cantidad_cartas")
            cartas_precio     = miForm.cleaned_data.get("precio")
            cartas_disponible = miForm.cleaned_data.get("disponibles")
            if cartas_disponible >0:
                cartas_stock = True
            else:
                cartas_stock = False
            carta = Cartas(
                juego       = cartas_juego,
                adultos     = cartas_adultos,
                cantCartas  = cartas_cantidad,
                precio      = cartas_precio,
                disponibles = cartas_disponible,
                en_stock    = cartas_stock
            )
            carta.save()
            contexto = {"cartas":Cartas.objects.all()}
            return render(request, "Cartas/inicio.html", contexto)
    else:
        miForm = CartasForm
    return render(request, "Cartas/formulario.html", {"form":miForm})
@login_required
def cartasUpdate(request, id_cartas):
    cartas = Cartas.objects.get(id=id_cartas)
    if request.method == "POST":
        miForm = CartasForm(request.POST)
        if miForm.is_valid():
            cartas.juego       = miForm.cleaned_data.get("juego")
            cartas.adultos     = miForm.cleaned_data.get("adultos")
            cartas.cantCartas  = miForm.cleaned_data.get("cantidad_cartas")
            cartas.precio      = miForm.cleaned_data.get("precio")
            cartas.disponibles = miForm.cleaned_data.get("disponibles")
            if cartas.disponibles >0:
                cartas.en_stock = True
            else:
                cartas.en_stock = False
            cartas.save()
            contexto = {"cartas":Cartas.objects.all()}
            return render(request, "Cartas/inicio.html", contexto)
    else:
        miForm = CartasForm(initial={
            "juego"           :cartas.juego,
            "adultos"         :cartas.adultos,
            "cantidad_cartas" :cartas.cantCartas,
            "precio"          :cartas.precio,
            "disponibles"     :cartas.disponibles,
        })
    return render(request, "Cartas/formulario.html", {"form":miForm})
@login_required
def cartasDelete(request, id_cartas):
    cartas = Cartas.objects.get(id=id_cartas)
    cartas.delete()
    contexto = {"cartas":Cartas.objects.all()}
    return render(request, "Cartas/inicio.html", contexto)
@login_required
def cartasComprar(request,id_cartas):
    compra     = Cartas.objects.get(id=id_cartas)
    estantería = Cartas.objects.all()
    contexto   = {"compra":compra,"cartas":estantería}
    return render(request, "Cartas/compra.html", contexto)
@login_required
def cartasComprado(request,id_cartas):
    cartas = Cartas.objects.get(id=id_cartas)
    cartas.disponibles -= 1
    if cartas.disponibles == 0:
        cartas.en_stock = False
    cartas.save()
    return render(request, "Cartas/venta.html", {"compra":cartas})

#Juegos de Mesa
@login_required
def juegos_de_mesa(request):
    contexto = {"juMesa":Juegos_de_Mesa.objects.all()}
    return render(request, "JueMesa/inicio.html", contexto)
@login_required
def mesaAdd(request):
    if request.method == "POST":
        miForm = JuegosMesaForm(request.POST)
        if miForm.is_valid():
            mesa_juego      = miForm.cleaned_data.get("juego")
            mesa_adultos    = miForm.cleaned_data.get("adultos")
            mesa_piezas     = miForm.cleaned_data.get("piezas")
            mesa_precio     = miForm.cleaned_data.get("precio")
            mesa_disponible = miForm.cleaned_data.get("disponibles")
            if mesa_disponible >0:
                mesa_stock = True
            else:
                mesa_stock = False
            mesa = Juegos_de_Mesa(
                juego       = mesa_juego,
                adultos     = mesa_adultos,
                piezas      = mesa_piezas,
                precio      = mesa_precio,
                disponibles = mesa_disponible,
                en_stock    = mesa_stock
            )
            mesa.save()
            contexto = {"juMesa":Juegos_de_Mesa.objects.all()}
            return render(request, "JueMesa/inicio.html", contexto)
    else:
        miForm = JuegosMesaForm
    return render(request, "JueMesa/formulario.html", {"form":miForm})
@login_required
def mesaUpdate(request,id_mesa):
    mesa = Juegos_de_Mesa.objects.get(id=id_mesa)
    if request.method == "POST":
        miForm = JuegosMesaForm(request.POST)
        if miForm.is_valid():
            mesa.juego      = miForm.cleaned_data.get("juego")
            mesa.adultos    = miForm.cleaned_data.get("adultos")
            mesa.piezas     = miForm.cleaned_data.get("piezas")
            mesa.precio     = miForm.cleaned_data.get("precio")
            mesa.disponibles = miForm.cleaned_data.get("disponibles")
            if mesa.disponibles >0:
                mesa.en_stock = True
            else:
                mesa.en_stock = False
            mesa.save()
            contexto = {"juMesa":Juegos_de_Mesa.objects.all()}
            return render(request, "JueMesa/inicio.html", contexto)
    else:
        miForm = JuegosMesaForm(initial={
            "juego"      :mesa.juego,
            "adultos"    :mesa.adultos,
            "piezas"     :mesa.piezas,
            "precio"     :mesa.precio,
            "disponibles":mesa.disponibles,
        })
    return render(request, "JueMesa/formulario.html", {"form":miForm})
@login_required
def mesaDelete(request,id_mesa):
    mesa = Juegos_de_Mesa.objects.get(id=id_mesa)
    mesa.delete()
    contexto = {"juMesa":Juegos_de_Mesa.objects.all()}
    return render(request, "JueMesa/inicio.html", contexto)
@login_required
def mesaComprar(request,id_mesa):
    compra     = Juegos_de_Mesa.objects.get(id=id_mesa)
    estantería = Juegos_de_Mesa.objects.all()
    contexto   = {"compra":compra,"juMesa":estantería}
    return render(request, "JueMesa/compra.html", contexto)
@login_required
def mesaComprado(request,id_mesa):
    mesa = Juegos_de_Mesa.objects.get(id=id_mesa)
    mesa.disponibles -= 1
    if mesa.disponibles == 0:
        mesa.en_stock = False
    mesa.save()
    return render(request, "JueMesa/venta.html", {"compra":mesa})

        