{
    'name': "Restrict Update Qty On Hand Button",

    'summary': """
        Restrict access to Qty On Hand Button on product form
    """,

    'author': "Your name",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Warehouse',
    'version': '11.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'stock',
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'views/product_template.xml',
        'views/product_product.xml',
    ],
}
