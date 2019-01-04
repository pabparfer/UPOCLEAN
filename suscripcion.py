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
#    GNU General Public License fo r more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields

class suscripcion(osv.Model):

    _name = 'suscripcion'
    _description = 'Suscripcion asociada a una empresa'
    
    _columns = {
            'name':fields.char('Id suscripcion', size=64, required=True),
            'start': fields.date('Comienza',required=True, autodate = True),
            'cuenta':fields.char('Cuenta bancaria', size=64, required=True),
            'tipo_suscripcion': fields.char("Tipo de suscripcion",size=300, required=False),
            'empresa_id': fields.many2one( 'empresa','Empresa'),
            "usuario_id": fields.many2one( "usuario","Usuario"),
            'pedido_id':fields.one2many('pedido','suscripcion_id','Pedidos'),
        }