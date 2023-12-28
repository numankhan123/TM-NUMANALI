# -*- coding: utf-8 -*-
{
    'name': "Task Manager",

    'summary': """
        Odoo module for task management""",

    'description': """
        Odoo module for task management
    """,

    'author': "Numan Ali",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Task',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        ',
        'views/task.xml',

        # 'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_common': [
            'task_manager/static/css/kanban_ribbon_style.css'
        ],
    },
}
