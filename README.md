# Mechatronic

---

All the documentation of Mechatronic is in the website https://mechatronic.readthedocs.io/en/test-web/

Select your language:
<details>
  <summary>English</summary>
  This repository have the parts of a mechatronic system

  ---
  
  ### Index
  * [Folder organization](#folder-organization)
  * [Stable Version](#stable-version)
  * [How it works](#how-it-works)
    * [Components](#components)
    * [Mechatronic system](#mechatronic-systems)
    * [Functions](#functions)

  ---
  ### Folder organization
  - comps: copy of the repository [fcad-comps](https://github.com/felipe-m/fcad-comps) of Felipe Machado.
  - icons: icons of the workbench.
  - parts 
  - src: source code
      - func: functions makes for the workbench
  
  ---
  ### Stable version
  The stable version is in the file [Mechatronic.zip](https://github.com/davidmubernal/Mechatronic/blob/master/Mechatronic.zip). This version run in FreeCAD 0.18

  ---
  ### How it works
  This workbench has some parts of a mechatronic system. You can modify this parts and build your system.
  #### Components:
  <details>
    <summary>Shaft holder</summary>
      <ul>
        <li>Size</li>
        <li>Low profile: only size 8</li>
      </ul>
  </details>

  ![Sk](/parts/img/sk08.png)
  ![Sk2](/parts/img/sk08_pillow.png)  

  <details>
    <summary>Idle pulley holder</summary>
      <ul>
        <li>Size of the profile</li>
        <li>Metric Nut</li>
        <li>Height</li>
        <li>Position of the end stop sensor</li> 
        <li>Height of the end stop sensor</li>
      </ul>
  </details>

  <details>
    <summary>End stop holder</summary>
      <ul>
        <li>Type</li>
        <li>Rail length</li>
      </ul>
  </details>

  ![End-Stop-30](/parts/img/endstop_holder_30.png)
  ![End-Stop-25-d3v](/parts/img/d3v_endstop_holder_r25_m4.png)

  <details>
    <summary>Hall stop holder</summary>
      <ul>
        <li>Width</li>
        <li>Thikness</li>
        <li>Metric nut</li>
        <li>Profile size</li>
        <li>Reinforce</li>
      </ul>
  </details>

  ![hall_stop](/parts/img/hall_stop_holder_21_10.png)

  <details>
    <summary>Bracket</summary>
      <ul>
        <li>Type: 3 options</li>
        <li>Size first profile</li>
        <li>Size second profile</li>
        <li>Thickness</li>
        <li>Metric nut first profile</li>
        <li>Metric nut second profile</li>
        <li>Number of nuts</li>
        <li>Distance betwen nuts</li>
        <li>Type of hole</li>
        <li>Reinforcement: first type only</li>
        <li>Flap: second type only</li>
        <li>Distance between profiles: third type only</li>
      </ul>
  </details>

  ![bracket](/parts/img/bracket_30x30_m6.png)
  ![bracket-15](/parts/img/bracket_30x30_m6_rail15.png)
  ![bracket-20](/parts/img/bracket_30x30_m6_rail20_6thick.png)

  <details>
    <summary>Motor holder</summary>
      <ul>
        <li>Size</li>
        <li>Height</li>
        <li>Thickness</li>
      </ul>
  </details>

  ![nema17-25](/parts/img/nema17_holder_rail25_8.png)
  ![nema17-35](/parts/img/nema17_holder_rail35_8.FCStd.png)

  <details>
    <summary>Lin bear house</summary>
      <ul>
        <li>Type</li>
      </ul>
  </details>

  ![all](/parts/img/thinlinbearhouse1rail_lm8.png)
  ![bot](/parts/img/thinlinbearhouse1rail_lm8_bot.png)

  <details>
    <summary>Filter holder</summary>
      <ul>
        <li>Length</li>
        <li>Width</li>
      </ul>
  </details>

  ![filter_holder](/parts/img/filter_holder.png)

  <details>
    <summary>Tensioner</summary>
      <ul>
        <li>Belt hight</li>
        <li>Base width</li>
        <li>Thickness</li>
        <li>Metric nut</li>
      </ul>
  </details>

  ![tensioner](/parts/img/tensioner.png)

  <details>
    <summary>Belt clamp</summary>
      <ul>
        <li>Type</li>
        <li>Length</li>
        <li>Width</li>
        <li>Metric nut</li>
      </ul>
  </details>

  ![BeltClamp1](/parts/img/Belt_clamp_simple.png)
  ![BeltClamp2](/parts/img/Belt_clamp_double.png)

  <details>
      <summary>Aluminium profile</summary>
        <ul>
          <li>Section</li>
          <li>Length</li>
        </ul>
    </details>

  ![Profiles](/parts/img/Profiles.png)

  <details>
    <summary>Bolts, Nuts & Washers</summary>
      <ul>
        <li>Type</li>
        <li>Metric</li>
        <li>Bolt length</li>
      </ul>
  </details>

  ![Bolt](/parts/img/Bolts.png)
  ![Nut](/parts/img/Nuts.png)
  ![Washers](/parts/img/Washers.png)

  #### Mechatronic Systems:
  <details>
    <summary>Filter Stage</summary>
      <ul>
        <li>Move distance</li>
        <li>Filter length</li>
        <li>Filter width</li>
        <li>Base width</li>
        <li>Tensioner stroke</li>
        <li>Tensioner thickness</li>
        <li>Metric nut</li>
        <li>Motor size</li>
        <li>Length rail motor holder</li>
        <li>Motor holder thickness</li>
      </ul>
  </details>

  ![filter_stage](/parts/img/filter_stage.png)

  #### Functions:
  <details>
    <summary>Change to print position</summary>
    Change the position of the piece to print position. Also, the user can select the folder where is save the piece.
  </details>

  <details>
    <summary>Assembly</summary>
    Select the part you want to move and the place to assembly.
  </details>

  ---
  ---
</details>
 
<details>
  <summary>Español</summary>
  Este repositorio tiene componentes de un sistema mecatrónico.

  ### Índice
  * [Organización de las carpetas](#organización-de-las-carpetas)
  * [Versión estable](#verión-estable)
  * [Funcionamiento del workbench](#funcionamiento-del-workbench)  
  * [Componentes](#componentes)
  * [Sistemas mecatrónicos](#sistemas-mecatrónicos)
  * [Funciones](#funciones)

  ---
  ### Organización de las carpetas:
  - comps: copia del repositorio [fcad-comps](https://github.com/felipe-m/fcad-comps) de Felipe Machado.
  - icons: iconos del workbench.
  - parts 
  - src: código fuente
      - func: funciones creadas para el workbench

  ---
  ### Versión estable:
  La versión estable del workbench se encuentra en el archivo comprimido [Mechatronic.zip](https://github.com/davidmubernal/Mechatronic/blob/master/Mechatronic.zip). Funciona en FreeCAD 0.18

  ---
  ### Funcionamiento del workbench

  El workbench consta de un conjunto de piezas empleadas en sistemas mecatrónicos.  
  En función de la pieza que seleccionemos tendremos distintas opciones de modificación

  #### Componentes:
  <details>
    <summary>Soporte de eje</summary>
      <ul>
        <li>Tamaño</li>
        <li>Perfil bajo: sólo para tamaño 8</li>
      </ul>
  </details>

  ![Sk](/parts/img/sk08.png)
  ![Sk2](/parts/img/sk08_pillow.png)

  <details>
    <summary>Soporte polea loca</summary>
      <ul>
        <li>Tamaño del perfil sobre el que se monta</li>
        <li>Métrica de los tornillos</li>
        <li>Altura</li>
        <li>Posición del sensor de final de carrera</li>
        <li>Altura del sensor de final de carrera</li>
      </ul>
  </details>

  <details>
    <summary>Soporte final de carrera</summary>
      <ul>
        <li>Tipo</li>
        <li>Distancia del carril</li>
      </ul>
  </details>

  ![End-Stop-30](/parts/img/endstop_holder_30.png)
  ![End-Stop-25-d3v](/parts/img/d3v_endstop_holder_r25_m4.png)

  <details>
    <summary>Soporte final</summary>
      <ul>
        <li>Ancho</li>
        <li>Espesor</li>
        <li>Métrica tornillo</li>
        <li>Tamaño perfil</li>
        <li>Refuerzo</li>
      </ul>
  </details>

  ![hall_stop](/parts/img/hall_stop_holder_21_10.png)

  <details>
    <summary>Bracket para perfiles</summary>
      <ul>
        <li>Tipo: 3 opciones distintas</li>
        <li>Tamaño primer perfil</li>
        <li>Tamaño segundo perfil</li>
        <li>Espesor</li>
        <li>Métrica tornillo primer perfil</li>
        <li>Métrica tornillo segundo perfil</li>
        <li>Número de tornillos</li>
        <li>Distancia entre tornillos</li>
        <li>Seleccion agujero</li>
        <li>Refuerzo: sólo para el primer tipo de bracket</li>
        <li>Flap: sólo para el segundo tipo de bracket</li>
        <li>Distancia entre perfiles: sólo para el tercer tipo de bracket</li>
      </ul>
  </details>

  ![bracket](/parts/img/bracket_30x30_m6.png)
  ![bracket-15](/parts/img/bracket_30x30_m6_rail15.png)
  ![bracket-20](/parts/img/bracket_30x30_m6_rail20_6thick.png)

  <details>
    <summary>Soporte motor</summary>
      <ul>
        <li>Tamaño del soporte</li>
        <li>Altura del soporte</li>
        <li>Espesor de las paredes del soporte</li>
      </ul>
  </details>

  ![nema17-25](/parts/img/nema17_holder_rail25_8.png)
  ![nema17-35](/parts/img/nema17_holder_rail35_8.FCStd.png)

  <details>
    <summary>Carcasa del rodamiento lineal</summary>
      <ul>
        <li>Tipo</li>
      </ul>
  </details>

  ![all](/parts/img/thinlinbearhouse1rail_lm8.png)
  ![bot](/parts/img/thinlinbearhouse1rail_lm8_bot.png)

  <details>
    <summary>Soporte del filtro</summary>
      <ul>
        <li>Largo</li>
        <li>Ancho</li>
      </ul>
  </details>

  ![filter_holder](/parts/img/filter_holder.png)

  <details>
    <summary>Tensionador de la polea</summary>
      <ul>
        <li>Altura de polea</li>
        <li>Ancho de base</li>
        <li>Espesor</li>
        <li>Métrica del tornillo</li>
      </ul>
  </details>

  ![tensioner](/parts/img/tensioner.png)

  <details>
    <summary>Abrazadera de polea</summary>
      <ul>
        <li>Tipo</li>
        <li>Largo</li>
        <li>Ancho</li>
        <li>Métrica del tornillo</li>
      </ul>
  </details>

  ![BeltClamp1](/parts/img/Belt_clamp_simple.png)
  ![BeltClamp2](/parts/img/Belt_clamp_double.png)

  <details>
      <summary>Perfil de aluminio</summary>
        <ul>
          <li>Sección</li>
          <li>Longitud</li>
        </ul>
    </details>

  ![Profiles](/parts/img/Profiles.png)

  <details>
      <summary>Tornillos, Tuercas y Arandelas</summary>
        <ul>
          <li>Tipo</li>
          <li>Métrica</li>
          <li>Longitud del tornillo</li>
        </ul>
  </details>

  ![Bolt](/parts/img/Bolts.png)
  ![Nut](/parts/img/Nuts.png)
  ![Washers](/parts/img/Washers.png)

  #### Sistemas mecatrónicos:
  <details>
    <summary>Filter Stage</summary>
      <ul>
        <li>Distancia de recorrido</li>
        <li>Largo del filtro</li>
        <li>Ancho del filtro</li>        
        <li>Ancho de base</li>
        <li>Largo tensionador</li>
        <li>Espesor tensionador</li>
        <li>Métrica del tornillo</li>
        <li>Tamaño del motor</li>
        <li>Longitud del rail del soporte motor</li>
        <li>Espesor del soporte motor</li>
      </ul>
  </details>

  ![filter_stage](/parts/img/filter_stage.png)

  #### Funciones:
  <details>
    <summary>Cambiar a posición de imprimir</summary>
    Coloca la pieza seleccionada en la posición de impresión y pide al usuario la carpeta donde exportar la pieza.
  </details>

  <details>
    <summary>Ensamblaje</summary>
    Selecciona la pieza que quieres mover y su nueva posición.
  </details>

  ---
  --- 
</details>
