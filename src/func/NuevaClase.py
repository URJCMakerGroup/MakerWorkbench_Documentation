import FreeCAD
import Part
import DraftVecUtils

import os
import sys
import math
import inspect
import logging

import fcfun
import kcomp

from fcfun import V0, VX, VY, VZ, V0ROT
from fcfun import VXN, VYN, VZN

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Obj3D (object):
    """ This is the the basic class, that provides reference axes and 
    methods to get positions

    It is the parent class of other classes, no instantiation of this class

    These objects have their own coordinate axes:

    * axis_d: depth
    * axis_w: width
    * axis_h: height

    They have an origin point pos_o (created in a child class)
    and have different interesting points:

    * d_o
    * w_o
    * h_o

    and methods to get to them::

        pos_o_adjustment: FreeCAD.Vector
            if not V0 indicates that shape has not been placed at pos_o, so the FreeCAD object
            will need to be placed at pos_o_adjust

    This object could be a FreeCAD Object or not::

        fco: FreeCAD Object
            fco = 1 create FreeCAD Object
            fco = 0 not FreeCAD Object
            
    """
    def __init__(self, axis_d = None, axis_w = None, axis_h = None, name = None):
        """
        :param axis_d: Vector depth
        :param axis_w: Vector width
        :param axis_h: Vector height
        :param name: Name of the object
        :type axis_d: FreeCAD.Vector
        :type axis_w: FreeCAD.Vector
        :type axis_h: FreeCAD.Vector
        :type name: str
        """
        # the TopoShape has an origin, and distance vectors from it to 
        # the different points along the coordinate system  
        self.d_o = {}  # along axis_d
        self.w_o = {}  # along axis_w
        self.h_o = {}  # along axis_h

        self.dict_child = {} # dict of child 
        self.dict_child_sum = {} # dict of child add
        self.dict_child_res = {} # dict of child remove

        self.name = name

        self.doc = FreeCAD.ActiveDocument

        if axis_h is not None:
            axis_h = DraftVecUtils.scaleTo(axis_h,1)
        else:
            self.h_o[0] = V0
            self.pos_h = 0
            axis_h = V0
        self.axis_h = axis_h

        if axis_d is not None:
            axis_d = DraftVecUtils.scaleTo(axis_d,1)
        else:
            self.d_o[0] = V0
            self.pos_d = 0
            axis_d = V0
        self.axis_d = axis_d

        if axis_w is not None:
            axis_w = DraftVecUtils.scaleTo(axis_w,1)
        else:
            self.w_o[0] = V0
            self.pos_w = 0
            axis_w = V0
        self.axis_w = axis_w

        self.pos_o_adjust = V0

    def vec_d(self, d):
        """ creates a vector along axis_d (depth) with the length of argument d

        :param d: depth: lenght of the vector along axis_d
        :type d: float
        :returns: FreeCAD.Vector

        """

        # self.axis_d is normalized, so no need to use DraftVecUtils.scaleTo
        vec_d = DraftVecUtils.scale(self.axis_d, d)
        return vec_d


    def vec_w(self, w):
        """ creates a vector along axis_w (width) with the length of argument w

        :param w: width: lenght of the vector along axis_w
        :type w: float
        :returns: FreeCAD.Vector
        """

        # self.axis_w is normalized, so no need to use DraftVecUtils.scaleTo
        vec_w = DraftVecUtils.scale(self.axis_w, w)
        return vec_w


    def vec_h(self, h):
        """ creates a vector along axis_h (height) with the length of argument h

        :param h: width: height: lenght of the vector along axis_h
        :type h: float
        :returns: FreeCAD.Vector
        """

        # self.axis_h is normalized, so no need to use DraftVecUtils.scaleTo
        vec_h = DraftVecUtils.scale(self.axis_h, h)
        return vec_h

    def vec_d_w_h(self, d, w, h):
        """ creates a vector with:
        
            * depth  : along axis_d
            * width  : along axis_w
            * height : along axis_h

        :param d, w, h: depth, widht and height
        :type d, w, h: : float
        :returns: FreeCAD.Vector
        """

        vec = self.vec_d(d) + self.vec_w(w) + self.vec_h(h)
        return vec

    def set_pos_o(self, adjust=0):
        """ calculates the position of the origin, and saves it in
        attribute pos_o

        :param adjust: 

            * 1: If, when created, wasnt possible to set the piece at pos_o,
                and it was placed at pos, then the position will be adjusted

        :type adjust: int
        """

        vec_from_pos_o =  (  self.get_o_to_d(self.pos_d)
                           + self.get_o_to_w(self.pos_w)
                           + self.get_o_to_h(self.pos_h))
        vec_to_pos_o =  vec_from_pos_o.negative()
        self.pos_o = self.pos + vec_to_pos_o
        if adjust == 1:
            self.pos_o_adjust = vec_to_pos_o # self.pos_o - self.pos

    def get_o_to_d(self, pos_d):
        """If it is symmetrical along axis_d, pos_d == 0 will be at the middle
        Then, pos_d > 0 will be the points on the positive side of axis_d
        and   pos_d < 0 will be the points on the negative side of axis_d

        ::

          d0_cen = 1
                :
           _____:_____
          |     :     |   self.d_o[1] is the vector from orig to -1
          |     :     |   self.d_o[0] is the vector from orig to 0
          |_____:_____|......> axis_d
         -2 -1  0  1  2

         o---------> A:  o to  1  :
         o------>    B:  o to  0  : d_o[0]
         o--->       C:  o to -1  : d_o[1]
         o    -->    D: -1 to  0  : d_o[0] - d_o[1] : B - C
                     A = B + D
                     A = B + (B-C) = 2B - C

         d0_cen = 0
          :
          :___________
          |           |   self.d_o[1] is the vector from orig to 1
          |           |
          |___________|......> axis_d
          0  1  2  3  4

        :param pos_d: 
        :type pos_d: int
        :returns: Vector from origin pos_o to pos_d
        """
        abs_pos_d = abs(pos_d)
        if self.d0_cen == 1:
            if pos_d <= 0:
                try:
                    vec = self.d_o[abs_pos_d]
                except KeyError:
                    logger.error('pos_d key not defined ' + str(pos_d))
                else:
                    return vec
            else:
                try:
                    vec_0_to_d = (self.d_o[0]).sub(self.d_o[pos_d]) # D= B-C
                except KeyError:
                    logger.error('pos_d key not defined ' + str(pos_d))
                else:
                    vec_orig_to_d = self.d_o[0] + vec_0_to_d # A = B + D
                    return vec_orig_to_d
        else: #pos_d == 0 is at the end, distances are calculated directly
            try:
                vec = self.d_o[pos_d]
            except KeyError:
                logger.error('pos_d key not defined' + str(pos_d))
            else:
                return vec

    def get_o_to_w(self, pos_w):
        """ 
        If it is symmetrical along axis_w, pos_w == 0 will be at the middle
        Then, pos_w > 0 will be the points on the positive side of axis_w
        and   pos_w < 0 will be the points on the negative side of axis_w
        See get_o_to_d drawings

        :param pos_w:
        :type pos_w: int
        :returns: The vector from origin pos_o to pos_w
        """
        abs_pos_w = abs(pos_w)
        if self.w0_cen == 1:
            if pos_w <= 0:
                try:
                    vec = self.w_o[abs_pos_w]
                except KeyError:
                    logger.error('pos_w key not defined ' + str(pos_w))
                else:
                    return vec
            else:
                try:
                    vec_0_to_w = (self.w_o[0]).sub(self.w_o[pos_w]) # D= B-C
                except KeyError:
                    logger.error('pos_w key not defined ' + str(pos_w))
                else:
                    vec_orig_to_w = self.w_o[0] + vec_0_to_w # A = B + D
                    return vec_orig_to_w
        else: #pos_w == 0 is at the end, distances are calculated directly
            try:
                vec = self.w_o[pos_w]
            except KeyError:
                logger.error('pos_w key not defined' + str(pos_w))
            else:
                return vec

    def get_o_to_h(self, pos_h):
        """
        If it is symmetrical along axis_h, pos_h == 0 will be at the middle
        Then, pos_h > 0 will be the points on the positive side of axis_h
        and   pos_h < 0 will be the points on the negative side of axis_h
        See get_o_to_d drawings

        :param pos_h:
        :type pos_h: int
        :returns: The vector from origin pos_o to pos_h
        """
        abs_pos_h = abs(pos_h)
        if self.h0_cen == 1:
            if pos_h <= 0:
                try:
                    vec = self.h_o[abs_pos_h]
                except KeyError:
                    logger.error('pos_h key not defined ' + str(pos_h))
                else:
                    return vec
            else:
                try:
                    vec_0_to_h = (self.h_o[0]).sub(self.h_o[pos_h]) # D= B-C
                except KeyError:
                    logger.error('pos_h key not defined ' + str(pos_h))
                else:
                    vec_orig_to_h = self.h_o[0] + vec_0_to_h # A = B + D
                    return vec_orig_to_h
        else: #pos_h == 0 is at the end, distances are calculated directly
            try:
                vec = self.h_o[pos_h]
            except KeyError:
                logger.error('pos_h key not defined' + str(pos_h))
            else:
                return vec

    def get_d_ab(self, pta, ptb):
        """ 
        :returns: The vector along axis_d from pos_d = pta to pos_d = ptb
        """
        vec = self.get_o_to_d(ptb).sub(self.get_o_to_d(pta))
        return vec

    def get_w_ab(self, pta, ptb):
        """ 
        :returns: The vector along axis_h from pos_w = pta to pos_w = ptb
        """
        vec = self.get_o_to_w(ptb).sub(self.get_o_to_w(pta))
        return vec

    def get_h_ab(self, pta, ptb):
        """ 
        :returns: The vector along axis_h from pos_h = pta to pos_h = ptb
        """
        vec = self.get_o_to_h(ptb).sub(self.get_o_to_h(pta))
        return vec


    def get_pos_d(self, pos_d):
        """ 
        :returns: The absolute position of the pos_d point
        """
        return self.pos_o + self.get_o_to_d(pos_d)

    def get_pos_w(self, pos_w):
        """ 
        :returns: The absolute position of the pos_w point
        """
        return self.pos_o + self.get_o_to_w(pos_w)

    def get_pos_h(self, pos_h):
        """ 
        :returns: The absolute position of the pos_h point
        """
        return self.pos_o + self.get_o_to_h(pos_h)

    def get_pos_dwh(self, pos_d, pos_w, pos_h):
        """ 
        :returns: The absolute position of the pos_d, pos_w, pos_h point
        """
        pos = (self.pos_o + self.get_o_to_d(pos_d)
                          + self.get_o_to_w(pos_w)
                          + self.get_o_to_h(pos_h))
        return pos

    def set_name (self, name = '', default_name = '', change = 0):
        """ Sets the name attribute to the value of parameter name
        if name is empty, it will take default_name.
        if change == 1, it will change the self.name attribute to name, 
        default_name
        if change == 0, if self.name is not empty, it will preserve it

        :param name: This is the name, but it can be empty.
        :param default_name: This is the default_name, if not name
        :param change:
            
            * 1: change the value of self.name
            * 0: preserve the value of self.name if it exists

        :type name: str
        :type default_name: str
        :type change: int
        """
        # attribute name has not been created
        if (not hasattr(self, 'name') or  # attribute name has not been created
            not self.name or              # attribute name is empty
            change == 1):                 # attribute has to be changed
            if not name:
                self.name = default_name
            else:
                self.name = name
    
    def create_fco (self, name = ''):
        """ creates a FreeCAD object of the TopoShape in self.shp

        :param name: it is optional if there is a self.name
        :type name: str
        """
        if not name:
            name = self.name
        
        fco = fcfun.add_fcobj(self.shp, name, self.doc)
        self.fco = fco
        try:
            self.fco.addProperty("App::PropertyVector","axis_d","","",4)
            self.fco.addProperty("App::PropertyVector","axis_w","","",4)
            self.fco.addProperty("App::PropertyVector","axis_h","","",4)
            self.fco.axis_d = self.axis_d
            self.fco.axis_w = self.axis_w
            self.fco.axis_h = self.axis_h

        except:
            print('Error al asignar la propiedad')

    def add_child(self, child, child_sum = 1, child_name = None):
        """ add child with their features

        :param child: Object part of other object
        :param child_sum:
            
            * 1: the child adds volume to the model
            * 0: the child removes volume from the model
        
        :param child_name: Child's name

        :type child: obj3D
        :type child_sum: int
        :type child_name: str
        
        """
        #Creamos un diccionario para cada hijo que se añade con datos clave
        self.dict_child[child_name] = dict(child_d_o = child.d_o, child_w_o = child.w_o, child_h_o = child.h_o, child_shp = child.shp)

        if child_sum == 1:
            self.dict_child_sum[child_name] = dict(child_d_o = child.d_o, child_w_o = child.w_o, child_h_o = child.h_o, child_shp = child.shp)
        else:
            self.dict_child_res[child_name] = dict(child_d_o = child.d_o, child_w_o = child.w_o, child_h_o = child.h_o, child_shp = child.shp)
    def get_child(self):
        """ :returns: a dict of childs, could be an empty dict.
        """
        return self.dict_child
        
    def make_parent(self, name):
        if len(self.dict_child) == 0:
            pass
        else:
            if len(self.dict_child_sum) == 0 and len(self.dict_child_res) == 0:
                pass
            else:
                shp_sum_list = []
                shp_res_list = []
                for key in self.dict_child_sum:
                    # listar todos los volumenes a sumar
                    shp_sum_list.append(self.dict_child[key]['child_shp'])

                for key in self.dict_child_res:

                    # listar todos los volumenes a restar
                    shp_res_list.append(self.dict_child[key]['child_shp'])

                shp_sum = fcfun.fuseshplist(shp_sum_list)
                shp_res = fcfun.fuseshplist(shp_res_list)
                # restar a los volumenes a sumar los volumenes a restar
                self.shp = shp_sum.cut(shp_res)
                return self
        

####################################################################################
# Ejemplo de funcionamiento

class Placa(Obj3D):

    def __init__(self, L_d = 10, L_w = 10, L_h = 2, axis_d = VX, axis_w = VY, axis_h = VZ, name = 'placa base',pos = V0):
        """
        Create a basic shape ::

            d_o[0] d_o[1]  d_o[2]
            :      :       :
            :____________:... h_o[2]
            |            |... h_o[1]
            |____________|... h_o[0]
           o
             ____________ ... w_o[2]
            |            |
            |            |... w_o[1]
            |            |
            |____________|... w_o[0]
           o
        """
        self.shp = fcfun.shp_boxcen(L_d, L_w, L_h, cx= False, cy=False, cz=False, pos=pos)
        self.name = name
        self.axis_d = axis_d
        self.axis_h = axis_h
        self.axis_w = axis_w

        Obj3D.__init__(self, self.axis_d , self.axis_w , self.axis_h, self.name)

        self.d_o[0] = 0
        self.d_o[1] = L_d/2
        self.d_o[2] = L_d
        
        self.w_o[0] = 0
        self.w_o[1] = L_w/2
        self.w_o[2] = L_w
        
        self.h_o[0] = 0
        self.h_o[1] = L_h/2
        self.h_o[2] = L_h

        #Obj3D.create_fco(self, name)
class Hole(Obj3D):
    def __init__(self, r = None, h = None, axis_d = VX, axis_w = VY, axis_h = VZ, pos = V0, name = None):
        """
        Create a basic shape
        """
        self.shp = fcfun.shp_cyl(r, h, axis_h, pos)
        self.name = name
        self.axis_d = axis_d
        self.axis_h = axis_h
        self.axis_w = axis_w

        Obj3D.__init__(self, self.axis_d , self.axis_w , self.axis_h, self.name)

        self.d_o[0] = 0
        self.d_o[1] = r/2
        self.d_o[2] = r
        
        self.w_o[0] = 0
        self.w_o[1] = r/2
        self.w_o[2] = r
        
        self.h_o[0] = 0
        self.h_o[1] = h/2
        self.h_o[2] = h

class PlacaPerforada(Obj3D):
    """
    Create a shape with other shapes ::

        d_o[0] d_o[1]  d_o[2]
        :      :       :
        :____________:... h_o[2]
        |     : :    |... h_o[1]
        |_____:_:____|... h_o[0]
        o
         ____________ ... w_o[2]
        |            |
        |      O     |... w_o[1]
        |            |
        |____________|... w_o[0]
        o
    """
    def __init__(self, d, w, h, r, name = 'placa perforada'):
        
        self.axis_d = VX
        self.axis_w = VY
        self.axis_h = VZ
        self.name = name
        
        super().__init__(self, self.axis_d , self.axis_w , self.axis_h , self.name)
        
        self.d_o[0] = 0
        self.d_o[1] = d/2
        self.d_o[2] = d
        
        self.w_o[0] = 0
        self.w_o[1] = w/2
        self.w_o[2] = w
        
        self.h_o[0] = 0
        self.h_o[1] = h/2
        self.h_o[2] = h
        
        # añadimos el hijo 1, añadiendo volumen
        placa = Placa(d,w,h, pos = FreeCAD.Vector(self.d_o[0], self.w_o[0], self.h_o[0]))
        self.add_child(placa, 1, 'placa') 
        
        # añadimos el hijo 2, quitando volumen
        hole = Hole(r, h+0.1, axis_d = VX, axis_w = VY, axis_h = VZ, pos = FreeCAD.Vector(placa.d_o[1],placa.w_o[1],placa.h_o[0]))
        self.add_child(hole, 0, 'hole')
        # creamos al padre
        self.make_parent(name)
        # creamos el fco
        self.create_fco(name)

class PlacaTornillos(Obj3D):
    """
    Create a shape with other shapes ::

        d_o[0] d_o[2]  d_o[4]
        :  d_o[1]  d_o[3]
        :__:___:___:_:... h_o[2]
        | ::      :: |... h_o[1]
        |_::______::_|... h_o[0]
        o
         ____________ ... w_o[4]
        | o        o |... w_o[3]
        |            |... w_o[2]
        |            |... w_o[1]
        |_o________o_|... w_o[0]
        o
    """
    def __init__(self, d, w, h, r, name = 'placa tornillos'):
        axis_d = VX
        axis_w = VY
        axis_h = VZ

        Obj3D.__init__(self, axis_d , axis_w , axis_h , name)
        
        self.d_o[0] = 0
        self.d_o[1] = 2*r
        self.d_o[2] = d/2
        self.d_o[3] = d - 2*r
        self.d_o[4] = d
        
        self.w_o[0] = 0
        self.w_o[1] = 2*r
        self.w_o[2] = w/2
        self.w_o[3] = w - 2*r
        self.w_o[4] = w
        
        self.h_o[0] = 0
        self.h_o[1] = h/2
        self.h_o[2] = h
        
        # añadimos el hijo 1, añadiendo volumen
        Obj3D.add_child(self, Placa(d,w,h, pos= FreeCAD.Vector(self.d_o[0],self.w_o[0],self.h_o[0])),1, 'placa') 
        # añadimos el hijo 2, quitando volumen
        Obj3D.add_child(self, Hole(r, h+0.1, axis_d = VX, axis_w = VY, axis_h = VZ, pos = FreeCAD.Vector(self.d_o[1],self.w_o[1],self.h_o[0])), 0, 'tornillo1')
        # añadimos el hijo 3, quitando volumen
        Obj3D.add_child(self, Hole(r, h+0.1, axis_d = VX, axis_w = VY, axis_h = VZ, pos = FreeCAD.Vector(self.d_o[1],self.w_o[3],self.h_o[0])), 0, 'tornillo2')
        # añadimos el hijo 4, quitando volumen
        Obj3D.add_child(self, Hole(r, h+0.1, axis_d = VX, axis_w = VY, axis_h = VZ, pos = FreeCAD.Vector(self.d_o[3],self.w_o[3],self.h_o[0])), 0, 'tornillo3')
        # añadimos el hijo 5, quitando volumen
        Obj3D.add_child(self, Hole(r, h+0.1, axis_d = VX, axis_w = VY, axis_h = VZ, pos = FreeCAD.Vector(self.d_o[3],self.w_o[1],self.h_o[0])), 0, 'tornillo4')
        # creamos al padre
        Obj3D.make_parent(self, name)
        # creamos el fco
        Obj3D.create_fco(self, name)