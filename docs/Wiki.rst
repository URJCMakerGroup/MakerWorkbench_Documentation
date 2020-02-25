.. Documento con toda la información sobre las piezas y las funciones

Wiki
====

.. note:: 
    This is a basic view of the Wiki

3D Model library
----------------

Shaft Holder
^^^^^^^^^^^^^
    * Size
    * Low profile: Only in size 8

    .. image:: ../parts/img/sk08.png
        :height: 148px
        :alt: Shaft Support Size 8

    .. image:: ../parts/img/sk08_pillow.png
        :height: 148px
        :alt: Shaft Support Size 8 Low Profile

.. toggle-header::
    :header: Details

    .. currentmodule:: comps
    .. autosummary::
        Sk_dir    

Idler Holder
^^^^^^^^^^^^^

    * Size of the profile on which it is mounted
    * Bolt metrics
    * Height
    * Position of the limit switch sensor
    * Height of the limit switch sensor

    ::

        The model will be modified for greater efficiency

.. toggle-header::
    :header: Details

    .. currentmodule:: parts
    .. autosummary::
        IdlePulleyHolder
    
Limit Switches Holder
^^^^^^^^^^^^^^^^^^^^^

    * Type
    * Rail distance

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

Hall stop
^^^^^^^^^^^

    * Width
    * Thikness
    * Metric nut
    * Profile size
    * Reinforce
      

    .. image:: ../parts/img/hall_stop_holder_21_10.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: parts
    .. autosummary::
        hallestop_holder

Bracket 
^^^^^^^

    * Type: 3 options
    * Size first profile
    * Size second profile
    * Thickness
    * Metric nut first profile
    * Metric nut second profile
    * Number of nuts
    * Distance betwen nuts
    * Type of hole
    * Reinforcement: first type only
    * Flap: second type only
    * Distance between profiles: third type only
 
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

Motor holder
^^^^^^^^^^^^^

    * Size
    * Height
    * Thickness

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

Lin bear house
^^^^^^^^^^^^^^
    
    * Type

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

Filter holder
^^^^^^^^^^^^^

    * Length
    * Width

    .. image:: ../parts/img/filter_holder.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: filter_holder_clss
    .. autosummary::
        PartFilterHolder

Tensioner
^^^^^^^^^

    * Belt hight
    * Base width
    * Thickness
    * Metric nut

    .. image:: ../parts/img/tensioner.png
        :height: 148px
        :alt:   

.. toggle-header::
    :header: Details

    .. currentmodule:: tensioner_clss
    .. autosummary::
        TensionerSet

Belt clamp
^^^^^^^^^^

    * Type
    * Length
    * Width
    * Metric nut
 
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

Aluminium profile
^^^^^^^^^^^^^^^^^
    * Section
    * Length
        
    .. image:: ../parts/img/Profiles.png
        :height: 148px
        :alt: 

.. toggle-header::
    :header: Details

    .. currentmodule:: comps
    .. autosummary::
        PartAluProf
    
Bolts, Nuts & Washers
^^^^^^^^^^^^^^^^^^^^^

    * Type
    * Metric
    * Bolt length

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

Systems library
---------------

Filter Stage
^^^^^^^^^^^^

    * Move distance
    * Filter length
    * Filter width
    * Base width
    * Tensioner stroke
    * Tensioner thickness
    * Metric nut
    * Motor size
    * Length rail motor holder
    * Motor holder thickness

    .. image:: ../parts/img/filter_stage.png
        :height: 148 px
        :alt: Filter Stage Picture
    

.. _functions library:

Functions Library
-----------------

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

Class library
-------------

Nueva Clase
^^^^^^^^^^^^
.. currentmodule:: NuevaClase
.. autosummary:: 
    Obj3D
    

.. _UML:

UML
---

The UML (Unified Modeling Language) is the base diagram for software development.
It is a visual description of the relationships between class objects. 

.. figure:: ../parts/img/UML_simplificado.jpg
    :width: 296 px

The main class will be "*Obj3D*" which will contain the basic information of the model:

* Internal axis:

    * axis_d
    * axis_w
    * axis_h

* Children's dictionary:

    * dict_child
    * dict_child_sum
    * dict_child_res

The rest of the classes that generate the different 3D models will be part of the *Obj3D* class

|

.. blank line - image bigger than text

3D model details
----------------

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

Functions details
--------------------

fcfun
^^^^^

.. automodule:: fcfun
    :members:

Class details
------------------

Nueva Clase
^^^^^^^^^^^^
.. automodule:: NuevaClase
    :members:
