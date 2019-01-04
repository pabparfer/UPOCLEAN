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

class empresa(osv.Model):
    _name = 'empresa'
    _description = 'Empresa asociada a upoclean'
    
    _columns = {
            'name':fields.char('Nombre empresa', size=64, required=True),
            'CIF':fields.char('CIF', size=64, required=True),
            'location':fields.char('Localizacion', size=64, required=False),
            'cpostal':fields.integer('Codigo Postal'),
            'trabajadores_ids': fields.one2many('trabajador','empresa_id', 'Trabajadores'),
            'suscripciones_ids': fields.one2many('suscripcion','empresa_id', 'Suscripciones'),
            'pedido_id':fields.one2many('pedido','empresa_id','Pedidos'),
        }