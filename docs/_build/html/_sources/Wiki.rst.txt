.. Documento con toda la información sobre las piezas y las funciones

Wiki
====

.. note:: 
    This is a basic view of the Wiki

Biblioteca de modelos
----------------------

Soporte de eje
^^^^^^^^^^^^^^
    * Tamaño
    * Perfil bajo: sólo para tamaño 8

    .. image:: ../parts/img/sk08.png
        :height: 148px
        :alt: Soporte de eje de tamaño 8

    .. image:: ../parts/img/sk08_pillow.png
        :height: 148px
        :alt: Soporte de eje de tamaño 8 de perfil bajo

.. toggle-header::
    :header: Details

    .. currentmodule:: comps
    .. autosummary::
        Sk_dir    

Soporte polea loca
^^^^^^^^^^^^^^^^^^

    * Tamaño del perfil sobre el que se monta
    * Métrica de los tornillos
    * Altura
    * Posición del sensor de final de carrera
    * Altura del sensor de final de carrera

    ::

        Pendiente de modificar el modelo para mayor eficiencia

.. toggle-header::
    :header: Details

    .. currentmodule:: parts
    .. autosummary::
        IdlePulleyHolder
    
Soporte final de carrera
^^^^^^^^^^^^^^^^^^^^^^^^

    * Tipo
    * Distancia del carril

    .. image:: ../parts/img/endstop_holder_30.png
        :height: 148px
        :alt: 

    .. image:: ../parts/img/d3v_endstop_holder_r25_m4.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: parts
    .. autosummary::
        SimpleEndstopHolder

Soporte final
^^^^^^^^^^^^^

    * Ancho
    * Espesor
    * Métrica tornillo
    * Tamaño perfil
    * Refuerzo
      

    .. image:: ../parts/img/hall_stop_holder_21_10.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: parts
    .. autosummary::
        hallestop_holder

Bracket para perfiles
^^^^^^^^^^^^^^^^^^^^^

    * Tipo: 3 opciones distintas
    * Tamaño primer perfil
    * Tamaño segundo perfil
    * Espesor
    * Métrica tornillo primer perfil
    * Métrica tornillo segundo perfil
    * Número de tornillos
    * Distancia entre tornillos
    * Seleccion agujero
    * Refuerzo: sólo para el primer tipo de bracket
    * Flap: sólo para el segundo tipo de bracket
    * Distancia entre perfiles: sólo para el tercer tipo de bracket
 
    .. image:: ../parts/img/bracket_30x30_m6.png
        :height: 148px
        :alt: 

    .. image:: ../parts/img/bracket_30x30_m6_rail15.png
        :height: 148px
        :alt: 

    .. image:: ../parts/img/bracket_30x30_m6_rail20_6thick.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: parts
    .. autosummary::
        AluProfBracketPerp
        AluProfBracketPerpFlap
        AluProfBracketPerpTwin

Soporte motor
^^^^^^^^^^^^^

    * Tamaño del soporte
    * Altura del soporte
    * Espesor de las paredes del soporte

    .. image:: ../parts/img/nema17_holder_rail25_8.png
        :height: 148px
        :alt: 

    .. image:: ../parts/img/nema17_holder_rail35_8.FCStd.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: parts
    .. autosummary::
        NemaMotorHolder

Carcasa del rodamiento lineal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    * Tipo

    .. image:: ../parts/img/thinlinbearhouse1rail_lm8.png
        :height: 148px
        :alt: 
    .. image:: ../parts/img/thinlinbearhouse1rail_lm8_bot.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: parts
    .. autosummary::
        ThinLinBearHouse1rail
        ThinLinBearHouse
        LinBearHouse
        ThinLinBearHouseAsim

Soporte del filtro
^^^^^^^^^^^^^^^^^^

    * Largo
    * Ancho

    .. image:: ../parts/img/filter_holder.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: filter_holder_clss
    .. autosummary::
        PartFilterHolder

Tensionador de la polea
^^^^^^^^^^^^^^^^^^^^^^^

    * Altura de polea
    * Ancho de base
    * Espesor
    * Métrica del tornillo

    .. image:: ../parts/img/tensioner.png
        :height: 148px
        :alt:   

.. toggle-header::
    :header: Details

    .. currentmodule:: tensioner_clss
    .. autosummary::
        TensionerSet

Abrazadera de polea
^^^^^^^^^^^^^^^^^^^

    * Tipo
    * Largo
    * Ancho
    * Métrica del tornillo
 
    .. image:: ../parts/img/Belt_clamp_simple.png
        :height: 148px
        :alt: 

    .. image:: ../parts/img/Belt_clamp_double.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: beltcl 
    .. autosummary::
        BeltClamp
        DoubleBeltClamp

Perfil de aluminio
^^^^^^^^^^^^^^^^^^
    * Sección
    * Longitud
        
    .. image:: ../parts/img/Profiles.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule::comps
    .. autosummary::
        PartAluProf
    
Tornillos, Tuercas y Arandelas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    * Tipo
    * Métrica
    * Longitud del tornillo

    .. image:: ../parts/img/Bolts.png
        :height: 148px
        :alt: 

    .. image:: ../parts/img/Nuts.png
        :height: 148px
        :alt: 

    .. image:: ../parts/img/Washers.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: fc_clss 
    .. autosummary::
        Din934Nut
        Din125Washer
        Din9021Washer
        Din912Bolt

.. Biblioteca de sistemas
   ----------------------

.. _biblioteca de funciones:

Biblioteca de funciones
-----------------------

fcfun
^^^^^

.. currentmodule:: fcfun
.. autosummary::
    NutHole
    add2CylsHole
    add3CylsHole
    addBolt
    addBoltNut_hole
    addBox
    addBox_cen
    addCyl
    addCylHole
    addCylHolePos
    addCylPos
    addCyl_pos
    add_fcobj
    aluprof_vec
    calc_desp_ncen
    calc_rot
    calc_rot_z
    edgeonaxis
    equ
    fc_calc_desp_ncen
    fc_calc_rot
    fc_isonbase
    fc_isparal
    fc_isparal_nrm
    fc_isperp
    fillet_len
    filletchamfer
    fuseshplist
    get_bolt_bearing_sep
    get_bolt_end_sep
    get_fc_perpend1
    get_fclist_4perp2_fcvec
    get_fclist_4perp2_vecname
    get_fclist_4perp_fcvec
    get_fclist_4perp_vecname
    get_fcvectup
    get_nameofbasevec
    get_positive_vecname
    get_rot
    get_tangent_2circles
    get_tangent_circle_pt
    get_vecname_perpend1
    get_vecname_perpend2
    getfcvecofname
    getvecofname
    regpolygon_dir_vecl
    regpolygon_vecl
    rotateview
    shpRndRectWire
    shp_2stadium_dir
    shp_aluwire_dir
    shp_belt_dir
    shp_belt_wire_dir
    shp_bolt
    shp_bolt_dir
    shp_boltnut_dir_hole
    shp_box_dir
    shp_box_dir_xtr
    shp_box_rot
    shp_boxcen
    shp_boxcenchmf
    shp_boxcenfill
    shp_boxcenxtr
    shp_boxdir_fillchmfplane
    shp_cableturn
    shp_cir_fillchmf
    shp_cyl
    shp_cyl_gen
    shp_cylcenxtr
    shp_cylfilletchamfer
    shp_cylhole
    shp_cylhole_arc
    shp_cylhole_bolthole
    shp_cylhole_gen
    shp_cylholedir
    shp_extrud_face
    shp_extrud_face_rot
    shp_face_lgrail
    shp_face_rail
    shp_filletchamfer    
    shp_filletchamfer_dir
    shp_filletchamfer_dirpt
    shp_filletchamfer_dirpts
    shp_filletchamfer_dirs
    shp_hollowbelt_dir
    shp_nuthole
    shp_regpolygon_dir_face
    shp_regpolygon_face
    shp_regprism
    shp_regprism_dirxtr
    shp_regprism_xtr
    shp_rndrect_face
    shp_stadium_dir
    shp_stadium_face
    shp_stadium_wire
    shp_stadium_wire_dir
    vecname_paral
    wire_beltclamp
    wire_cableturn
    wire_lgrail
    wire_sim_xy


    




Biblioteca de clases
-----------------------

Nueva Clase
^^^^^^^^^^^^
.. currentmodule:: NuevaClase
.. autosummary:: 
    Obj3D
    

.. _UML:

UML
---
.. Imagen dispuesta a la derecha del texto que se encuentra debajo

.. figure:: ../parts/img/UML_simplificado.jpg
    :width: 296 px
    :align: right

El UML (Unified Modeling Language) es el diagrama base para el desarrollo de software.
Es una descripción visual de las relaciones entre las clases de objetos.
Sería comparable al plano de un edificio. Algunos programadores consideran que hacer UML es 
un gasto de tiempo, pero es muy útil cuando se debe trabajar en equipo, ya que todos parten 
de un mismo diseño.

La clase principal será "*Obj3D*" la cual contendrá la información básica del modelo:

* Ejes interno:

    * axis_d
    * axis_w
    * axis_h

* Diccionario de hijos:

    * dict_child
    * dict_child_sum
    * dict_child_res

El resto de clases que generan los distintos modelos 3D se referenciarán a la clase *Obj3D*

|

.. blank line - image bigger than text

Detalle de modelos
------------------

comps
^^^^^

.. automodule:: comps
    :members: Sk_dir, PartAluProf

parts
^^^^^

.. automodule:: parts
    :members: IdlePulleyHolder,
              SimpleEndstopHolder,
              AluProfBracketPerp,
              AluProfBracketPerpFlap,
              AluProfBracketPerpTwin,
              hallestop_holder,
              NemaMotorHolder,
              ThinLinBearHouse1rail,
              ThinLinBearHouse,
              LinBearHouse,
              ThinLinBearHouseAsim

Detalle de funciones
--------------------

fcfun
^^^^^

.. automodule:: fcfun
    :members:

Detalles de clases
------------------

Nueva Clase
^^^^^^^^^^^^
.. automodule:: NuevaClase
    :members:
    
.. :special-members: __init__
