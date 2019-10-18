# Mechatronic
---
Select your lenguage:
## English
  This repository have the parts of a mechatronic system

  ---
  
### Index
  * [Folder organization](#folder-organization)
  * [Stable Version](#stable-version)
  * [How it's works](#how-its-works)
    * [Components](#components)
    * [Mechatronic system](#mechatronic-systems)
    * [Functions](#functions)
  ---
### Folder organization
  - comps: copy of the repository [fcad-comps](https://github.com/felipe-m/fcad-comps) of Felipe Machado.
  - icons: icons of the workbench.
  - parts: 
  - src: source code
      - func: functions makes for the workbench
  ---
### Stable version
  The stable version is in the file [Mechatronic.zip](https://github.com/davidmubernal/Mechatronic/blob/master/Mechatronic.zip). This version run in FreeCAD 0.18

  ---
### How it's works
  This workbench has some parts of a mechatronic system. You can modify this parts and build your system.
#### Components:

  Shaft holder
  - Size
  - Low profile: only size 8

  ![Sk](../parts/img/sk08.png)
  ![Sk2](../parts/img/sk08_pillow.png)  

  Idle pulley holder
  - Size of the profile
  - Metric Nut
  - Height
  - Position of the end stop sensor
  - Height of the end stop sensor

  End stop holder
  - Type
  - Distance of the rail

  ![End-Stop-30](../parts/img/endstop_holder_30.png)
  ![End-Stop-25-d3v](../parts/img/d3v_endstop_holder_r25_m4.png)

  Hall stop holder
  - Width
  - Thikness
  - Metric nut
  - Profile size
  - Reinforce

  ![hall_stop](../parts/img/hall_stop_holder_21_10.png)

  Bracket
  - Type: 3 options
  - Size first profile
  - Size second profile
  - Thickness
  - Metric nut first profile
  - Metric nut second profile
  - Number of nuts
  - Distance betwen nuts
  - Type of hole
  - Reinforcment: first type only
  - Flap: second type only
  - Distance between profiles: third type only

  ![bracket](../parts/img/bracket_30x30_m6.png)
  ![bracket-15](../parts/img/bracket_30x30_m6_rail15.png)
  ![bracket-20](../parts/img/bracket_30x30_m6_rail20_6thick.png)

  Motor holder
  - Size
  - Height
  - Thickness

  ![nema17-25](../parts/img/nema17_holder_rail25_8.png)
  ![nema17-35](../parts/img/nema17_holder_rail35_8.FCStd.png)

  Lin bear house
  - Type

  ![all](../parts/img/thinlinbearhouse1rail_lm8.png)
  ![bot](../parts/img/thinlinbearhouse1rail_lm8_bot.png)

  Filter holder
  - Length
  - Width

  ![filter_holder](../parts/img/filter_holder.png)

  Tensioner
  - Belt hight
  - Base width
  - Thickness
  - Metric nut

  ![tensioner](../parts/img/tensioner.png)

  Belt clamp
  - Type
  - Length
  - Width
  - Metric nut

  ![BeltClamp1](../parts/img/Belt_clamp_simple.png)
  ![BeltClamp2](../parts/img/Belt_clamp_double.png)

  Aluminium profile
  - Secction
  - Length

  ![Profiles](../parts/img/Profiles.png)

  Bolts, Nuts & Washers
  - Type
  - Metric
  - Bolt legnth

  ![Bolt](../parts/img/Bolts.png)
  ![Nut](../parts/img/Nuts.png)
  ![Washers](../parts/img/Washers.png)

#### Mechatronic Systems:
  Filter Stage
  - Move distance
  - Filter length
  - Filter width
  - Base width
  - Tensioner stroke
  - Tensioner thickness
  - Metric nut
  - Motor size
  - Lenght rail motor holder
  - Motor holder thickness

  ![filter_stage](../parts/img/filter_stage.png)

#### Functions:
  
  - Change to print position
  
    Change the position of the piece to print position. Also, the user can select the folder where is save the piece.

  - Assembly
 
    Select the part you like and a new place.

  ---
  ---