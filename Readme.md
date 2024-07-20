# JUGUETERÍA TOYLAND

Esta pagina va de una tienda de juguetes que se dedica a, valga la redundancia, a vender juguetes, simplemente. 

***Copiright Ramiro Joel Zarza*** (referencia)

## Admin
**Usuario**: RamiZarza

**Clave**: rzpro811 

## Modelos

hay 5 modelos de productos:

- Peluches
- Figuras de Acción
- Cartas
- Juegos de Mesa

Hice carpetas de templates para cada uno por separado así me ahorraba tiempo y podía hacer copy paste tranquilo y sin problemas. Tambien les asigne palabras clave para las funciones

Cada clase tiene un **"inicio.html"**, donde se pone la lista de productos que estan disponibles para comprar. Por otro lado tambien tienen un **"formulatio.html"** en donde, valga la redundancia, se encuentran los formularios. Ademas incluyen un html de **"Compra"** y **"Venta"** para poder comprar los productos.

##

* ### Peluches

Todos de chiquitos hemos tenído peluches que queremos mucho y hasta nos vamos a dormir con ellos, por eso si vamos a hacer una juguetería no pueden faltar los peluches

### Atributos
- **Producto**: Nombre del peluche
- **Foto**: Imagen del peluche
- **Precio**: Cuanto cuesta el peluche en cuestion
- **En_Stock**: Valor booleano que indica si hay stock disponible, si es True, aun quedan peluches para vender, si es False, no
- **Disponibles**: Cuanto Stock hay disponble de peluches

**Palabra Clave**: peluche
##

 * ### Figuras de Acción

Ya sea que te gusten los superheroes o el anime, o lo que fuera, te gustaría tener una figura de acción para poder tenerla en tu cuarto posando epicamente o para que tu sobrino juegue con ella esperan a que rompa algo que te costo medio riñón pagarlo   * no supera su trauma *

### Atributos
- **Figura**: Nombre del personaje
- **Origen**: De que pelicula, serie o juego viene tal personaje
- **Fabricante**: La marca que fabrico dicha figura de acción (no se porque solo lo hice para esta clase)
- **Foto**: Imagen de la figura
- **Precio**: Cuanto cuesta la figura en cuestion
- **En_Stock**: Valor booleano que indica si hay stock disponible, si es True, aun quedan figuras para vender, si es False, no
- **Disponibles**: Cuanto Stock hay disponble de figuras

**Palabra Clave**: figura

##
 * ### Cartas

Has jugado al Uno, al Poker, a la casita robada, las cartas son una parte fundamental de la diversión, por lo que no podíamos dejarlas fuera de esta pagina

### Atributos
- **Juego**: Nombre del juego de cartas
- **Adultos**: Si el juego es para +18, entonces esto será True. Si algo me enseño la pelicula "la Fiesta de las salchichas" es que es necesario especificar cuando algo no es apto para niños
- **cantCartas**: La cantidad de cartas que hay en los masos de cartas
- **Foto**: Imagen del juego de cartas
- **Precio**: Cuanto cuesta el juego de cartas
- **En_Stock**: si hay stock del juego
- **Disponibles**: Cuantos juegos hay disponibles

**Palabra clave**: cartas

##
* ### Juegos de Mesa

Juegue en familia, con amigos, como sea. Juegue con un tablero y varias fichas o lo que sea para divertirse entre todos si es que no tienen television, celulares, wifi y se mueren del aburrimiento

### Atributos
- **Juego**: Nombre del juego de mesa
- **Adultos**: Si es apto para niños o no
- **Piezas**: La cantidad de piezas que hay en las cajas
- **Foto**: 
- **Precio**: 
- **En_Stock**:
- **Disponibles**: ¿Es necesario que explique estos cuatro? literalmente estan en los otros modelos y funcionan exactamente igual

**Palabra clave**: mesa
