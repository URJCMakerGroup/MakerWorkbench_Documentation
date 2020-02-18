.. Explicacion de donde surge la idea de Mechatronic


Introduccion
============

Qué es Mechatronic
------------------
Mechatronic es un Workbench para FreeCAD que permite la modificaciones de los modelos paramétricos que incluye y
facilita el ensamblaje y la composición. También facilita una librería de funciones con la que generar nuevos
modelos paramétricos que se pondrá incluir en el Workbench.

Funcionamiento
--------------
Mechatronic está enfocado a dos usuarios distintos:

**1.** Usuario básico: Usuario sin conocimientos de CAD o Programación que necesita realizar un diseño.
Para este usuario está enfocada la parte gráfica. Los pasos a seguir serían:

   1. Selecciona la pieza
   2. Introduce los valores deseados
   3. Ya tiene la pieza deseada

   .. note::
      Proximamente disponible tutorial
   
   Adicionalmente, este usuario puede querer combinar piezas entre sí. Para ello, está el módulo *Assembly* [#]_
   que permite la colocación de unas piezas respecto a otras
      

**2.** Usuario avanzado: Usuario con conocimientos de programación que quiere diseñar modelos 3D parametrizables.
Este usuario dispone de la :ref:`biblioteca de funciones` [#]_ para la realización de modelos 3D de manera sencilla.
Puede consultar el diseño de clases (:ref:`UML`) si desea comprender mejor el funcionamiento

Historia
--------
Mechatronic Workbench surge al realizar el proyecto Filter Stage. En este proyecto se realiza el diseño 
de un soporte para el portamuestras de un microscopio para la URJC.
Para poder modificar el diseño y adaptarlo a las dimensiones deseadas se realizó un diseño paramétrico.
El diseño paramétrico requiere el uso de un lenguaje de programación para describir el modelo, en este caso
Python.

En base a este diseño parametrizable surgió un trabajo final de grado para realizar un Workbench 
donde se pudieran modificar los parámetros del sistema Filter Stage desde la interface de FreeCAD. 

Se decidió mejorar este primer Workbench añadiendo diseños usados normalmente en sistemas mecatrónicos y funciones para 
facilitar la colocación de estos diseños

.. rubric:: Notes

.. [#] El módulo Assembly está pendiente de mejoras
.. [#] La bliblioteca de funciones está en proceso y aún no se encuentra disponible
