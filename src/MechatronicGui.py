# -*- coding: utf-8 -*-
# FreeCAD script for the commands of the mechatronic workbench
# (c) 2019 David Muñoz Bernal

#***************************************************************************
#*   (c) David Muñoz Bernal                                                *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/

import PySide
from PySide import QtCore, QtGui
import os
import FreeCAD
import FreeCADGui
import logging

import comps
from fcfun import V0, VX, VY, VZ, VZN
import parts
import kcomp
import partset
import beltcl
from filter_stage_fun import filter_stage_fun
import tensioner_clss
import filter_holder_clss
from print_export_fun import print_export

from parts import AluProfBracketPerp, AluProfBracketPerpFlap, AluProfBracketPerpTwin, NemaMotorHolder, ThinLinBearHouse1rail

import grafic

__dir__ = os.path.dirname(__file__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

###############################################################################
#***************************************SK*************************************
class _Sk_Dir_Cmd:
    def Activated(self):
        baseWidget = QtGui.QWidget()
        panel = Sk_Dir_TaskPanel(baseWidget)

        FreeCADGui.Control.showDialog(panel)
    
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Sk',
            'Sk')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Sk',
            'Create a Sk')
        return {
            'Pixmap': __dir__ + '/icons/Sk_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class Sk_Dir_TaskPanel:
    def __init__(self,widget):
        self.form = widget
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Size
        # Label:
        self.Size_Label = QtGui.QLabel("Size:")
        # Spin Box that takes doubles
        self.Size_ComboBox = QtGui.QComboBox()
        # text:
        self.Size_text = ["6","8","10","12"]
        self.Size_ComboBox.addItems(self.Size_text)
        self.Size_ComboBox.setCurrentIndex(0)
        

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Size_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Size_ComboBox,0,1,1,1)

        # ---- row 1: Pillow
        # Label:
        self.Pillow_Label = QtGui.QLabel("Pillow:")
        self.Pillow_Label2 = QtGui.QLabel("(only for size 8)")
        # Spin Box that takes doubles
        self.Pillow_ComboBox = QtGui.QComboBox()
        # Add values in ComboBox
        self.V_Pillow = ["No","Yes"]
        self.Pillow_ComboBox.addItems(self.V_Pillow)
        self.Pillow_ComboBox.setCurrentIndex(self.V_Pillow.index('No'))
        
        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Pillow_Label,1,0,1,1)
        layout.addWidget(self.Pillow_Label2,2,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Pillow_ComboBox,1,1,1,1)
    
    def accept(self):
        Size_Value = {0:6, 1:8, 2:10, 3:12}
        Values_Pillow = {0: 0, 1: 1}
        TOL_Value = {0: 0.4, 1: 0.7}
        Size = Size_Value[self.Size_ComboBox.currentIndex()]
        Pillow = Values_Pillow[self.Pillow_ComboBox.currentIndex()]
        Tol = TOL_Value[self.Pillow_ComboBox.currentIndex()]
        
        if Pillow == 0 or (Pillow == 1 and Size == 8): # Pillow only exist for size 8.
            comps.Sk_dir(size = Size,
                    fc_axis_h = VX,
                    fc_axis_d = VZ,
                    fc_axis_w = V0,
                    ref_hr = 0,
                    ref_wc = 0,
                    ref_dc = 0,
                    pillow = Pillow,
                    pos = V0,
                    tol = Tol,#0.7, # for the pillow block
                    wfco = 1,
                    name= "shaft" + str(Size) + "_holder")
            FreeCADGui.activeDocument().activeView().viewAxonometric() #Axonometric view
            FreeCADGui.SendMsgToActiveView("ViewFit") #Fit the view to the object
            FreeCADGui.Control.closeDialog() #close the dialog

        elif Pillow == 1 and Size != 8:
            message = QtGui.QMessageBox()
            message.setText("This Size don't have Pillow option")
            message.setStandardButtons(QtGui.QMessageBox.Ok)
            message.setDefaultButton(QtGui.QMessageBox.Ok)
            message.exec_()

    #When you click on the cancel button have a default behaviur.
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

###############################################################################
#*****************************IDLE**PULLEY**HOLDER*****************************
class _IdlePulleyHolder_Cmd:
    def Activated(self):
        baseWidget = QtGui.QWidget()
        panel = IdlePulleyHolder_TaskPanel(baseWidget)

        FreeCADGui.Control.showDialog(panel)
    
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Idle Pulley Holder',
            'Idle Pulley Holder')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Idle Pulley Holder',
            'Create an Idle Pulley Holder')
        return {
            'Pixmap': __dir__ + '/icons/IdlePulleyHolder_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class IdlePulleyHolder_TaskPanel:
    def __init__(self,widget):
        self.form = widget
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Aluprof
        # Label:
        self.ALuprof_Label = QtGui.QLabel("Aluminium profile:")
        # Combo Box
        self.Aluprof_ComboBox = QtGui.QComboBox()
        # Add items
        self.Aluprof_Str = ["20mm","30mm"]
        self.Aluprof_ComboBox.addItems(self.Aluprof_Str)
        self.Aluprof_ComboBox.setCurrentIndex(0)

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.ALuprof_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Aluprof_ComboBox,0,1,1,1)

        # ---- row 1: Nut Bolt
        # Label:
        self.NutBolt_Label = QtGui.QLabel("Nut bolt:")
        # Combo Box 
        self.NutBolt_Str = ["2.5","3","4","5","6"]
        self.NutBolt_ComboBox = QtGui.QComboBox()
        # Add items
        self.NutBolt_ComboBox.addItems(self.NutBolt_Str)
        self.NutBolt_ComboBox.setCurrentIndex(3)

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.NutBolt_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.NutBolt_ComboBox,1,1,1,1)

        # ---- row 2: High to profile
        # Label:
        self.HighToProfile_Label = QtGui.QLabel("High to profile:")
        # Spin Box that takes doubles
        self.HighToProfile_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.HighToProfile_Value.setValue(40)
        # suffix to indicate the units
        self.HighToProfile_Value.setSuffix(' mm')

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.HighToProfile_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.HighToProfile_Value,2,1,1,1)

        # ---- row 3: End Stop Side
        # Label:
        self.EndSide_Label = QtGui.QLabel("End Stop Side:")
        # Spin Box that takes doubles
        self.EndSide_ComboBox = QtGui.QComboBox()
        # Add items
        self.EndSide_Str = ["1","0","-1"]
        self.EndSide_ComboBox.addItems(self.EndSide_Str)
        self.EndSide_ComboBox.setCurrentIndex(1)

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.EndSide_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.EndSide_ComboBox,3,1,1,1)

        # ---- row 4: End Stop High
        # Label:
        self.EndStopHigh_Label = QtGui.QLabel("End Stop Pos:")
        # Spin Box that takes doubles
        self.EndStopHigh_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.EndStopHigh_Value.setValue(0)
        # suffix to indicate the units
        self.EndStopHigh_Value.setSuffix(' mm')

        # row 4, column 0, rowspan 1, colspan 1
        layout.addWidget(self.EndStopHigh_Label,4,0,1,1)
        # row 4, column 1, rowspan 1, colspan 1
        layout.addWidget(self.EndStopHigh_Value,4,1,1,1)

    def accept(self):
        self.Aluprof_values = {0: 20, 1:30}
        self.NutBolt_values = {0:2.5, 1:3, 2:4, 3:5, 4:6}
        self.EndSide_values = {0:1, 1:0, 2:-1}
        Aluprof = self.Aluprof_values[self.Aluprof_ComboBox.currentIndex()]
        NutBolt = self.NutBolt_values[self.NutBolt_ComboBox.currentIndex()]
        High = self.HighToProfile_Value.value()
        EndSide = self.EndSide_values[self.EndSide_ComboBox.currentIndex()]
        EndHigh = self.EndStopHigh_Value.value()

        parts.IdlePulleyHolder( profile_size= Aluprof, #20.,#
                                pulleybolt_d=3.,
                                holdbolt_d = NutBolt, #5,#
                                above_h = High, #40,#
                                mindepth = 0,
                                attach_dir = '-y',
                                endstop_side = EndSide, #0,
                                endstop_posh = EndHigh, #0,  
                                name = "idlepulleyhold")
        
        FreeCADGui.activeDocument().activeView().viewAxonometric() #Axonometric view
        FreeCADGui.SendMsgToActiveView("ViewFit") #Fit the view to the object
        FreeCADGui.Control.closeDialog() #close the dialog

    #When you click on the cancel button have a default behaviur.

    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

###############################################################################
#**************************SIMPLE**END***STOP**HOLDER**************************
class _SimpleEndStopHolder_Cmd:
    def Activated(self):
        baseWidget = QtGui.QWidget()
        panel = SimpleEndStopHolder_TaskPanel(baseWidget)

        FreeCADGui.Control.showDialog(panel)
    
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Simple End Stop Holder',
            'Simple End Stop Holder')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Simple End Stop Holder',
            'Create a Simple End Stop Holder')
        return {
            'Pixmap': __dir__ + '/icons/SimpleEndStopHolder_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None
class SimpleEndStopHolder_TaskPanel:
    def __init__(self, widget):
        self.form = widget
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: 
        # Label:
        self.Type_Label = QtGui.QLabel("Type:")
        # ComboBox
        self.Type_ComboBox = QtGui.QComboBox()
        Type_text = ["A","B"]
        self.Type_ComboBox.addItems(Type_text)
        self.Type_ComboBox.setCurrentIndex(0)

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Type_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Type_ComboBox,0,1,1,1)

        # ---- row 1: 
        # Label:
        self.Rail_Label = QtGui.QLabel("Rail Lenght:")
        # Spin Box that takes doubles
        self.Rail_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Rail_Value.setValue(15)
        # suffix to indicate the units
        self.Rail_Value.setSuffix(' mm')

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Rail_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Rail_Value,1,1,1,1)



        
    def accept(self):
        Type_values = {0:kcomp.ENDSTOP_A, 1:kcomp.ENDSTOP_B}
        Type = Type_values[self.Type_ComboBox.currentIndex()]
        Rail_L = self.Rail_Value.value()
        parts.SimpleEndstopHolder(d_endstop = Type,
                                  rail_l = Rail_L,
                                  base_h = 5.,
                                  h = 0,
                                  holder_out = 2.,
                                  #csunk = 1,
                                  mbolt_d = 3.,
                                  endstop_nut_dist = 0.,
                                  min_d = 0,
                                  fc_axis_d = VX,
                                  fc_axis_w = V0,
                                  fc_axis_h = VZ,
                                  ref_d = 1,
                                  ref_w = 1,
                                  ref_h = 1,
                                  pos = V0,
                                  wfco = 1,
                                  name = 'simple_endstop_holder')
        
        FreeCADGui.activeDocument().activeView().viewAxonometric() #Axonometric view
        FreeCADGui.SendMsgToActiveView("ViewFit") #Fit the view to the object
        FreeCADGui.Control.closeDialog() #close the dialog

###############################################################################
#*******************************ALUPROF**BRACKET*******************************
class _AluprofBracket_Cmd:
    def Activated(self):
        baseWidget = QtGui.QWidget()
        #panel = AluprofBracket_Set_TaskPanel(baseWidget)
        panel = AluprofBracket_TaskPanel(baseWidget)

        FreeCADGui.Control.showDialog(panel)
    
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Aluprof Bracket',
            'Aluprof Bracket')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Aluprof Bracket',
            'Create an Aluprof Bracket')
        return {
            'Pixmap': __dir__ + '/icons/AluprofBracket_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class AluprofBracket_TaskPanel:
    def __init__(self, widget):#,Type):
        self.form = widget
        # The layout will be a grid
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Type
        # Label:
        self.Type_Label = QtGui.QLabel("Selected Type:")
        # Label with Bracket selected:
        self.Type_Aluprof = ["2 profiles","2 profiles with flap","3 profiles"]
        #self.Type_Sel_Label = QtGui.QLabel(self.Type_Aluprof[Type])
        self.Type_ComboBox = QtGui.QComboBox()
        self.Type_Aluprof = ["2 profiles","2 profiles with flap","3 profiles"]
        self.Type_ComboBox.addItems(self.Type_Aluprof)
        self.Type_ComboBox.setCurrentIndex(0)
        
        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Type_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        #layout.addWidget(self.Type_Sel_Label,0,1,1,1)
        layout.addWidget(self.Type_ComboBox,0,1,1,1)

        # ---- row 1: Size profile line 1
        # Label:
        self.Size_1_Label = QtGui.QLabel("Size first profile:")
        # ComboBox
        self.Size_1_ComboBox = QtGui.QComboBox()
        self.Size_text = ["10mm","15mm","20mm","30mm","40mm"]         ##Select profiles kcomp
        self.Size_1_ComboBox.addItems(self.Size_text)
        self.Size_1_ComboBox.setCurrentIndex(self.Size_text.index('20mm'))

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Size_1_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Size_1_ComboBox,1,1,1,1)

        
        # ---- row 2: Size profile line 2
        # Label:
        self.Size_2_Label = QtGui.QLabel("Size second profile:")
        # ComboBox
        self.Size_2_ComboBox = QtGui.QComboBox()
        self.Size_2_ComboBox.addItems(self.Size_text)
        self.Size_2_ComboBox.setCurrentIndex(self.Size_text.index('20mm'))

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Size_2_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Size_2_ComboBox,2,1,1,1)

        
        # ---- row 3: Thikness 
        # Label:
        self.Thikness_Label = QtGui.QLabel("Thikness:")
        # Spin Box that takes doubles
        self.Thikness_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Thikness_Value.setValue(3)
        self.Thikness_Value.setMinimum(2)
        # suffix to indicate the units
        self.Thikness_Value.setSuffix(' mm')

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Thikness_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Thikness_Value,3,1,1,1)

        
        # ---- row 4: Nut profile line 1
        # Label:
        self.Nut_Profile_1_Label = QtGui.QLabel("Size of Nut first profile :")
        #ComboBox for NUt type 1
        self.Nut_Profile_1_ComboBox = QtGui.QComboBox()
        self.NUT_text = ["M3","M4","M5","M6"]    #D912
        self.Nut_Profile_1_ComboBox.addItems(self.NUT_text)
        self.Nut_Profile_1_ComboBox.setCurrentIndex(0)

        # row 4, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Nut_Profile_1_Label,4,0,1,1)
        # row 4, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Nut_Profile_1_ComboBox,4,1,1,1)
        
        
        # ---- row 5: Nut profile line 2
        # Label:
        self.Nut_Profile_2_Label = QtGui.QLabel("Size of Nut second profile :")
        # ComboBox for Nut type 2
        self.Nut_Profile_2_ComboBox = QtGui.QComboBox()
        self.Nut_Profile_2_ComboBox.addItems(self.NUT_text)
        self.Nut_Profile_2_ComboBox.setCurrentIndex(0)

        # row 5, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Nut_Profile_2_Label,5,0,1,1)
        # row 5, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Nut_Profile_2_ComboBox,5,1,1,1)

        # ---- row 6: Nº Nut
        # Label:
        self.N_Nut_Label = QtGui.QLabel("Number of Nuts:")
        # Spin Box that takes doubles
        self.N_Nut_ComboBox = QtGui.QComboBox()
        self.N_Nut_text = ["1","2"]
        self.N_Nut_ComboBox.addItems(self.N_Nut_text)
        self.N_Nut_ComboBox.setCurrentIndex(0)

        # row 6, column 0, rowspan 1, colspan 1
        layout.addWidget(self.N_Nut_Label,6,0,1,1)
        # row 6, column 1, rowspan 1, colspan 1
        layout.addWidget(self.N_Nut_ComboBox,6,1,1,1)

        # ---- row 7: Dist Nut
        # Label:
        self.Dist_Nut_Label = QtGui.QLabel("Distance between nuts:")
        self.Dist_Nut_Label2 = QtGui.QLabel("(0 = min distance)")
        # Spin Box that takes doubles
        self.Dist_Nut_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Dist_Nut_Value.setValue(0)
        self.Dist_Nut_Value.setMinimum(0)
        # suffix to indicate the units
        self.Dist_Nut_Value.setSuffix(' mm')

        # row 7, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Dist_Nut_Label,7,0,1,1)
        # row 8, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Dist_Nut_Label2,8,0,1,1)
        # row 7, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Dist_Nut_Value,7,1,1,1)

        
        # ---- row 9: Sunk
        # Label:
        self.Sunk_Label = QtGui.QLabel("Sunk:")
        # Spin Box that takes doubles
        self.Sunk_ComboBox = QtGui.QComboBox()
        Sunk_Text = ["Hole fot Nut","Without center","Withput reinforce"]
        self.Sunk_ComboBox.addItems(Sunk_Text)
        self.Sunk_ComboBox.setCurrentIndex(0)

        # row 9, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Sunk_Label,9,0,1,1)
        # row 9, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Sunk_ComboBox,9,1,1,1)        

        #if self.Type == 0:
            #self.form.repaint()
        # ---- row 10: Reinforce
        # Label:
        self.Reinforce_Label = QtGui.QLabel("Reinforce:")
        self.Reinforce_Label2= QtGui.QLabel("(Only for 2 profile)")
        # Spin Box that takes doubles
        self.Reinforce_ComboBox = QtGui.QComboBox()
        self.Reinforce_text = ["No","Yes"]
        self.Reinforce_ComboBox.addItems(self.Reinforce_text)
        self.Reinforce_ComboBox.setCurrentIndex(0)

        # row 10, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Reinforce_Label,10,0,1,1)
        layout.addWidget(self.Reinforce_Label2,11,0,1,1)
        # row 10, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Reinforce_ComboBox,10,1,1,1)

        #elif self.Type == 1:
            #self.form.repaint()
        # ---- row 11: Flap
        # Label:
        self.Flap_Label = QtGui.QLabel("Flap:")
        self.Flap_Label2 = QtGui.QLabel("(Only for 2 profiles with flap)")
        # Spin Box that takes doubles
        self.Flap_ComboBox = QtGui.QComboBox()
        # Default value
        self.Flap_text = ["No","Yes"]
        self.Flap_ComboBox.addItems(self.Flap_text)
        self.Flap_ComboBox.setCurrentIndex(1)

        # row 12, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Flap_Label,12,0,1,1)
        # row 13, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Flap_Label2,13,0,1,1)
        # row 12, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Flap_ComboBox,12,1,1,1)
        
        # ---- row 14: Dist Between Profiles
        # Label:
        self.Dist_Prof_Label = QtGui.QLabel("Dist between profiles:")
        self.Dist_Prof_Label2 = QtGui.QLabel("(Only fot 3 profiles)")
        # Spin Box that takes doubles
        self.Dist_Prof_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Dist_Prof_Value.setValue(26)
        self.Dist_Prof_Value.setMinimum(26)
        # suffix to indicate the units
        self.Dist_Prof_Value.setSuffix(' mm')

        # row 14, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Dist_Prof_Label,14,0,1,1)
        # row 15, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Dist_Prof_Label2,15,0,1,1)
        # row 14, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Dist_Prof_Value,14,1,1,1)


    def accept(self):
        NUT = {0:3, 1:4, 2:5, 3:6}
        Size = {0: 10, 1: 15, 2: 20, 3: 30, 4: 40}
        Sunk_values = {0:0, 1:1, 2:2}
        Size_1 = Size[self.Size_1_ComboBox.currentIndex()]
        Size_2 = Size[self.Size_2_ComboBox.currentIndex()]
        Thikness = self.Thikness_Value.value()
        Nut_Prof_1 = NUT[self.Nut_Profile_1_ComboBox.currentIndex()]
        Nut_Prof_2 = NUT[self.Nut_Profile_2_ComboBox.currentIndex()]
        NumberNut = 1+self.N_Nut_ComboBox.currentIndex()
        Dist_Nut = self.Dist_Nut_Value.value()
        Sunk = Sunk_values[self.Sunk_ComboBox.currentIndex()]
        self.Type = self.Type_ComboBox.currentIndex()

        if self.Type == 0:
            Reinforce = self.Reinforce_ComboBox.currentIndex()
            parts.AluProfBracketPerp( alusize_lin = Size_1, alusize_perp = Size_2, #cambiar a combobox
                                      br_perp_thick = Thikness,
                                      br_lin_thick = Thikness,
                                      bolt_lin_d = Nut_Prof_1,
                                      bolt_perp_d = Nut_Prof_2,
                                      nbolts_lin = NumberNut,
                                      bolts_lin_dist = Dist_Nut,
                                      bolts_lin_rail = Dist_Nut,
                                      xtr_bolt_head = 0,
                                      xtr_bolt_head_d = 0, # space for the nut
                                      reinforce = Reinforce,
                                      fc_perp_ax = VZ,
                                      fc_lin_ax = VX,
                                      pos = V0,
                                      wfco=1,
                                      name = 'bracket2_perp')
        elif self.Type == 1:
            Flap = self.Flap_ComboBox.currentIndex()
            parts.AluProfBracketPerpFlap(alusize_lin = Size_1, alusize_perp = Size_2,
                                        br_perp_thick = Thikness,
                                        br_lin_thick = Thikness,
                                        bolt_lin_d = Nut_Prof_1,
                                        bolt_perp_d = Nut_Prof_2,
                                        nbolts_lin = NumberNut,
                                        bolts_lin_dist = Dist_Nut,
                                        bolts_lin_rail = Dist_Nut,
                                        xtr_bolt_head = 1,
                                        sunk = Sunk,
                                        flap = Flap, 
                                        fc_perp_ax = VZ,
                                        fc_lin_ax = VX,
                                        pos = V0,
                                        wfco=1,
                                        name = 'bracket3_flap')
        elif self.Type ==2:
            Dis_Prof = self.Dist_Prof_Value.value()
            parts.AluProfBracketPerpTwin(alusize_lin = Size_1, alusize_perp = Size_2,
                                        alu_sep = Dis_Prof,
                                        br_perp_thick = Thikness,
                                        br_lin_thick = Thikness,
                                        bolt_lin_d = Nut_Prof_1,
                                        bolt_perp_d = Nut_Prof_2,
                                        nbolts_lin = NumberNut,
                                        bolts_lin_dist = Dist_Nut,
                                        bolts_lin_rail = Dist_Nut,
                                        bolt_perp_line = 0,
                                        xtr_bolt_head = 2, 
                                        sunk = Sunk,
                                        fc_perp_ax = VZ,
                                        fc_lin_ax = VX,
                                        fc_wide_ax = VY,
                                        pos = V0,
                                        wfco=1,
                                        name = 'bracket_twin')

        FreeCADGui.activeDocument().activeView().viewAxonometric() #Axonometric view
        FreeCADGui.SendMsgToActiveView("ViewFit") #Fit the view to the object
        FreeCADGui.Control.closeDialog() #close the dialog


###############################################################################
#********************************Motor***Holder********************************
class _MotorHolderCmd:
    
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        Widget_MotorHolder = QtGui.QWidget()
        Panel_MotorHolder = MotorHolderTaskPanel(Widget_MotorHolder)
        FreeCADGui.Control.showDialog(Panel_MotorHolder) 
        

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Motor Holder',
            'Motor Holder')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Motor Holder',
            'Creates a Motor Holder')
        return {
            'Pixmap': __dir__ + '/icons/Motor_Holder_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class MotorHolderTaskPanel:
    def __init__(self, widget):
        self.form = widget
        # The layout will be a grid
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Size Holder ----
        self.Size_Holder_Label = QtGui.QLabel("Size")
        self.ComboBox_Size_Holder = QtGui.QComboBox()
        # Type of Nut
        self.TextSizeHolder = ["8","11","14","17","23","34","42"]
        self.ComboBox_Size_Holder.addItems(self.TextSizeHolder)
        # Indicate inicial value in ComboBox
        self.ComboBox_Size_Holder.setCurrentIndex(self.TextSizeHolder.index('11'))

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Size_Holder_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Size_Holder,0,1,1,1)

        # ---- row 1: Rail Max High  ----
        # Label:
        self.motor_high_Label = QtGui.QLabel("Rail max High")
        # Spin Box that takes doubles
        self.motor_high_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.motor_high_Value.setValue(40)
        # suffix to indicate the units
        self.motor_high_Value.setSuffix(' mm')

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.motor_high_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.motor_high_Value,1,1,1,1)

        # ---- row 2: Thikness ----
        self.Thikness_Label = QtGui.QLabel("Thikness:")
        self.Thikness_Value = QtGui.QDoubleSpinBox()
        #Default value
        self.Thikness_Value.setValue(3)
        self.Thikness_Value.setMinimum(2)
        self.Thikness_Value.setSuffix(' mm')

        # row 2, column 0, rowspan 1, colspan 1        
        layout.addWidget(self.Thikness_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Thikness_Value,2,1,1,1)

    def accept(self):
        SizeHolder = {0:8, 1:11, 2:14, 3:17, 4:23, 5:34, 6:42}
        self.size_motor = SizeHolder[self.ComboBox_Size_Holder.currentIndex()]
        #Set_Select = self.ComboBox_Set.currentIndex()
        h_motor=self.motor_high_Value.value()
        Thikness = self.Thikness_Value.value()

        parts.NemaMotorHolder(nema_size = self.size_motor,
                             wall_thick = Thikness,
                             motor_thick = Thikness,
                             reinf_thick = Thikness,
                             motor_min_h =10.,
                             motor_max_h = h_motor,
                             rail = 1, # if there is a rail or not at the profile side
                             motor_xtr_space = 2., # counting on one side
                             motor_xtr_space_d = -1, # same as motor_xtr_space
                             bolt_wall_d = 4., # Metric of the wall bolts
                             bolt_wall_sep = 0., # optional   30
                             chmf_r = 1.,
                             fc_axis_h = VZ,
                             fc_axis_n = VX,
                             #fc_axis_p = VY,
                             ref_axis = 1, 
                             #ref_bolt = 0,
                             pos = V0,
                             wfco = 1,
                             name = 'nema_holder')

        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.Control.closeDialog() #close the dialog
        FreeCADGui.SendMsgToActiveView("ViewFit")
    
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()


###############################################################################
#*****************************Linear**Bear**House*****************************
class _LinBearHouse_Cmd:
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        Widget_LinBearHouse = QtGui.QWidget()
        Panel_LinBearHouse = LinBearHouseTaskPanel(Widget_LinBearHouse)
        FreeCADGui.Control.showDialog(Panel_LinBearHouse) 
        
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Linear Bear House',
            'Linear Bear House')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Linear Bear House',
            'Creates a Linear Bear House')
        return {
            'Pixmap': __dir__ + '/icons/Thin_Linear_Bear_House_1Rail_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class LinBearHouseTaskPanel:
    def __init__(self, widget):
        self.form = widget
        # The layout will be a grid
        layout = QtGui.QGridLayout(self.form)
        
        # ---- row 0: Version
        # Label: 
        self.LinBearHouse_Label = QtGui.QLabel("Select Bear House:")
        # Combo Box
        self.LinBearHouse_ComboBox = QtGui.QComboBox()
        # Values and initial
        self.LinBearHouse_text = ["Thin 1 rail", "Thin","Normal (only SC type)","Asimetric"]
        self.LinBearHouse_ComboBox.addItems(self.LinBearHouse_text)
        self.LinBearHouse_ComboBox.setCurrentIndex(0)

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.LinBearHouse_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.LinBearHouse_ComboBox,0,1,1,1)

        # ---- row 1: Type
        # Label: 
        self.Type_Label = QtGui.QLabel("Type:")
        # ComboBox
        self.Type_ComboBox = QtGui.QComboBox()
        # Values and initial
        self.Type_text = ["LMUU 6","LMUU 8","LMUU 10","LMUU 12","LMEUU 8","LMEUU 10","LMEUU12","LMELUU 12","SC8UU_Pr","SC10UU_Pr","SC12UU_Pr"]
        self.Type_ComboBox.addItems(self.Type_text)
        self.Type_ComboBox.setCurrentIndex(1)

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Type_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Type_ComboBox,1,1,1,1)

    def accept(self):
        Type_values = {0:kcomp.LM6UU,
                         1:kcomp.LM8UU,
                         2:kcomp.LM10UU,
                         3:kcomp.LM12UU,
                         4:kcomp.LME8UU,
                         5:kcomp.LME10UU,
                         6:kcomp.LME12UU,
                         7:kcomp.LME12LUU,
                         8:kcomp.SC8UU_Pr,
                         9:kcomp.SC10UU_Pr,
                         10:kcomp.SC12UU_Pr }

        LinBearHouse = self.LinBearHouse_ComboBox.currentIndex()
        Type = Type_values[self.Type_ComboBox.currentIndex()]
        if LinBearHouse == 0:
            parts.ThinLinBearHouse1rail(d_lbear = Type,
                                        fc_slide_axis = VX,
                                        fc_bot_axis =VZN,
                                        axis_center = 1,
                                        mid_center  = 1,
                                        pos = V0,
                                        name = 'thinlinbearhouse1rail')
        elif LinBearHouse == 1:
            parts.ThinLinBearHouse(d_lbear = Type,
                                fc_slide_axis = VX,
                                fc_bot_axis =VZN,
                                fc_perp_axis = V0,
                                axis_h = 0,
                                bolts_side = 1,
                                axis_center = 1,
                                mid_center  = 1,
                                bolt_center  = 0,
                                pos = V0,
                                name = 'thinlinbearhouse')
        elif LinBearHouse == 2:
            parts.LinBearHouse(d_lbearhousing = Type, #SC only
                               fc_slide_axis = VX,
                               fc_bot_axis =VZN,
                               axis_center = 1,
                               mid_center  = 1,
                               pos = V0,
                               name = 'linbearhouse')

        else:
            parts.ThinLinBearHouseAsim(d_lbear = Type,
                                       fc_fro_ax = VX,
                                       fc_bot_ax =VZN,
                                       fc_sid_ax = V0,
                                       axis_h = 0,
                                       bolts_side = 1,
                                       refcen_hei = 1,
                                       refcen_dep  = 1,
                                       refcen_wid  = 1,
                                       bolt2cen_wid_n = 0,
                                       bolt2cen_wid_p = 0,
                                       pos = V0,
                                       name = 'thinlinbearhouse_asim')


        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.Control.closeDialog() #close the dialog
        FreeCADGui.SendMsgToActiveView("ViewFit")

###############################################################################
#*********************************Stop**Holder*********************************
class _stop_holderCmd:
    def Activated(self):
        baseWidget = QtGui.QWidget()
        panel = stop_holderTaskPanel(baseWidget)
        FreeCADGui.Control.showDialog(panel)

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Stop Holder',
            'Stop Holder')
        ToolTip =QtCore.QT_TRANSLATE_NOOP(
            'Stop Holder',
            'Creates Stop Holder with set parametres')
        return {
            'Pixmap': __dir__ + '/icons/Stop_Holder.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class stop_holderTaskPanel:
    def __init__(self,widget):
        self.form = widget
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: width
        # Label:
        self.Width_Label = QtGui.QLabel("Width:")
        self.Width_Value = QtGui.QDoubleSpinBox()
        self.Width_Value.setValue(21)
        self.Width_Value.setSuffix("mm")

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Width_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Width_Value,0,1,1,1)

        # ---- row 1: height
        # Label:
        self.Heigth_Label = QtGui.QLabel("Heigth:")
        self.Heigth_Value = QtGui.QDoubleSpinBox()
        self.Heigth_Value.setValue(31)
        self.Heigth_Value.setSuffix("mm")

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Width_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Width_Value,1,1,1,1)

        # ---- row 2: Thikness
        # Label:
        self.Thickness_Label = QtGui.QLabel("Thickness:")
        self.Thickness_Value = QtGui.QDoubleSpinBox()
        self.Thickness_Value.setValue(4)
        self.Thickness_Value.setSuffix("mm")

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Thickness_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Thickness_Value,2,1,1,1)

        # ---- row 3: Metric Bolt
        # Label:
        self.Bolt_Label = QtGui.QLabel("Metric Bolt")
        # ComboBox
        self.Bolt_ComboBox = QtGui.QComboBox()
        # Type of Nut
        self.TextNutType = ["M3","M4","M5","M6"]
        self.Bolt_ComboBox.addItems(self.TextNutType)
        # Indicate inicial value in ComboBox
        self.Bolt_ComboBox.setCurrentIndex(self.TextNutType.index('M3'))

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Bolt_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Bolt_ComboBox,3,1,1,1)

        # ---- row 4: Rail
        # Label
        self.Rail_Label = QtGui.QLabel("Rail Size:")
        #ComboBox
        self.Rail_ComboBox = QtGui.QComboBox()
        self.Rail_ComboBox.addItems(["10mm","20mm","30mm"])
        self.Rail_ComboBox.setCurrentIndex(0)

        # row 4, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Rail_Label,4,0,1,1)
        # row 4, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Rail_ComboBox,4,1,1,1)        

        # ---- row 5: Reinforce
        # Label:
        self.Reinforce_Label = QtGui.QLabel("Reinforce:")
        # ComboBox
        self.Reinforce_ComboBox = QtGui.QComboBox()
        self.Reinforce_ComboBox.addItems(["No","Yes"])
        self.Reinforce_ComboBox.setCurrentIndex(1)

        # row 5, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Reinforce_Label,5,0,1,1)
        # row 5, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Reinforce_ComboBox,5,1,1,1)

    def accept(self):
        Width = self.Width_Value.value()
        Heigth = self.Heigth_Value.value()
        Thick = self.Thickness_Value.value()
        Bolt_values = {0: 3,
                       1: 4,
                       2: 5,
                       3: 6}
        Bolt = Bolt_values[self.Bolt_ComboBox.currentIndex()]
        Rail_values = {0: 10,
                       1: 20,
                       2: 30}
        Rail = Rail_values[self.Rail_ComboBox.currentIndex()]
        Reinforce_values = {0: 0, #No
                            1: 1}#Yes
        Reinforce = Reinforce_values[self.Reinforce_ComboBox.currentIndex()]

        parts.hallestop_holder(stp_w = Width,
                              stp_h = Heigth,
                              base_thick = Thick,
                              sup_thick = Thick,
                              bolt_base_d = Bolt, #metric of the bolt 
                              bolt_sup_d = Bolt, #metric of the bolt
                              bolt_sup_sep = 17.,  # fixed value
                              alu_rail_l = Rail,
                              stp_rail_l = Rail,
                              xtr_bolt_head = 3,
                              xtr_bolt_head_d = 0,
                              reinforce = Reinforce,
                              base_min_dist = 1,
                              fc_perp_ax = VZ,
                              fc_lin_ax = VX,
                              pos = V0,
                              wfco=1,
                              name = 'stop_holder')

        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.Control.closeDialog() #close the dialog
        
###############################################################################
#********************************Filter***Stage********************************
class _FilterStageCmd:
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        baseWidget = QtGui.QWidget()
        panel = FilterStageTaskPanel(baseWidget)
        # having a panel with a widget in self.form and the accept and 
        # reject functions (if needed), we can open it:
        FreeCADGui.Control.showDialog(panel)

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Filter_Stage_',
            'Filter Stage')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Filter_Stage',
            'Creates a Filter Stage with set parametres')
        return {
            'Pixmap': __dir__ + '/icons/Filter_Stage_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

class FilterStageTaskPanel:                                    
    def __init__(self,widget):
        self.form = widget
        # The layout will be a grid, since the form is an argument
        # we dont need this statement afterwards: self.form.setLayout(layout)
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Move distance
        # Label:
        self.move_l_Label = QtGui.QLabel("Move distance:")
        # Spin Box that takes doubles
        self.move_l_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.move_l_Value.setValue(60)
        # suffix to indicate the units
        self.move_l_Value.setSuffix(' mm')

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.move_l_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.move_l_Value,0,1,1,1)

        # ---- row 1: Filter Length ----
        # Label:
        self.Filter_Length_Label = QtGui.QLabel("Filter Length")
        # Spin Box that takes doubles
        self.Filter_Length_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Filter_Length_Value.setValue(60)
        # suffix to indicate the units
        self.Filter_Length_Value.setSuffix(' mm')

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Length_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Length_Value,1,1,1,1)

        # ---- row 2: Filter Width ----
        # Label:
        self.Filter_Width_Label = QtGui.QLabel("Filter Width")
        # Spin Box that takes doubles
        self.Filter_Width_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Filter_Width_Value.setValue(25)
        # suffix to indicate the units
        self.Filter_Width_Value.setSuffix(' mm')

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Width_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Width_Value,2,1,1,1)

        # ---- row 3: Base width
        # Label:
        self.base_w_Label = QtGui.QLabel("Base width:")  #10/15/20/30/40
        # Spin Box that takes doubles
        self.ComboBox_base_w = QtGui.QComboBox()
        # Diferents base
        self.TextBase_W = ["10mm","15mm","20mm","30mm","40mm"] 
        self.ComboBox_base_w.addItems(self.TextBase_W)
        self.ComboBox_base_w.setCurrentIndex(self.TextBase_W.index('20mm'))

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.base_w_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_base_w,3,1,1,1)
                
        # ---- row 4: Tensioner Stroke
         # Label:
        self.tens_stroke_Label = QtGui.QLabel("Tensioner stroke:")
        # Spin Box that takes doubles
        self.tens_stroke_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.tens_stroke_Value.setValue(20)
        # suffix to indicate the units
        self.tens_stroke_Value.setSuffix(' mm')

        # row 4, column 0, rowspan 1, colspan 1
        layout.addWidget(self.tens_stroke_Label,4,0,1,1)
        # row 4, column 1, rowspan 1, colspan 1
        layout.addWidget(self.tens_stroke_Value,4,1,1,1)

        # ---- row 5: Wall thick
        # Label:
        self.wall_th_Label = QtGui.QLabel("Wall thick:")
        # Spin Box that takes doubles
        self.wall_th_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.wall_th_Value.setValue(3)
        # suffix to indicate the units
        self.wall_th_Value.setSuffix(' mm')

        # row 5, column 0, rowspan 1, colspan 1
        layout.addWidget(self.wall_th_Label,5,0,1,1)
        # row 5, column 1, rowspan 1, colspan 1
        layout.addWidget(self.wall_th_Value,5,1,1,1)

        # ---- row 6: Nut Type
        #Label:
        self.nut_hole_Label = QtGui.QLabel("Nut Type:")   

        # Combo Box that have multiple choice
        self.ComboBox_Nut_Hole = QtGui.QComboBox()
        # Type of Nut
        self.TextNutType = ["M3","M4","M5","M6"]
        self.ComboBox_Nut_Hole.addItems(self.TextNutType)
        # Indicate inicial value in ComboBox
        self.ComboBox_Nut_Hole.setCurrentIndex(self.TextNutType.index('M3'))

        # row 6, column 0, rowspan 1, colspan 1
        layout.addWidget(self.nut_hole_Label,6,0,1,1)
        # row 6, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Nut_Hole,6,1,1,1)

        # ---- row 7: Size Holder ----
        self.Size_Holder_Label = QtGui.QLabel("Motor size")
        self.ComboBox_Size_Holder = QtGui.QComboBox()
        # Type of Nut
        self.TextSizeHolder = ["8","11","14","17","23","34","42"]
        self.ComboBox_Size_Holder.addItems(self.TextSizeHolder)
        # Indicate inicial value in ComboBox
        self.ComboBox_Size_Holder.setCurrentIndex(self.TextSizeHolder.index('14'))

        # row 7, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Size_Holder_Label,7,0,1,1)
        # row 7, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Size_Holder,7,1,1,1)

        # ---- row 8: Rail Max High  ----
        # Label:
        self.motor_high_Label = QtGui.QLabel("Rail high Motor holder")
        # Spin Box that takes doubles
        self.motor_high_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.motor_high_Value.setValue(25) #Value printed
        # suffix to indicate the units
        self.motor_high_Value.setSuffix(' mm')

        # row 8, column 0, rowspan 1, colspan 1
        layout.addWidget(self.motor_high_Label,8,0,1,1)
        # row 8, column 1, rowspan 1, colspan 1
        layout.addWidget(self.motor_high_Value,8,1,1,1)

        # ---- row 9: Thikness ----
        self.Thikness_Label = QtGui.QLabel("Motor holder thikness:")
        self.Thikness_Value = QtGui.QDoubleSpinBox()
        #Default value
        self.Thikness_Value.setValue(3)
        self.Thikness_Value.setMinimum(2)
        self.Thikness_Value.setSuffix(' mm')

        # row 9, column 0, rowspan 1, colspan 1        
        layout.addWidget(self.Thikness_Label,9,0,1,1)
        # row 9, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Thikness_Value,9,1,1,1)


    # Ok and Cancel buttons are created by default in FreeCAD Task Panels
    # What is done when we click on the ok button.

    def accept(self):
        self.selec_base = {0: 5, 1: 10, 2: 15, 3: 20, 4: 30, 5: 40}
        move_l = self.move_l_Value.value()
        #Filter holder
        Filter_Length = self.Filter_Length_Value.value()
        Filter_Width = self.Filter_Width_Value.value()
        #tensioner
        nut_hole = 3 + self.ComboBox_Nut_Hole.currentIndex()  #Index star in 0, first value = 3
        tens_stroke = self.tens_stroke_Value.value()
        base_w = self.selec_base[self.ComboBox_base_w.currentIndex()]
        wall_thick = self.wall_th_Value.value()
        #motor holder
        SizeHolder = {0:8, 1:11, 2:14, 3:17, 4:23, 5:34, 6:42}
        size_motor = SizeHolder[self.ComboBox_Size_Holder.currentIndex()]
        h_motor=self.motor_high_Value.value()
        thik_motor = self.Thikness_Value.value()

        filter_stage_fun(move_l,Filter_Length,Filter_Width, nut_hole, tens_stroke, base_w, wall_thick, size_motor, h_motor, thik_motor)
            #pulley_h => belt_pos_h
            #nut_hole => bolttens_mtr
            #tens_stroke => tens_stroke_Var
            #base_w => aluprof_w
            #wall_thick => wall_thick_Var
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.Control.closeDialog() #close the dialog

###############################################################################
#********************************Filter**Holder********************************
class _FilterHolderCmd:
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        Widget_FilterHolder = QtGui.QWidget()
        Panel_FilterHolder = FilterHolderTaskPanel(Widget_FilterHolder)
        FreeCADGui.Control.showDialog(Panel_FilterHolder) 

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Filter Holder',
            'Filter Holder')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Creates a Filter Holder')
        return {
            'Pixmap': __dir__ + '/icons/Filter_Holder_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class FilterHolderTaskPanel:
    def __init__(self, widget):
        self.form = widget
        # The layout will be a grid
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Filter Lenth ----
        # Label:
        self.Filter_Length_Label = QtGui.QLabel("Filter Length")
        # Spin Box that takes doubles
        self.Filter_Length_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Filter_Length_Value.setValue(60)
        # suffix to indicate the units
        self.Filter_Length_Value.setSuffix(' mm')

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Length_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Length_Value,0,1,1,1)

        # ---- row 1: Filter Width ----
        # Label:
        self.Filter_Width_Label = QtGui.QLabel("Filter Width")
        # Spin Box that takes doubles
        self.Filter_Width_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Filter_Width_Value.setValue(25)
        # suffix to indicate the units
        self.Filter_Width_Value.setSuffix(' mm')

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Width_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Filter_Width_Value,1,1,1,1)


    def accept(self):
        Filter_Length = self.Filter_Length_Value.value()
        Filter_Width = self.Filter_Width_Value.value()

        filter_holder_clss.PartFilterHolder(filter_l = Filter_Length, #60     #########################################################################
                                            filter_w = Filter_Width, #25
                                            filter_t = 2.5,
                                            base_h = 6.,
                                            hold_d = 10.,
                                            filt_supp_in = 2.,
                                            filt_rim = 3.,
                                            filt_cen_d = 30,
                                            fillet_r = 1.,
                                            # linear guides SEBLV16 y SEBS15, y MGN12H:
                                            boltcol1_dist = 20/2.,
                                            boltcol2_dist = 12.5, #thorlabs breadboard distance
                                            boltcol3_dist = 25,
                                            boltrow1_h = 0,
                                            boltrow1_2_dist = 12.5,
                                            # linear guide MGN12H
                                            boltrow1_3_dist = 20.,
                                            # linear guide SEBLV16 and SEBS15
                                            boltrow1_4_dist = 25.,

                                            bolt_cen_mtr = 4, 
                                            bolt_linguide_mtr = 3, # linear guide bolts 

                                            beltclamp_t = 3.,
                                            beltclamp_l = 12.,
                                            beltclamp_h = 8.,
                                            clamp_post_dist = 4.,
                                            sm_beltpost_r = 1.,

                                            tol = kcomp.TOL,
                                            axis_d = VX,
                                            axis_w = VY,
                                            axis_h = VZ,
                                            pos_d = 0,
                                            pos_w = 0,
                                            pos_h = 0,
                                            pos = V0,
                                            model_type = 0, # exact
                                            name = 'filter_holder')
        
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.Control.closeDialog() #close the dialog
    
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()

###############################################################################
#**********************************Tensioner***********************************
class _TensionerCmd:
    
    def Activated(self):
        # what is done when the command is clicked
        # creates a panel with a dialog
        Widget_Tensioner = QtGui.QWidget()
        Panel_Tensioner = TensionerTaskPanel(Widget_Tensioner)
        FreeCADGui.Control.showDialog(Panel_Tensioner) 
        

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Tensioner',
            'Tensioner')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Tensioner',
            'Creates a Tensioner')
        return {
            'Pixmap': __dir__ + '/icons/Tensioner_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None

class TensionerTaskPanel:
    def __init__(self, widget):
        self.form = widget
        # The layout will be a grid
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Belt High ----
        # Label:
        self.belt_h_Label = QtGui.QLabel("Belt hight:")
        # Spin Box that takes doubles
        self.belt_h_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.belt_h_Value.setValue(20)
        # suffix to indicate the units
        self.belt_h_Value.setSuffix(' mm')

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.belt_h_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.belt_h_Value,0,1,1,1)

        # ---- row 1: Base width ----
        # Label:
        self.base_w_Label = QtGui.QLabel("Base width:")  #10/15/20/30/40
        # Spin Box that takes doubles
        self.ComboBox_base_w = QtGui.QComboBox()
        # Diferents base
        self.TextBase_W = ["10mm","15mm","20mm","30mm","40mm"] 
        self.ComboBox_base_w.addItems(self.TextBase_W)
        self.ComboBox_base_w.setCurrentIndex(self.TextBase_W.index('20mm'))

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.base_w_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_base_w,1,1,1,1)
                
        # ---- row 2: Tensioner Stroke ----
         # Label:
        self.tens_stroke_Label = QtGui.QLabel("Tensioner stroke:")
        # Spin Box that takes doubles
        self.tens_stroke_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.tens_stroke_Value.setValue(20)
        # suffix to indicate the units
        self.tens_stroke_Value.setSuffix(' mm')

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.tens_stroke_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.tens_stroke_Value,2,1,1,1)

        # ---- row 3: Wall thick ----
        # Label:
        self.wall_th_Label = QtGui.QLabel("Wall thick:")
        # Spin Box that takes doubles
        self.wall_th_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.wall_th_Value.setValue(3)
        # suffix to indicate the units
        self.wall_th_Value.setSuffix(' mm')

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.wall_th_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.wall_th_Value,3,1,1,1)

        # ---- row 4: Nut Type ----
        #Label:
        self.nut_hole_Label = QtGui.QLabel("Nut Type:")   

        # Combo Box that have multiple choice
        self.ComboBox_Nut_Hole = QtGui.QComboBox()
        # Type of Nut
        self.TextNutType = ["M3","M4","M5","M6"]
        self.ComboBox_Nut_Hole.addItems(self.TextNutType)
        # Indicate inicial value in ComboBox
        self.ComboBox_Nut_Hole.setCurrentIndex(self.TextNutType.index('M3'))

        # row 4, column 0, rowspan 1, colspan 1
        layout.addWidget(self.nut_hole_Label,4,0,1,1)
        # row 4, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Nut_Hole,4,1,1,1)

        # ---- row 5: Set Holder ----
        self.Set_Label = QtGui.QLabel("See Set")
        self.ComboBox_Set = QtGui.QComboBox()
        # Type for ComboBox
        self.TextSet = ["No","Yes"]
        self.ComboBox_Set.addItems(self.TextSet)
        # Indicate inicial value in ComboBox
        self.ComboBox_Set.setCurrentIndex(self.TextSet.index('No'))

        # row 5, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Set_Label,5,0,1,1)
        # row 5, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Set,5,1,1,1)

    def accept(self):
        IndexNut = {0:3,1:4,2:5,3:6}
        IndexBase = {0: 10, 1: 15, 2: 20, 3: 30, 4: 40}
        tensioner_belt_h = self.belt_h_Value.value()
        nut_hole = IndexNut[self.ComboBox_Nut_Hole.currentIndex()]
        tens_stroke = self.tens_stroke_Value.value()
        base_w = IndexBase[self.ComboBox_base_w.currentIndex()]
        wall_thick = self.wall_th_Value.value()
        Set_Select = self.ComboBox_Set.currentIndex()

        tensioner_clss.TensionerSet(aluprof_w = base_w,#20.,
                                    belt_pos_h = tensioner_belt_h, 
                                    hold_bas_h = 0,
                                    hold_hole_2sides = 1,
                                    boltidler_mtr = 3,
                                    bolttens_mtr = nut_hole,   #métrica del tensor
                                    boltaluprof_mtr = nut_hole,
                                    tens_stroke = tens_stroke ,
                                    wall_thick = wall_thick,
                                    in_fillet = 2.,
                                    pulley_stroke_dist = 0,
                                    nut_holder_thick = nut_hole ,   
                                    opt_tens_chmf = 0,
                                    min_width = 0,
                                    tol = kcomp.TOL,
                                    axis_d = VY.negative(),
                                    axis_w = VX.negative(),
                                    axis_h = VZ,
                                    pos_d = 0.,
                                    pos_w = 0.,
                                    pos_h = 0.,
                                    pos = V0,
                                    name = 'tensioner_set')
        
        if Set_Select == 0: #work only for tens_stroke = 20
            FreeCAD.ActiveDocument.removeObject("bearing_idlpulley_m3")
            FreeCAD.ActiveDocument.removeObject("idlpull_bearing")
            FreeCAD.ActiveDocument.removeObject("idlpull_rwash_bt")
            FreeCAD.ActiveDocument.removeObject("idlpull_lwash_bt")
            FreeCAD.ActiveDocument.removeObject("idlpull_rwash_tp")
            FreeCAD.ActiveDocument.removeObject("idlpull_lwash_tp")
            FreeCAD.ActiveDocument.removeObject("d912bolt_washer_m3")
            FreeCAD.ActiveDocument.removeObject("din125_washer_m3")  
            FreeCAD.ActiveDocument.removeObject("leadscrew_nut")
            FreeCAD.ActiveDocument.removeObject("d9343")
            FreeCAD.ActiveDocument.removeObject("d934nut_m3")
            FreeCAD.ActiveDocument.removeObject("d912bolt_m3_l20")
            if nut_hole == 3:
                FreeCAD.ActiveDocument.removeObject("din125_washer_m3001")
                FreeCAD.ActiveDocument.removeObject("d912bolt_m3_l30")
                FreeCAD.ActiveDocument.removeObject("d912bolt_washer_m"  + str(int(nut_hole)) + "001")
                FreeCAD.ActiveDocument.removeObject("din125_washer_m" + str(int(nut_hole)) + "002")  
            elif nut_hole == 4:
                FreeCAD.ActiveDocument.removeObject("din125_washer_m3001")
                FreeCAD.ActiveDocument.removeObject("d912bolt_m4_l35")
                FreeCAD.ActiveDocument.removeObject("din125_washer_m4")
                FreeCAD.ActiveDocument.removeObject("d912bolt_washer_m4")
            elif nut_hole == 5:  
                FreeCAD.ActiveDocument.removeObject("din125_washer_m3001")
                FreeCAD.ActiveDocument.removeObject("d912bolt_m5_l40")
                FreeCAD.ActiveDocument.removeObject("din125_washer_m5")
                FreeCAD.ActiveDocument.removeObject("d912bolt_washer_m5")
            else: 
                FreeCAD.ActiveDocument.removeObject("din125_washer_m3001")
                FreeCAD.ActiveDocument.removeObject("d912bolt_m6_l40")
                FreeCAD.ActiveDocument.removeObject("din125_washer_m6")
                FreeCAD.ActiveDocument.removeObject("d912bolt_washer_m6")

        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.Control.closeDialog() #close the dialog
    
    #def reject(self):
    #   FreeCADGui.Control.closeDialog()


###############################################################################
#*********************************Belt***Clamp*********************************
class _BeltClampCmd:
    def Activated(self):
        Widget_BeltClamp = QtGui.QWidget()
        Panel_BeltClamp = BeltClampTaskPanel(Widget_BeltClamp)
        FreeCADGui.Control.showDialog(Panel_BeltClamp)     
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Belt clamp')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Creates a belt clamp')
        return {
            'Pixmap': __dir__ + '/icons/Double_Belt_Clamp_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None 

class BeltClampTaskPanel:
    def __init__(self, widget):
        self.form = widget
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Type ----
        #Label:
        self.Type_Label = QtGui.QLabel("Type:")   

        # Combo Box that have multiple choice
        self.Type_ComboBox = QtGui.QComboBox()
        # Type of Nut
        self.TextType = ["Simple","Double"]
        self.Type_ComboBox.addItems(self.TextType)
        # Indicate inicial value in ComboBox
        self.Type_ComboBox.setCurrentIndex(0)

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Type_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Type_ComboBox,0,1,1,1)

        # ---- row 1: Length ----
        # Label:
        self.Length_Label = QtGui.QLabel("Length:")
        # Spin Box that takes doubles
        self.Length_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Length_Value.setValue(42)
        # suffix to indicate the units
        self.Length_Value.setSuffix(' mm')
        self.Length_Value.setMinimum(42)

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Length_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Length_Value,1,1,1,1)

        # ---- row 2: Width ----
        # Label:
        self.Width_Label = QtGui.QLabel("Width:")
        # Spin Box that takes doubles
        self.Width_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Width_Value.setValue(10.8)
        # suffix to indicate the units
        self.Width_Value.setSuffix(' mm')
        self.Width_Value.setMinimum(10.8)

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Width_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Width_Value,2,1,1,1)

        # ---- row 3: Nut Type ----
        #Label:
        self.nut_hole_Label = QtGui.QLabel("Nut Type:")   

        # Combo Box that have multiple choice
        self.ComboBox_Nut_Hole = QtGui.QComboBox()
        # Type of Nut
        self.TextNutType = ["M3","M4","M5","M6"]
        self.ComboBox_Nut_Hole.addItems(self.TextNutType)
        # Indicate inicial value in ComboBox
        self.ComboBox_Nut_Hole.setCurrentIndex(self.TextNutType.index('M3'))

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.nut_hole_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.ComboBox_Nut_Hole,3,1,1,1)

    def accept(self):
        Type = self.Type_ComboBox.currentIndex()
        Length = self.Length_Value.value()
        Width = self.Width_Value.value()
        IndexNut = {0 : 3,
                    1 : 4,
                    2 : 5,
                    3 : 6}
        nut_hole = IndexNut[self.ComboBox_Nut_Hole.currentIndex()]

        if Type == 0:
            beltcl.BeltClamp(fc_fro_ax = VX,
                             fc_top_ax = VZ,
                             base_h = 2,
                             base_l = Length,
                             base_w = Width,
                             bolt_d = nut_hole,
                             bolt_csunk = 0,
                             ref = 1,
                             pos = V0,
                             extra=1,
                             wfco = 1,
                             intol = 0,
                             name = 'belt_clamp' )
        elif Type == 1:
            beltcl.DoubleBeltClamp(axis_h = VZ,
                                axis_d = VX,
                                axis_w = VY,
                                base_h = 2,
                                base_l = Length,
                                base_w = Width,
                                bolt_d = nut_hole,
                                bolt_csunk = 0,
                                ref = 1,
                                pos = V0,
                                extra=1,
                                wfco = 1,
                                intol = 0,
                                name = 'double_belt_clamp' )
        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.Control.closeDialog() #close the dialog
        FreeCADGui.SendMsgToActiveView("ViewFit")


###############################################################################
#********************************SENSOR**HOLDER********************************
class _SensorHolderCmd:
    def Activated(self):
        Widget_SensorHolder = QtGui.QWidget()
        Panel_SensorHolder = SensorHolderTaskPanel(Widget_SensorHolder)
        FreeCADGui.Control.showDialog(Panel_SensorHolder)     
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Sensor Holder')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Creates a sensor holder')
        return {
            'Pixmap': __dir__ + '/icons/Sensor_holder_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None 

class SensorHolderTaskPanel:
    def __init__(self, widget):
        self.form = widget
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Sensor Pin Length ----
        #Label:
        self.Sensor_Pin_Length_Label = QtGui.QLabel("Sensor Pin Length:")  
        # Spin Box that takes doubles
        self.Sensor_Pin_Length_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Sensor_Pin_Length_Value.setValue(10)
        # suffix to indicate the units
        self.Sensor_Pin_Length_Value.setSuffix(' mm')
        self.Sensor_Pin_Length_Value.setMinimum(10) #Not sure

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Sensor_Pin_Length_Label,0,0,1,1)
        # row 0, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Sensor_Pin_Length_Value,0,1,1,1)

        # ---- row 1: Sensor Pin Width ----
        #Label:
        self.Sensor_Pin_Width_Label = QtGui.QLabel("Sensor Pin Width:")  
        # Spin Box that takes doubles
        self.Sensor_Pin_Width_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Sensor_Pin_Width_Value.setValue(2)
        # suffix to indicate the units
        self.Sensor_Pin_Width_Value.setSuffix(' mm')
        self.Sensor_Pin_Width_Value.setMinimum(2) #Not sure

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Sensor_Pin_Width_Label,1,0,1,1)
        # row 1, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Sensor_Pin_Width_Value,1,1,1,1)

        # ---- row 2: Sensor Pin High ----
        #Label:
        self.Sensor_Pin_High_Label = QtGui.QLabel("Sensor Pin High:")  
        # Spin Box that takes doubles
        self.Sensor_Pin_High_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Sensor_Pin_High_Value.setValue(3)
        # suffix to indicate the units
        self.Sensor_Pin_High_Value.setSuffix(' mm')
        self.Sensor_Pin_High_Value.setMinimum(3) #Not sure

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Sensor_Pin_High_Label,2,0,1,1)
        # row 2, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Sensor_Pin_High_Value,2,1,1,1)

        # ---- row 3: Depth ----
        #Label:
        self.Depth_CD_Label = QtGui.QLabel("Depth:")  
        # Spin Box that takes doubles
        self.Depth_CD_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Depth_CD_Value.setValue(8)
        # suffix to indicate the units
        self.Depth_CD_Value.setSuffix(' mm')
        self.Depth_CD_Value.setMinimum(8) #Not sure

        # row 3, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Depth_CD_Label,3,0,1,1)
        # row 3, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Depth_CD_Value,3,1,1,1)

        # ---- row 4: Width CD case----
        #Label:
        self.Width_CD_Label = QtGui.QLabel("Width CD case:")  
        # Spin Box that takes doubles
        self.Width_CD_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.Width_CD_Value.setValue(20)
        # suffix to indicate the units
        self.Width_CD_Value.setSuffix(' mm')
        self.Width_CD_Value.setMinimum(20) #Not sure

        # row 4, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Width_CD_Label,4,0,1,1)
        # row 4, column 1, rowspan 1, colspan 1
        layout.addWidget(self.Width_CD_Value,4,1,1,1)

        # ---- row 5: High CD case----
        #Label:
        self.High_CD_Label = QtGui.QLabel("High CD case:")  
        # Spin Box that takes doubles
        self.High_CD_Value = QtGui.QDoubleSpinBox()
        # Default value
        self.High_CD_Value.setValue(37)
        # suffix to indicate the units
        self.High_CD_Value.setSuffix(' mm')
        self.High_CD_Value.setMinimum(37) #Not sure

        # row 5, column 0, rowspan 1, colspan 1
        layout.addWidget(self.High_CD_Label,5,0,1,1)
        # row 5, column 1, rowspan 1, colspan 1
        layout.addWidget(self.High_CD_Value,5,1,1,1)

    def accept(self):
        Sensor_Pin_Lenght = self.Sensor_Pin_Length_Value.value()
        Sensor_Pin_Width = self.Sensor_Pin_Width_Value.value()
        Sensor_Pin_High = self.Sensor_Pin_High_Value.value()
        Depth_CD = self.Depth_CD_Value.value()
        Width_CD = self.Width_CD_Value.value()
        High_CD = self.High_CD_Value.value()

        parts.sensor_holder(sensor_support_length = Sensor_Pin_Lenght,
                            sensor_pin_sep = 2.54,
                            sensor_pin_pos_h = Sensor_Pin_High,
                            sensor_pin_pos_w = Sensor_Pin_Width,
                            sensor_pin_r_tol = 1.05,
                            sensor_pin_rows = 6,
                            sensor_pin_cols = 6,
                            #sensor_clip_pos_h = 2.45, #position from center
                            #sensor_clip_h_tol = 1.28,
                            #sensor_clip_w_tol = 1.,
                            base_height = High_CD, # height of the cd case
                            base_width = Width_CD, # width of the cd case
                            flap_depth = Depth_CD,
                            flap_thick = 2.,
                            base_thick = 2., #la altura
                            basesensor_thick = 9., #la altura de la parte de los sensores
                            pos =V0,
                            axis_h = VZ,
                            axis_d = VX,
                            axis_w = VY,
                            wfco=1,
                            name = 'sensorholder')

        FreeCADGui.activeDocument().activeView().viewAxonometric()
        FreeCADGui.Control.closeDialog() #close the dialog
        FreeCADGui.SendMsgToActiveView("ViewFit")

###############################################################################
#******************************PRINT**AND**EXPORT******************************
class _ChangePosExportCmd:
    def Activated(self):
        objSelect = FreeCADGui.Selection.getSelection()[0]#.Name
        print_export(objSelect)
        
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Change Pos and Export',
            'Change Pos and Export')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            'Object selected changes to print position and it is exported in .stl')
        return {
            'Pixmap': __dir__ + '/icons/Print_Export_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None 

###############################################################################
#***********************************ASSEMBLY***********************************
class _AssemlyCmd:
    """
    This utility change the position of the component that has been selected and set up in the second component you have selected.
    Shape has:
        - Vertexes
        - Edges
        - Faces
        - Solids
    
    """
    def Activated(self):
        baseWidget = QtGui.QWidget()
        panel_Assembly = Assembly_TaskPanel(baseWidget)
        FreeCADGui.Control.showDialog(panel_Assembly) 
        """
        message = QtGui.QMessageBox()
        message.setText('Select:\n  - First: Think to move.\n   - Second: New placement.\n')
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.setDefaultButton(QtGui.QMessageBox.Ok)
        message.exec_()"""
        
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Assembly',
            'Assembly')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            '',
            '')
        return {
            'Pixmap': __dir__ + '/icons/Assembly_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}
    def IsActive(self):
        return not FreeCAD.ActiveDocument is None 
    
class Assembly_TaskPanel:
    def __init__(self, widget):
        self.form = widget
        layout = QtGui.QGridLayout(self.form)

        # ---- row 0: Text ----
        #Label:
        self.Text_1_Label = QtGui.QLabel("1 - Select object to move")  

        # row 0, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Text_1_Label,0,0,1,1)

        """# ---- row 1: Text ----
        #Label:
        self.Text_2_Label = QtGui.QLabel(" ")  

        # row 1, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Text_2_Label,1,0,1,1)
        """
        # ---- row 2: Text ----
        #Label:
        self.Text_3_Label = QtGui.QLabel("2 - After select the place")  

        # row 2, column 0, rowspan 1, colspan 1
        layout.addWidget(self.Text_3_Label,1,0,1,1)

    def accept(self):
        if len(FreeCADGui.Selection.getSelection()) == 2 :
            grafic.grafic()
            FreeCADGui.Control.closeDialog() #close the dialog
        else:
            message = QtGui.QMessageBox()
            message.setText('Select object to move and placement')
            message.setStandardButtons(QtGui.QMessageBox.Ok)
            message.setDefaultButton(QtGui.QMessageBox.Ok)
            message.exec_()

###############################################################################
#***********************************COMMANDS***********************************
FreeCADGui.addCommand('Sk',_Sk_Dir_Cmd())
FreeCADGui.addCommand('Idle_Pulley_Holder',_IdlePulleyHolder_Cmd())
FreeCADGui.addCommand('Aluprof_Bracket',_AluprofBracket_Cmd())
FreeCADGui.addCommand('Motor_Holder',_MotorHolderCmd())
FreeCADGui.addCommand('Simple_End_Stop_Holder',_SimpleEndStopHolder_Cmd())
FreeCADGui.addCommand('LinBearHouse',_LinBearHouse_Cmd())
FreeCADGui.addCommand('Stop_Holder',_stop_holderCmd())
FreeCADGui.addCommand('Sensor_Holder',_SensorHolderCmd())

## Filter Stage
FreeCADGui.addCommand('Filter_Stage', _FilterStageCmd())
FreeCADGui.addCommand('Filter_Holder',_FilterHolderCmd())
FreeCADGui.addCommand('Tensioner',_TensionerCmd())

## In progress
FreeCADGui.addCommand('Belt_Clamp',_BeltClampCmd())

## Print
FreeCADGui.addCommand('ChangePosExport',_ChangePosExportCmd())

## Assembly
FreeCADGui.addCommand('Assembly',_AssemlyCmd())