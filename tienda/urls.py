from django.urls import *
from .views import *


urlpatterns = [
    
    #Principal
    path("",                       home,      name="home"     ),
    path("about_us/",              acerca_de, name="acerca_de"),
    path("buscar/",                buscar,    name="buscar"   ),
    path("resulados_de_busqueda/", encontrar, name="encontrar"),

    #Usuario
    path("login/",    iniciar_sesion,    name="login"        ),
    path("register/", registrar_usuario, name="register"     ),
    path("editUser/", editar_usuario,    name="editUser"     ),
    path("avatar/",   agregar_avatar,    name="agragarAvatar"),
    path("logout/",   cerrar_sesion,     name="logout"       ),

    #Peluches
    path("peluches/",                     peluches,        name="peluches"    ),
    path("peluches/Add/",                 peluchesAdd,     name="peluchesAdd" ),
    path("peluches/update/<id_peluche>",  peluchesUpdate,  name="peluchesUpdt"),
    path("peluches/delete/<id_peluche>",  peluchesDelete,  name="peluchesDel" ),
    path("peluches/compra/<id_peluche>",  peluchesComprar, name="peluchesSell"),
    path("peluches/purchase/<id_peluche>",peluchesComprado,name="peluchesSold"),

    #Figuras de acción
    path("figuras/",                     figuras_de_accion, name="figurasAccion"),
    path("figuras/Add/",                 figurasAdd,        name="figurasAdd"   ),
    path("figuras/update/<id_figura>",   figurasUpdate,     name="figurasUpdt"  ),
    path("figuras/delete/<id_figura>",   figurasDelete,     name="figurasDel"   ),
    path("figuras/compra/<id_figura>",   figurasComprar,    name="figurasSell"  ),
    path("figuras/purchase/<id_figura>", figurasComprado,   name="figurasSold"  ),

    #Cartas
    path("cartas/",                    cartas,          name="cartas"    ),
    path("cartas/Add/",                cartasAdd,       name="cartasAdd" ),
    path("cartas/update/<id_cartas>",  cartasUpdate,    name="cartasUpdt"),
    path("cartas/delete/<id_cartas>",  cartasDelete,    name="cartasDel" ),
    path("cartas/compra/<id_cartas>",  cartasComprar,   name="cartasSell"),
    path("cartas/purchase/<id_cartas>",cartasComprado,  name="cartasSold"),
    

    #Juegos de mesa
    path("mesa/",                     juegos_de_mesa,name="mesa"    ), 
    path("mesa/Add/",                 mesaAdd,       name="mesaAdd" ),
    path("mesa/update/<id_mesa>",     mesaUpdate,    name="mesaUpdt"),
    path("mesa/delete/<id_mesa>",     mesaDelete,    name="mesaDel" ),
    path("mesa/compra/<id_mesa>",     mesaComprar,   name="mesaSell"),
    path("mesa/purchase/<id_mesa>",   mesaComprado,  name="mesaSold"),

]