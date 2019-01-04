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

class pedido(osv.Model):

    _name = 'pedido'
    _description = 'modulo para gestionar un pedido'
 
    _columns = {
            'id_pedido':fields.char('Id_Pedido', size=64, required=True),
            'fechaHora':fields.datetime('Fecha_hora',required=True,autodate=True),
            'cajero':fields.char('cajero',required=True,size=50),
            'empresa_id':fields.many2one('empresa','Empresa'),
            'suscripcion_id':fields.many2one('suscripcion','Suscripcion'),
            'lineaPedido_id':fields.one2many("lineas","pedido_id","Lineas de pedido"),
            'state':fields.selection([("start","Comenzando"),("listo","Listo"),("finalizado","Finalizado")]),
            
        }
    _defaults = {"state":"start"   }
    
    _sql_constraints = [ ('pedido_uniq', 'unique (id_pedido)', 'El id de pedido usado ya existe')]

pedido()