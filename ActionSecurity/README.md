# ActionSecurity
In openerp 7.0 and sitll 8.0 you can access any view by manipulating URL even if the related menu is not available to you. This addon is my solution to this problem.

This module restict user to only actions that she has access to from user interface. This modules check for group_id that is defined in the action and if user does not member of that group it drops it.
If you want add your group to given action add this to one of the xml files:
        <record id="other_module_name.action_id" model="ir.actions.act_window">
            <field eval="[(6,0,[ref('your_group_name')]),]" name="groups_id"/>
        </record>
Best Regards
M.samadi
