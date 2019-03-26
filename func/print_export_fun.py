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
import PySide
from PySide import QtCore, QtGui

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

    if  nema in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,1,0),180) 
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif objSelect.Name == 'idler_tensioner':
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,1,0),90)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif objSelect.Name == 'tensioner_holder':
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,0),-90)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif objSelect.Name == 'filter_holder':
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif nema_holder in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,1,0),180) 
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif thinlinbearhouse1rail in objSelect.Name:
        if top  in objSelect.Name:
            pos = objSelect.Placement.Base
            rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
            centre = FreeCAD.Vector(0,0,0)
            objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
        elif bot in objSelect.Name:
            pos = objSelect.Placement.Base
            rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
            centre = FreeCAD.Vector(0,0,0)
            objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
        else:
            message = QtGui.QMessageBox()
            message.setText('Error')
    elif bracket2 in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif bracket3 in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif bracket_twin in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif shaft in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif idlepulleyhold in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    elif simple_endstop_holder in objSelect.Name:
        pos = objSelect.Placement.Base
        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,0),0)
        centre = FreeCAD.Vector(0,0,0)
        objSelect.Placement = FreeCAD.Placement(pos,rot,centre)
    else:
        message = QtGui.QMessageBox()
        message.setText('This object is not a workbench object.\n')
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.setDefaultButton(QtGui.QMessageBox.Ok)
        message.exec_()
        show_message = False

    if show_message == True:
        message = QtGui.QMessageBox()
        message.setText("You select " + objSelect.Name + " to change to print position and export.\n")
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.setDefaultButton(QtGui.QMessageBox.Ok)
        message.exec_()
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
