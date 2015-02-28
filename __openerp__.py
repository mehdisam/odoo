# -*- coding : utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http ://tiny.be>).
#
#    This program is free software : you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http ://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Action Group', 
    'version' : '1.0', 		
    'author' : 'Mehdi Samadi',	
    'category' : 'System',
    'sequence' : 100,		
    'website' : 'www.webirani.com',
    'summary' : 'URL Manipulation Patch for Actions',
    'description' : """
    This module prevents user from accessing unauthorized views by manipulating
    URL and restricts an action to its specified groups.
    Module only allows only actions from visible menu items to be run.
    To restrict an action to your_group simply add this line:
        <field name="groups_id" eval="[(6,0,[ref('your_group')])]" />
    to action definition and action only will be available for this group only.
    
    
    """,
    'author' : 'Mehdi Samadi',
    'images' : [
        #'images/any image files',
    ],
    'depends' : ['base','web'], # list of dependant modules
    'data' : [
        #'security/ir.model.access.csv',
    ],
    'demo' : [
        #'demo.xml'
        ], 
    'test' : [ 
        #'test1.yml',
    ],
    'installable' : True, 
    'application' : True,
    'auto_install' : False,
    'css' : [ 
        #'static/src/css/my.css' 
        ],
}
# vim :expandtab :smartindent :tabstop=4 :softtabstop=4 :shiftwidth=4 :
