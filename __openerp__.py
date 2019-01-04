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

{
#" 
#"empresa_demo.xml"
    "name": "UpoClean",
    "version": "1.0",
    "depends": ["base"],
    "author": "Grupo 4",
    "category": "Enterprise",
    "description": """
    Enterprise guided 
    """,
    "init_xml": [],
    "data":["usuario_view.xml","suscripcion_view.xml","empresa_view.xml","trabajador_view.xml","tick_trabajo_view.xml","linea_pedido_view.xml","material_limpieza_view.xml","pedido_view.xml","jefe_view.xml","pedido_workflow.xml"],
    'demo_xml': ["empresa_demo.xml"],
    'installable': True,
    'active': False,
}
