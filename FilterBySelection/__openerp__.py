# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2012 Domsense srl (<http://www.domsense.com>)
#    Copyright (C) 2012-2013 Agile Business Group sagl
#    (<http://www.agilebg.com>)
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
    'name': 'Filter By Selection',
    'version': '1.0',
    'category': 'Web',
    'description': """
FILTER BY SELECTION
===============
Sometimes you need to work with couple of records and adding one by one to
filter could be hard. By using this module you can select your records and
then filter them and then start to work on them.
By using this you can save your selections.
select records from list view then go to Tools->Filter by Selection to add
a filter to search view that filters all your selected records.
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
