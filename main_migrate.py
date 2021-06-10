from presta_controller import fetch_categories, fetch_products
from shopify_controller import create_shopify_collections, add_shopify_products


def migrate_categories_to_shopify():
    ctgrs = fetch_categories()
    create_shopify_collections(ctgrs)


def migrate_products_to_shopify():
    presta_prods = fetch_products()
    add_shopify_products(presta_prods)

# migrate_categories_to_shopify()
# migrate_products_to_shopify()