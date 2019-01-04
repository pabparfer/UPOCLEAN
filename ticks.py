# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields

class ticks(osv.Model):

    _name = 'ticks'
    _description = 'gestiona el parte de trabajo'
 
    _columns = {
            'id_ticks':fields.char('id_ticks',size=30,required=True),
            'f_comienzo':fields.datetime('fecha_comienzo',required=True),
            'f_fin':fields.datetime('fecha_fin',required=True),
            'trabajador_id':fields.many2one('trabajador','Trabajador'),
            #'lineaPedido_id':fields.many2one('lineaPedido','Lineas de Pedido'),
            
            
        }
