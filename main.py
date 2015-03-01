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
import openerp
from openerp.addons.web import http
openerpweb = http
class Meh_Action(openerp.addons.web.controllers.main.Action):
    _cp_path = "/web/action"

    @openerpweb.jsonrequest
    def load(self, req, action_id, do_not_eval=False):
        Actions = req.session.model('ir.actions.actions')
        value = False
        try:
            action_id = int(action_id)
        except ValueError:
            try:
                module, xmlid = action_id.split('.', 1)
                model, action_id = req.session.model('ir.model.data').get_object_reference(module, xmlid)
                assert model.startswith('ir.actions.')
            except Exception:
                action_id = 0   # force failed read

        base_action = Actions.read([action_id], ['type'], req.context)
        # read groups of current user
        user_groups = frozenset(req.session.model('res.users').read( [req.session._uid], ['groups_id'], req.context)[0]['groups_id'])
        visible_menu_ids = []
        if base_action:
            ctx = {}
            action_type = base_action[0]['type']
            if action_type == 'ir.actions.report.xml':
                ctx.update({'bin_size': True})
            ctx.update(req.context)
            action = req.session.model(action_type).read([action_id], False, ctx)
            # get all menus that have reference to this action
            if action_type == 'ir.actions.act_window' and  action[0].get('id',False) :
                ir_values_obj = req.session.model('ir.values')
                ir_menu_obj = req.session.model("ir.ui.menu")
                value_ids = ir_values_obj.search([
                                                  ('model', '=', 'ir.ui.menu'), ('key', '=', 'action'),
                                                  ('key2', '=', 'tree_but_open'), ('value', '=', 'ir.actions.act_window,{0}'.format(action[0]['id']) )],context=req.context)
                menu_ids = [menu['res_id'] for menu in ir_values_obj.read(value_ids,['res_id'],req.context)]
                # get all visible menus
                all_menu_ids = set(ir_menu_obj.search([],context=req.context))
                # remove menu if parent is not in the visible list
                
                for menu_id in  menu_ids :
                    cmenu_id = menu_id
                    while True:
                        parent_menu = ir_menu_obj.read(cmenu_id,['parent_id'],context=req.context) or []
                        parent_menu_id = parent_menu['parent_id'][0] if parent_menu['parent_id'] else False
                        
                        if not parent_menu_id :
                            if cmenu_id in all_menu_ids:
                                visible_menu_ids.append(menu_id)
                            break
                        elif cmenu_id not in all_menu_ids:
                            break
                        cmenu_id = parent_menu_id
                
                
                
            # no groups_id === green light, user group has overlap with groups_id
            if ((action  and action[0].get('groups_id',[]) == []) and visible_menu_ids) or not user_groups.isdisjoint(set(action[0].get('groups_id',[]))) :
                value = openerp.addons.web.controllers.main.clean_action(req, action[0])
        return value
# vim :expandtab :smartindent :tabstop=4 :softtabstop=4 :shiftwidth=4 :
