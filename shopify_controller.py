from typing import List

import requests
import shopify

import settings, models
import logging

logger = logging.getLogger(__name__)

def start_shopify_session():
    api_version = '2021-04'
    private_app_password = settings.SHOPIFY_PASSWORD
    session = shopify.Session(settings.SHOP_URL, api_version, private_app_password)
    shopify.ShopifyResource.activate_session(session)
    return session


def create_image(img_url:str) -> shopify.Image:
    image = shopify.Image()
    resp = requests.get(img_url)
    image.attach_image(data=resp.content)

    return image


def find_collection_id_by_name(col_name:str) -> int:
    res_col = shopify.CustomCollection.find(title=col_name)
    if res_col:
        return res_col[0].id


def associate_product_with_collection(col_name:str, prod_id: int):
    col_id = find_collection_id_by_name(col_name)
    if col_id:
        collect = shopify.Collect(
            {
                'product_id': prod_id,
                'collection_id': col_id
            }
        )
        collect.save()
    else:
        logger.error("No collection found: %s", col_name)

def add_shopify_products(prods: List[models.Product]):
    session = start_shopify_session()
    # title, body_html(descr),
    for prd in prods:
        variant = shopify.Variant()
        variant.attributes = {
            "price": float(prd.price),
        }

        image = create_image(prd.img_url)
        product = shopify.Product(attributes={
            "title": prd.name,
            "body_html": prd.html_descr,
            "variants": [variant]
        })

        product.images = [image]
        product.save()

        associate_product_with_collection(prd.category_name, product.id)


def create_shopify_collections(collections: List[models.Category]):
    session = start_shopify_session()
    for coll in collections:
        shop_col = shopify.CustomCollection(attributes={
            "title": coll.name,
            "body_html": coll.html_descr
        })
        shop_col.save()
