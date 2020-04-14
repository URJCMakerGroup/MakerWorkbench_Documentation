# -*- coding: utf-8 -*-
# FreeCAD init script of the Filter Stage module,

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

class MechatronicWorkbench (Workbench):
    """Mechatronic Wokbench to create objects"""
    #Icon in XPM 16x16
    Icon = """
    /* XPM */
    static char * Filter_Stage_xpm[] = {
    "16 16 5 1",
    " 	c None",
    ".	c #FFFFFF",
    "+	c #000000",
    "@	c #7F4F00",
    "#	c #FFBF00",
    "................",
    "...++++++++++++.",
    "..+@#########++.",
    ".+@#########+@+.",
    ".+++++++++++@#+.",
    ".+#########+##+.",
    ".+#++###++#+##+.",
    ".+#+#+#+#+#+##+.",
    ".+#+##+##+#+##+.",
    ".+#+#####+#+##+.",
    ".+#+#####+#+##+.",
    ".+#+#####+#+##+.",
    ".+#+#####+#+#@+.",
    ".+#########+@+..",
    ".++++++++++++...",
    "................"};
    """
    MenuText = "Mechatronic"
    ToolTip = "Mechatronic Workbench"

    def Initialize(self):
        from PySide import QtCore, QtGui
        import MechatronicGui
        
        # +-------------------------------+
        # |                               |
        # |   List of mechanical models   |
        # |                               |
        # +-------------------------------+

        partsList = ["Sk",
                     "Idle_Pulley_Holder",
                     "Aluprof_Bracket",
                     "Motor_Holder",
                     "Motor",
                     "Simple_End_Stop_Holder",
                     "LinBearHouse",
                     "Stop_Holder",
                     "Filter_Holder",
                     "Tensioner",
                     "Belt_Clamp",
                    #  "Belt_Clamped", # Not working properly
                     "Sensor_Holder",
                     "Aluproft",
                     "Linear_Guide_Block",
                     "Bolts, Nuts & Washers"]

        # +-------------------------------+
        # |                               |
        # |   List of optic models        |
        # |                               |
        # +-------------------------------+    

        opticList = ["TubeLense",
                     "LCB1M_Base",
                     "Plate",
                     "CageCube",
                     "ThLed30",
                     "PrizLed",
                     "BreadBoard"]

        # +-------------------------------+
        # |                               |
        # |   List of systems             |
        # |                               |
        # +-------------------------------+

        sysList = ["Filter_Stage"]

        # +-------------------------------+
        # |                               |
        # |   List of functions           |
        # |                               |
        # +-------------------------------+

        modList = ["ChangePosExport",
                   "Assembly"]

        # +-------------------------------+
        # |                               |
        # |   Add ToolBars                |
        # |                               |
        # +-------------------------------+

        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Mechatronic", "Parts")), partsList)
        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Mechatronic", "Systems")), sysList)
        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Mechatronic", "Functions")), modList)
        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Mechatronic", "Optic")), opticList)

        # +-------------------------------+
        # |                               |
        # |   Add Menus                   |
        # |                               |
        # +-------------------------------+


        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Mechatronic", "Parts")), partsList)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Mechatronic", "Systems")), sysList)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Mechatronic", "Functions")), modList)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Mechatronic", "Optic")), opticList)
        
        Log ('Loalding Mechatronic Workbench... done! \n')
    
    def GetClassName(self):
        return "Gui::PythonWorkbench"
    
#Add workbench
Gui.addWorkbench(MechatronicWorkbench())