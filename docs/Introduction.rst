.. Explicacion de donde surge la idea de Mechatronic


Introduccion
============

Mechatronic
-----------
Mechatronic is a Workbench for FreeCAD that allows the modification of parametric models that includes and
facilitates assembly and composition. It also provides a library of functions with which to generate new
parametric models to be included in the Workbench.

How it works
------------
Mechatronic is designed for two different users:

**1.** Basic User: User without CAD or Programming knowledge who needs to make a design.
For this user is the graphic part. The steps to follow would be:

   1. Select the part
   2. Enter the values you want to use
   3. You already have the part you want.
   
   .. note::
      See the :ref:`Tutorial` section for more details

   Additionally, this user may want to combine parts with each other. For this purpose, there is the *Assembly* module [#]_
   that allows the placement of some pieces with respect to others
      

**2.** Advanced user: User with programming knowledge who wants to design parameterizable 3D models.
This user has the :ref:`functions library` [#]_ to make 3D models in a simple way.
You can consult the class design (:ref:`UML`) if you wish to better understand the operation

History
-------
Mechatronic Workbench started with the Filter Stage project. In this project, we designed a support for the 
sample holder of a microscope to the URJC.
To be able to modify the design and adapt it to the required dimensions, we chose to make a parametric design.
Parametric design requires the use of a programming language to describe the model, in this case we use Python.

Based on this parameterizable design, a final degree work was conceived to create a Workbench 
where the Filter Stage parameters could be modified from the FreeCAD interface. 

It was decided to improve this first Workbench by adding designs commonly used in mechatronic systems and 
functions to facilitate the placement of these designs

.. rubric:: Footnotes

.. [#] The Assembly module will be upgraded
.. [#] The functions library is in process
