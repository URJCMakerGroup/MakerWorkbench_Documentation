# Tutorial: how to make 3D models

## Main class of the models - **Obj3D**

The main class of all 3D models is *Obj3D* and is located inside the *NewClass.py* file available in [Mechatronic Documentation](https://github.com/davidmubernal/Mechatronic_Documentation/blob/master/src/func/NuevaClase.py). This class contains the properties and functions that allow to generate the models more easily.

![](/parts/img/UML_simplificado.jpg)

The most interesting function in *Obj3D* is the function *\__init__* that defines the basic properties of our model (axes and name). Also, *\__init__* initializes the list of internal points as the dictionaries as additive or subtractive volumes.

To start the *obj3D* it is used the following line:

```python
# import
from NuevaClase import Obj3D

# in our object that will be a 3D object we have to initialize as follows
Obj3D.__init__(self, axis_d, axis_w, axis_h, name)
# although it could also be made clearer
Obj3D.__init__(self, axis_d = axis_d, axis_w = axis_w, axis_h = axis_h, name = name)
```



Inside the *obj3D* class we have many functions and all are documented, any doubt you can check the code or go to the [web](https://mechatronic.readthedocs.io/en/test-web/Wiki.html#id5).
The most interesting and that are going to be used to create the models are

* *add_child*: adds a volume to the list of volumes. To do this you pass the volume, if it is additive or subtractive and the name.

  ```python
  # being volume_example a shape 
  # if child_sum = 1 -> volume is additive
  add_child(volume_example, child_sum=1, "additive_volume_name")
  # if child_sum = 0 -> volume is subtractive
  add_child(example_volume, child_sum=0, "subtractive_volume_name")
  ```

* *make_parent*: you give it a name and generate the resulting volume by combining the additive and subtractive volumes.

  ```python
  make_parent("final_volume")
  ```
  
  ​	 It is not necessary to store it in a variable, since the result is stored in *self*.

* *create_fco*: perform the fco and assign the properties to the model for versions higher than FreeCAD 0.19

* *append_part*: adds a component to the list to create an assembly

* *place_fcos*: places in its position the different models of a set or assembly

* *make_group*: create a group for an assembly

## Creation of a new 3D model

### Class definition

First you must define a class of the model. This class must inherit from the basic class *Obj3D* or a class that inherits from it (*ShpCylHole for example*).

```python
plate(Obj3D):
```

### Function \__init__

This is the construction function of the model, it must have as parameters the characteristics that we want to parameterize

#### Define model parameters

Following the example of the plate we want to parameterize: length, width and height.

```python
def __init__(self, L_d = 10, L_w = 10, L_h = 2)
```

In addition, to use the *Obj3D* we also have to have as parameters: axis_d, axis_w, axis_h, name. Finally, it is usually useful to define the position. Therefore we have to add these parameters to the construction function.

```python
def __init__(self, L_d = 10, L_w = 10, L_h = 2, axis_d = VX, axis_w = VY, axis_h = VZ, name = 'placa', pos = V0)
```

It is preferable to have the attributes that we want to parameterize with some initial values to avoid errors in case we forgot to enter one when calling the object.



> In order to be able to program the model better and to make a composition of volumes simpler. It is convenient to make a small scheme at the beginning of the function with the shape of our object and the points of interest of the same one.
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

When the parameters of our model are defined, we must store them in the *'self'* object. For it we have to create an attribute inside the object:

```python
self.name = name
self.axis_d = axis_d
self.axis_h = axis_h
self.axis_w = axis_w
self.position = pos
```

#### Instantiate the Obj3D

Then, we must generate an instance of the *'Obj3D'* to have all the functions of that class.

```python
# To instantiate the class we call the class from which it is inherited from the super() function
super().__init__(self.axis_d , self.axis_w , self.axis_h, self.name)
# it is analogous to instantiate the building function of the class we want
Obj3D.__init__(self, self.axis_d , self.axis_w , self.axis_h, self.name)
```

After instantiating the *Obj3D* we can already define the different internal points that we have drawn in the initial scheme. These points are usually useful to make the design, for example to place a hole correctly. In the case of the example model we are doing we have 3 points of interest per axis.

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

#### Create object shapes

All that remains is to generate the *shapes* that form our model. In this case we only have to make a 

tetrahedron.

```python
self.shp = fcfun.shp_boxcen(L_d, L_w, L_h, cx=False, cy=False, cz=False, pos=pos)
```

#### Create the FreeCAD Object

Finally, it remains to generate the model in FreeCAD. For this there is the function *create_fco* that has been seen in the previous section.

```python
super().create_fco(self.name)
```

## Creation of 3D model with multiple shapes

Let's start from the object **Plate** that we have developed before and the object **Hole** that would be analogous to a plate. In this case, both objects will not be **fco** (FreeCAD object)

```python
class plate(Obj3D):

    def __init__(self, L_d = 10, L_w = 10, L_h = 2, axis_d = VX, axis_w = VY, axis_h = VZ, name = 'base plate', pos= V0):
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



Based on these two objects we will create a perforated plate in the center. We are going to create the *perforated_plate* model that is an *Obj3D*.



```python
class perforated_plate(Obj3D):
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
    def __init__(self, d, w, h, r, name = 'perforated plate')
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

So far we have done nothing new. We have created the class, instantiated the Obj3D and defined its internal points. Now we are going to create an instance of *plate* and *hole*. 

```python
_placa = placa(d, w, h, self.axis_d, self.axis_w, self.axis_h, name = 'plate')
hole place = FreeCAD.Vector(self.d_o[2],self.w_o[2],self.h_o[0])
_hole = hole(r, h+0.1, axis_d = VX, axis_w = VY, axis_h = VZ, pos = hole_place)
```

### Add forms

Once the forms are created we have to add them to the *Obj3D* and determine if they add or subtract volume. To do this we will use the *add_child* function.

```python
super().add_child(_placa, 1, 'plate')
super().add_child(_hole, 0, 'hole')
```

### Create form

Finally, it remains to add up the forms and create the *fco*.

```python
super().make_parent(self.name)
super().create_fco(self.name)
```

The object *perforated_plate* would remain:

```python
class perforated_plate(Obj3D):
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
    def __init__(self, d, w, h, r, name = 'perforated_plate', pos = V0):
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
        
        _plate = plate(d, w, h, self.axis_d, self.axis_w, self.axis_h, name = 'plate', self.position)
        
        hole_place = FreeCAD.Vector(self.d_o[2],self.w_o[2],self.h_o[0])
        _hole = hole(r, h+0.1, axis_d = VX, axis_w = VY, axis_h = VZ, pos = hole_place)
        super().add_child(_placa, 1, 'plate')
        super().add_child(_hole, 0, 'hole')
        
        super().make_parent(self.name)
        super().create_fco(self.name)
        self.fco.Placement.Base = FreeCAD.Vector(0,0,0) # we start the positioning at the origin
        self.fco.Placement.Base = self.position # we move to the position we want
```

## Creation of sets or assemblies

An assembly is composed of several FreeCAD models or objects. In this case we are going to have a class that derives from *Obj3D* that is going to instantiate other objects **fco**.

As an example to see the process we are going to create a table with 4 legs. To save time in the example we are going to reuse the *plate* class that we have seen in the section ["Creating a new 3D model"](#Creating a new 3D model):

```python
class plate(Obj3D):

    def __init__(self, L_d = 10, L_w = 10, L_h = 2, axis_d = VX, axis_w = VY, axis_h = VZ, name = 'base plate', pos = V0):
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

We start by defining and initializing the *Obj3D*. We are going to use the function *get_pos_dwh* that obtains the relative position of the selected internal point to be able to set the position of the different components of the assembly.





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
        
        # we created the table
        table = placa(L_d=d, L_w=w, L_h=h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'table', pos=self.get_pos_dwh(0,0,1))
        # we add the table to the set
        self.append_part(table)
        
        # we create the table legs
        leg_1 = placa(L_d=w_leg, L_w=w_leg, L_h=h-h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'leg_1', pos=self.get_pos_dwh(0,0,0))
        # we add to the set
        self.append_part(leg_1)
        
        leg_2 = placa(L_d=w_leg, L_w=w_leg, L_h=h-h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'leg_2', pos=self.get_pos_dwh(0,3,0))
        # we add to the set
        self.append_part(leg_2)
        
        leg_3 = placa(L_d=w_leg, L_w=w_leg, L_h=h-h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'leg_3', pos=self.get_pos_dwh(3,0,0))
        # we add to the set
        self.append_part(leg_3)
        
        leg_4 = placa(L_d=w_leg, L_w=w_leg, L_h=h-h_table, axis_d=self.axis_d, axis_w=self.axis_w, axis_h=self.axis_h, name = 'leg_4', pos=self.get_pos_dwh(3,3,0))
        # we add to the set
        self.append_part(leg_4)
        
        # we created the group with the parts that we have added to the set
        super().make_group()
        
        # we place the group in the desired position
        self.fco.Placement.Base = FreeCAD.Vector(0,0,0)
        self.fco.Placement.Base = self.position
        
        
        
```

