# -*- coding: utf-8 -*-
##############################################################################
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Convert Selection To Filter',
    'version': '1.0',
    'category': 'Web',
    'description': """
FILTER BY SELECTION
===============
This module allows you to convet your selected records in a list view to a 
search view filter.
""",
    'author': "Mehdi Samadi    ",
    'website': 'http://www.webirani.co',
    'license': 'AGPL-3',
    'depends': ['web'],
    # 'external_dependencies': {
    #     'python': ['xlwt'],
    # },
    'qweb': ['static/xml/filter_by_selection.xml'],    
    'js': ['static/*/*.js', 'static/*/js/*.js'],

    'installable': True,
    'auto_install': False,
    'web_preload': False,
}
