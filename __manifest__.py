# -*- coding: utf-8 -*-
# Part of Rhodes Technologies.
{
    "name": "Custom Module Template",
    "author": "Khalid Joomun",
    "category": "Tools",
    "description": """Custom Module Template""",
    "version": "1.0.1",
    "depends": ["mail",
                "contacts",
                "calendar",
                "portal",],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        # "data/ir_cron_data.xml",
        # "data/mail_template.xml",
        # "data/paper_format.xml",
        # "views/menu.xml",
        # "views/res_config_settings_inherit.xml",
        # "views/res_users_inherit.xml",
    ],
    'assets': {},
    "application": True,
    "installable": True,
    "auto_install": False,
}
