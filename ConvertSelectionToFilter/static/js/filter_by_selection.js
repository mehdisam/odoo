//  @@@ filter by selection JS @@@
//#############################################################################
//    
//    Copyright (C) 2015 Mehdi Samadi
//    
//
//    This program is free software: you can redistribute it and/or modify
//    it under the terms of the GNU Affero General Public License as published
//    by the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU Affero General Public License for more details.
//
//    You should have received a copy of the GNU Affero General Public License
//    along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//#############################################################################

openerp.filter_by_selection = function(instance, m) {

    var _t = instance.web._t,
    QWeb = instance.web.qweb;

    instance.web.Sidebar.include({
        redraw: function() {
            var self = this;
            this._super.apply(this, arguments);
            self.$el.find('.oe_sidebar').append(QWeb.render('AddToolsTemplate', {widget: self}));
            self.$el.find('.oe_sidebar_filter_by_selection').on('click', self.on_sidebar_filter_by_selection);
        },

        on_sidebar_filter_by_selection: function() {
        	var self = this;
        	var active_ids = self.getParent().groups.get_selection().ids;
        	var domain = ['id','in',active_ids]
        	this.getParent().ViewManager.searchview.query.add({
                category: "Advanced",
                values: [{label: 'Filter By Selections', value: {domain}}],
                field: {
                    get_context: function () { },
                    get_domain: function () { return [('id','in',domain)];},
                    get_groupby: function () { }
                }
            });
        	
        },

    });

};
