# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# -- Function Print and Export Object
# ----------------------------------------------------------------------------
# -- (c) David Muñoz Bernal
# ----------------------------------------------------------------------------
# -- This function set the object to yhe print position and export the object.
import os
import sys
import FreeCAD
import FreeCADGui
import Mesh
import MeshPart
import PySide
from PySide import QtCore, QtGui
import kparts


def print_export(objSelect):
    show_message = True
    nema = 'motorholder'
    nema_holder = 'nema_holder'
    thinlinbearhouse1rail = 'thinlinbearhouse1rail'
    top = 'top'
    bot = 'bot'
    bracket2 = 'bracket2'
    bracket3 = 'bracket3'
    bracket_twin = 'bracket_twin'
    shaft = 'shaft'
    idlepulleyhold = 'idlepulleyhold'
    simple_endstop_holder = 'endstop'
    stop_holder = 'stop_holder'

    #_________Motor_Holder_________
    if  nema in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,1,0),180) 
        centre = FreeCAD.Vector(0,0,0)

    #_________Idler_Tensioner_________
    elif objSelect.Name == 'idler_tensioner':
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,1,0),90)
        centre = FreeCAD.Vector(0,0,0)

    #_________Tensioner_Holder_________
    elif objSelect.Name == 'tensioner_holder':
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,0),-90)
        centre = FreeCAD.Vector(0,0,0)

    #_________Filter_Holder_________
    elif objSelect.Name == 'filter_holder':
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)

    #_________Nema_Holder_________
    elif nema_holder in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,1,0),180) 
        centre = FreeCAD.Vector(0,0,0)

    #_________Thinlinbearhouse1rail_________
    elif thinlinbearhouse1rail in objSelect.Name:
        if top  in objSelect.Name:
            pos = objSelect.Placement.Base
            rot = FreeCAD.Rotation(FreeCAD.Vector(0,1,0),180)
            centre = FreeCAD.Vector(0,0,0)

        elif bot in objSelect.Name:
            pos = objSelect.Placement.Base
            rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
            centre = FreeCAD.Vector(0,0,0)

        else:
            message = QtGui.QMessageBox()
            message.setText('Error')
            message.setStandardButtons(QtGui.QMessageBox.Ok)
            message.setDefaultButton(QtGui.QMessageBox.Ok)
            message.exec_()

    #_________Bracket_2_________
    elif bracket2 in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)
    
    #_________Bracket_3_________
    elif bracket3 in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)

    #_________Bracket_Twin_________
    elif bracket_twin in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)

    #_________Shaft_________
    elif shaft in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)

    #_________IdlepulleyHold_________
    elif idlepulleyhold in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)

    #_________Simple_End_Stop_Holder_________
    elif simple_endstop_holder in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)

    #_________Stop_Holder_________
    elif stop_holder in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)

    #_________Not_Name_________
    else:
        message = QtGui.QMessageBox()
        message.setText('This object is not a workbench object.\n')
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.setDefaultButton(QtGui.QMessageBox.Ok)
        message.exec_()
        show_message = False

    #######################################################
    #_________Message_And_Change_________
    if show_message == True:
        """message = QtGui.QMessageBox()
        message.setText("You select " + objSelect.Name + " to change to print position and export.\n")
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.setDefaultButton(QtGui.QMessageBox.Ok)
        message.exec_()"""
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        #_________EXPORT_________
        #Open the file explorer to set the folder
        gui = QtGui.QWidget()
        folderName = QtGui.QFileDialog.getExistingDirectory(gui,"Select directory","c:/",QtGui.QFileDialog.ShowDirsOnly) 


        # take the path and export the object
        stlFileName = str(folderName) + objSelect.Name + ".stl"
        mesh_shp = MeshPart.meshFromShape(objSelect.Shape,
                                            LinearDeflection=kparts.LIN_DEFL,
                                            AngularDeflection=kparts.ANG_DEFL)
        mesh_shp.write(stlFileName)
        del mesh_shp