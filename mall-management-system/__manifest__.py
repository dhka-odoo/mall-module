{
    'name': 'Mallz',
    'version': '1.0',
    'depends': ['base','mail'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    'data':[
        'security/ir.model.access.csv',
        'views/mall_shop_rent_views.xml',
        'views/mall_shop_views.xml',
        'views/mall_floor_views.xml',
        'views/all_malls_views.xml',
        'views/mall_overview.xml',
        'views/mall_shop_offer_views.xml',
        'views/mall_tenant_views.xml',
        'views/mall_shop_categories_views.xml',
        'data/mall_shop_rent_sequence.xml',
        'views/res_users_views.xml',
        'views/mall_menus.xml',
    ],
    "demo":[
        "demo/demo_malls.xml",
        "demo/mall.shop.categories.csv",
        "demo/demo_mall_floor.xml",
        "demo/demo_mall_tenant.xml",
        "demo/demo_mall_shop.xml",
        "demo/demo_mall_shop_offers.xml",
    ],
    'application': True,
}
