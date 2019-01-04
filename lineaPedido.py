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

class lineaPedido(osv.Model):
    _name = 'lineas'
    _description = 'cada linea de pedido de un pedido'
 
    _columns = {
            'id_lineas':fields.char('ID',required=True,size=64),
            'lugar':fields.char('Lugar', size=300, required=True),
            'metros':fields.char('Metros',size=10,required=True),
            'f_comienzo':fields.date('fecha_comienzo',autodate=True, required=True),
            'f_fin':fields.date('fecha_fin',required=True),  
            #'tickTrabajo_id':fields.one2many('ticks','lineaPedido_id','Trabajos (Ticks)'),
            'pedido_id':fields.many2one('pedido','Pedidos'),
            
            
        }