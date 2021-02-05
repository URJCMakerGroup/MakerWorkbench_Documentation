# Tutorial: como hacer modelos 3D

## Clase principal de los modelos - **Obj3D**

La clase principal de todos los modelos 3D es *Obj3D* y se encuentra dentro del archivo *NuevaClase.py* disponible en [Mechatronic Documentation](https://github.com/davidmubernal/Mechatronic_Documentation/blob/master/src/func/NuevaClase.py). Esta clase contiene las propiedades y funciones que permiten generar los modelos de forma más sencilla.

<img src="img/Tutorial_modelos_3D/UML_simplificado.svg" style="zoom: 67%;" />

Lo más interesante está en el *\__init__* que nos define las propiedades básicas de nuestro modelo (ejes y nombre) y también inicializa el listado de puntos internos como los diccionarios de volúmenes aditivos o sustractivos.

Para iniciar el *obj3D* se usa la siguiente línea:

```python
# primero importamos
from NuevaClase import Obj3D

# en nuestro objeto que será objeto 3D tenemos que inicializar de la siguiente forma
Obj3D.__init__(self, axis_d, axis_w, axis_h, name)
# aunque también se podría hacer mas claro
Obj3D.__init__(self, axis_d = axis_d, axis_w = axis_w, axis_h = axis_h, name = name)
```

 Dentro de la clase *obj3D* tenemos muchas funciones y todas están documentadas, cualquier duda puedes consultar el código o ir a la [web](https://mechatronic.readthedocs.io/en/test-web/Wiki.html#id5).
Las más interesantes y que se van a usar para crear los modelos son:

* *add_child*: añade un volumen al listado de volúmenes. Para ello se le pasa el volumen, si es aditivo o sustractivo y el nombre.

  ```python
  # siendo volumen_ejemplo una forma (shape) 
  # si child_sum = 1 -> el volumen es aditivo
  add_child(volumen_ejemplo, child_sum=1, "nombre_volumen_aditivo")
  # si child_sum = 0 -> el volumen es sustractivo
  add_child(volumen_ejemplo, child_sum=0, "nombre_volumen_sustractivo")
  
  ```

* *make_parent*: le das un nombre y se encarga de generar el volumen resultante de combinar los volúmenes aditivos y sustractivos.

  ```python
  make_parent("volumen_final")
  ```

  No es necesario almacenarlo en una variable, ya que el resultado lo guarda en el *self*.

* *create_fco*: realiza the fco y asigna las propiedades al modelo para versiones superiores a FreeCAD 0.19

* *append_part*: añade un componente a la lista para crear un conjunto o ensamblaje

* *place_fcos*: sitúa en su posición los distintos modelos de un conjunto o ensamblaje

* *make_group*: crea un grupo para un conjunto o ensamblaje

## Creación de un nuevo modelo 3D

### Definición de la clase

Primero se debe definir una clase del modelo. Esta clase debe heredar de la clase básica *Obj3D* o de una clase que herede de esta (*ShpCylHole por ejemplo*).

```python
placa(Obj3D):
```

### Función \__init__

Esta es la función constructora del modelo, debe tener como parámetros las características que queramos parametrizar

#### Definir parámetros del modelo

Siguiendo con el ejemplo de la placa queremos parametrizar: largo, ancho y alto.

```python
def __init__(self, L_d = 10, L_w = 10, L_h = 2)
```

Además, de cara a usar el *Obj3D* también tenemos que tener como parámetros: axis_d, axis_w, axis_h, name. Por último, suele ser útil definir la posición. Por tanto tenemos que añadir estos parámetros a la función constructora.

```python
def __init__(self, L_d = 10, L_w = 10, L_h = 2, axis_d = VX, axis_w = VY, axis_h = VZ, name = 'placa', pos = V0)
```

Es preferible tener los atributos que queremos parametrizar con unos valores iniciales para evitar errores en caso de que se nos olvide introducir alguno al realizar una llamada al objeto.



> De cara a poder programar mejor el modelo y realizar una composición de volúmenes más sencilla es conveniente realizar un pequeño esquema al inicio de la función con la forma de nuestro objeto y los puntos de interés del mismo.
>
> ```python
>  """
>      d_o[0] d_o[1]  d_o[2]
>      :      :       :
>      :____________:... h_o[2]
>      |            |... h_o[1]
>      |____________|... h_o[0]
>      o
>      ____________ ... w_o[2]
>      |            |
>      |            |... w_o[1]
>      |            |
>      |____________|... w_o[0]
>      o
>  """
> ```

Una vez definidos los parámetros de nuestro modelo, debemos almacenarlos en el objeto *'self'*. Para ello tenemos que crear un atributo dentro del objeto:

```python
self.name = name
self.axis_d = axis_d
self.axis_h = axis_h
self.axis_w = axis_w
self.position = pos
```

#### Instanciar el Obj3D

Después, debemos generar una instancia del *'Obj3D'* para tener todas las funciones de dicha clase.

```python
# Para instanciar la clase llamamos a la clase de la que se hereda desde la función super()
super().__init__(self.axis_d , self.axis_w , self.axis_h, self.name)
# es análogo instanciar la función costructora de la clase que queremos
Obj3D.__init__(self, self.axis_d , self.axis_w , self.axis_h, self.name)
```

Tras instanciar el *Obj3D* ya podemos definir los distintos puntos internos que hemos dibujado en el esquema inicial. Estos puntos suelen ser útiles para realizar el diseño, por ejemplo colocar correctamente un orificio. En el caso del modelo ejemplo que estamos haciendo tenemos 3 puntos de interés por eje.

```python
self.d_o[0] = 0
self.d_o[1] = L_d/2
self.d_o[2] = L_d

self.w_o[0] = 0
self.w_o[1] = L_w/2
self.w_o[2] = L_w

self.h_o[0] = 0
self.h_o[1] = L_h/2
self.h_o[2] = L_h
```

#### Crear formas del objeto

Ya sólo queda generar los *shapes* que formen nuestro modelo. En este caso sólo tenemos que hacer un 

tetraedro.

```python
self.shp = fcfun.shp_boxcen(L_d, L_w, L_h, cx= False, cy=False, cz=False, pos=pos)
```

#### Crear el FreeCAD Object

Para acabar, queda generar el modelo en FreeCAD. Para ello está la función *create_fco* que se ha visto en el apartado anterior.

```python
super().create_fco(self.name)
```

## Creación de modelo 3D con múltiples formas

Vamos a partir del objeto **Placa** que hemos desarrollado antes y el objeto **Hole** que sería análogo a placa. En este caso, ambos objetos no serán **fco** (Objeto FreeCAD)

```python
class placa(Obj3D):

    def __init__(self, L_d = 10, L_w = 10, L_h = 2, axis_d = VX, axis_w = VY, axis_h = VZ, name = 'placa base', pos= V0):
        """
            d_o[0] d_o[1]  d_o[2]
            :      :       :
            :____________:... h_o[2]
            |            |... h_o[1]
            |____________|... h_o[0]
           o
             ____________ ... w_o[2]
            |            |
            |            |... w_o[1]
            |            |
            |____________|... w_o[0]
           o
        """
        self.name = name
        self.axis_d = axis_d
        self.axis_h = axis_h
        self.axis_w = axis_w

        super().__init__(self.axis_d , self.axis_w , self.axis_h, self.name)

        self.d_o[0] = 0
        self.d_o[1] = L_d/2
        self.d_o[2] = L_d
        
        self.w_o[0] = 0
        self.w_o[1] = L_w/2
        self.w_o[2] = L_w
        
        self.h_o[0] = 0
        self.h_o[1] = L_h/2
        self.h_o[2] = L_h
        
         self.shp = fcfun.shp_boxcen(L_d, L_w, L_h, cx= False, cy=False, cz=False, pos=self.position)
        
        
class hole(Obj3D):
    def __init__(self, r = None, h = None, axis_d = VX, axis_w = VY, axis_h = VZ, pos = V0, name = None, pos = V0):
        """
		   d_o[0]
            : d_o[1]
            : : d_o[2]
            : : :
            :___:... h_o[2]
            |   |
            |   |... h_o[1]
            |   |
            |___|... h_o[0]
           o
              _... w_o[2]
             / \... w_o[1]
             \_/... w_o[0]
           o
        """
        self.name = name
        self.axis_d = axis_d
        self.axis_h = axis_h
        self.axis_w = axis_w
        self.position = pos

        super().__init__(self.axis_d , self.axis_w , self.axis_h, self.name)

        self.d_o[0] = 0
        self.d_o[1] = r/2
        self.d_o[2] = r
        
        self.w_o[0] = 0
        self.w_o[1] = r/2
        self.w_o[2] = r
        
        self.h_o[0] = 0
        self.h_o[1] = h/2
        self.h_o[2] = h
        
        self.shp = fcfun.shp_cyl(r, h, self.axis_h, self.position)
        
```



En base a estos dos objetos vamos a crear una placa perforada en el centro. Vamos a crear el modelo *placa_perforada* que es un *Obj3D*.



```python
class placa_perforada(Obj3D):
    """
        d_o[0] d_o[1]  d_o[2]
        :      :       :
        :____________:... h_o[2]
        |     : :    |... h_o[1]
        |_____:_:____|... h_o[0]
        o
         ____________ ... w_o[2]
        |            |
        |      O     |... w_o[1]
        |            |
        |____________|... w_o[0]
        o
    """
    def __init__(self, d, w, h, r, name = 'placa perforada'):
        self.axis_d = VX
        self.axis_w = VY
        self.axis_h = VZ
        self.name = name
        
        super().__init__(self.axis_d , self.axis_w , self.axis_h , self.name)
        
        self.d_o[0] = 0
        self.d_o[1] = d/2
        self.d_o[2] = d
        
        self.w_o[0] = 0
        self.w_o[1] = w/2
        self.w_o[2] = w
        
        self.h_o[0] = 0
        self.h_o[1] = h/2
        self.h_o[2] = h
```

Hasta aquí no hemos hecho nada nuevo. Hemos creado la clase, instanciado el Obj3D y definido sus puntos internos. Ahora vamos a crear una instancia de *placa* y de *hole*. 

```python
_placa = placa(d, w, h, self.axis_d, self.axis_w, self.axis_h, name = 'plate')
hole place = FreeCAD.Vector(self.d_o[2],self.w_o[2],self.h_o[0])
_hole = hole(r, h+0.1, axis_d = VX, axis_w = VY, axis_h = VZ, pos = hole_place)
```

### Añadir formas

Una vez creadas la formas tenemos que añadirlas al *Obj3D* y determinar si añaden o substraen volumen. Para ello vamos a usar la función *add_child* .

```python
super().add_child(_placa, 1, 'plate')
super().add_child(_hole, 0, 'hole')
```

### Crear forma

Por último, queda sumar las formas y crear el *fco*.

```python
super().make_parent(self.name)
super().create_fco(self.name)
```

El objeto *placa_perforada* quedaría:

```python
class placa_perforada(Obj3D):
    """
        d_o[0] d_o[1]  d_o[2]
        :      :       :
        :____________:... h_o[2]
        |     : :    |... h_o[1]
        |_____:_:____|... h_o[0]
        o
         ____________ ... w_o[2]
        |            |
        |      O     |... w_o[1]
        |            |
        |____________|... w_o[0]
        o
    """
    def __init__(self, d, w, h, r, name = 'placa perforada', pos = V0):
        self.axis_d = VX
        self.axis_w = VY
        self.axis_h = VZ
        self.name = name
        self.position = pos
        
        super().__init__(self.axis_d , self.axis_w , self.axis_h , self.name)
        
        self.d_o[0] = 0
        self.d_o[1] = d/2
        self.d_o[2] = d
        
        self.w_o[0] = 0
        self.w_o[1] = w/2
        self.w_o[2] = w
        
        self.h_o[0] = 0
        self.h_o[1] = h/2
        self.h_o[2] = h
        
        _placa = placa(d, w, h, self.axis_d, self.axis_w, self.axis_h, name = 'plate', self.position)
        
        hole place = FreeCAD.Vector(self.d_o[2],self.w_o[2],self.h_o[0])
        _hole = hole(r, h+0.1, axis_d = VX, axis_w = VY, axis_h = VZ, pos = hole_place)
        super().add_child(_placa, 1, 'plate')
        super().add_child(_hole, 0, 'hole')
        
        super().make_parent(self.name)
        super().create_fco(self.name)
        self.fco.Placement.Base = FreeCAD.Vector(0,0,0) # iniciamos el posicionamiento en el origen
        self.fco.Placement.Base = self.position # movemos a la posición que queremos
```

## Creación de conjuntos o ensamblajes

Un conjunto o ensamblaje está compuesto por varios modelos u objetos de FreeCAD. En esta caso vamos a tener una clase que deriva de *Obj3D* que va a instanciar a otros objetos **fco**.

Como ejemplo para ver el proceso vamos a crear una mesa con 4 patas. Para ahorrar tiempo en el ejemplo vamos a reusar la clase *placa* que hemos visto en el apartado ["Creación de un nuevo modelo 3D"](#Creación de un nuevo modelo 3D):

```python
class placa(Obj3D):

    def __init__(self, L_d = 10, L_w = 10, L_h = 2, axis_d = VX, axis_w = VY, axis_h = VZ, name = 'placa base', pos = V0):
        """
            d_o[0] d_o[1]  d_o[2]
            :      :       :
            :____________:... h_o[2]
            |            |... h_o[1]
            |____________|... h_o[0]
           o
             ____________ ... w_o[2]
            |            |
            |            |... w_o[1]
            |            |
            |____________|... w_o[0]
           o
        """
        self.name = name
        self.axis_d = axis_d
        self.axis_h = axis_h
        self.axis_w = axis_w
        self.position = pos

        super().__init__(self.axis_d , self.axis_w , self.axis_h, self.name)

        self.d_o[0] = 0
        self.d_o[1] = L_d/2
        self.d_o[2] = L_d
        
        self.w_o[0] = 0
        self.w_o[1] = L_w/2
        self.w_o[2] = L_w
        
        self.h_o[0] = 0
        self.h_o[1] = L_h/2
        self.h_o[2] = L_h
        
        self.shp = fcfun.shp_boxcen(L_d, L_w, L_h, cx= False, cy=False, cz=False, pos=self.position)
        super().create_fco(self.name)
        self.fco.Placement.Base = FreeCAD.Vector(0,0,0)
        self.fco.Placement.Base = self.position
```

Empezamos definiendo e inicializando el *Obj3D*. Vamos a hacer uso de la función *get_pos_dwh* que obtiene la posición relativa del punto interno seleccionado para poder fijar la posición de los distintos componentes del conjunto.



```python
class table(Obj3D):
    def __init__(self, d=1000, w=600, h_table=100, h=800, w_leg=60, axis_d=VX, axis_w=VY, axis_h=VZ = , name='table', pos = V0):
        """
            d_o[0]       d_o[4]
            :      d_o[2]:
            :d_o[1]:  d_o[3]
            :_:____:___:_:... h_o[2]
            |____________|... h_o[1]
            | |        | |
            |_|        |_|... h_o[0]
           o
             ____________ ... w_o[4]
            |o          o|... w_o[3]
            |            |... w_o[2]
            |            |... w_o[1]
            |o__________o|... w_o[0]
           o
        """
        self.name = name
        self.axis_d = axis_d
        self.axis_h = axis_h
        self.axis_w = axis_w
        
        super().__init__(self.axis_d , self.axis_w , self.axis_h, self.name)
        
        self.d_o[0] = 0
        self.d_o[1] = w_leg
        self.d_o[2] = d/2
        self.d_o[3] = d-w_leg
        self.d_o[4] = d
        
        self.w_o[0] = 0
        self.w_o[1] = w_leg
        self.w_o[2] = w/2
        self.w_o[3] = w-w_leg
        self.w_o[4] = w
        
        self.h_o[0] = 0
        self.h_o[1] = h-h_table
        self.h_o[2] = h 
        
        # creamos la tabla de la mesa
        table = placa(L_d=d, L_w=w, L_h=h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'table', pos=self.get_pos_dwh(0,0,1))
        # añadimos la tabla al conjunto
        self.append_part(table)
        
        # creamos las patas de la mesa
        leg_1 = placa(L_d=w_leg, L_w=w_leg, L_h=h-h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'leg_1', pos=self.get_pos_dwh(0,0,0))
        # añadimos al conjunto
        self.append_part(leg_1)
        
        leg_2 = placa(L_d=w_leg, L_w=w_leg, L_h=h-h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'leg_2', pos=self.get_pos_dwh(0,3,0))
        # añadimos al conjunto
        self.append_part(leg_2)
        
        leg_3 = placa(L_d=w_leg, L_w=w_leg, L_h=h-h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'leg_3', pos=self.get_pos_dwh(3,0,0))
        # añadimos al conjunto
        self.append_part(leg_3)
        
        leg_4 = placa(L_d=w_leg, L_w=w_leg, L_h=h-h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'leg_4', pos=self.get_pos_dwh(3,3,0))
        # añadimos al conjunto
        self.append_part(leg_4)
        
        # creamos el grupo con las partes que hemos añadido al conjunto
        super().make_group()
        
        # colocamos el grupo en la posición deseada
        self.fco.Placement.Base = FreeCAD.Vector(0,0,0)
        self.fco.Placement.Base = self.position
        
        
        
```

