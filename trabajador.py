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

class trabajador(osv.Model):

    _name = 'trabajador'
    _description = 'Trabajador asociado a una empresa'
    
    def _check_sueldo(self, cr, uid, ids):   
        for trabajador in self.browse(cr, uid, ids):
            if trabajador.sueldo < 0 : 
                return False
        return True
    
    def _calculaTickets(self, cr, uid, ids, field, arg,context=None):                    
        res = {} 
        
        for clase in self.browse(cr,uid,ids,context=context):        
            res[clase.id] = len(clase.tick_trabajo_id)    
        return    res    
    
    _columns = {
            'name':fields.char('Nombre trabajador', size=64, required=True),
            'DNI':fields.char('DNI', size=64, required=True),
            'nticks': fields.function(_calculaTickets, type='integer', string='Numero de tickets', store  = True),
            'sueldo': fields.integer("Sueldo"),
            'empresa_id': fields.many2one( 'empresa','Empresa'),
            'tick_trabajo_id':fields.one2many('ticks','trabajador_id','Trabajos (Ticks)'),
            'jefe_ids':fields.many2many('jefe','jefe_trabajador_rel','trabajador_id','jefe_id','Jefes'),        
        }
    
    _constraints = [(_check_sueldo, ' Sueldo negativo ' , [ 'sueldo' ])]
    
   
trabajador()