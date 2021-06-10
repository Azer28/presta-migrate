import os

DB_HOST="localhost"
DB_PORT=3307
DB_NAME="prestashop"
DB_USER = "root"
DB_PASSWORD = os.getenv('DB_PASSWORD', '')

SHOP_URL="https://booksteller.myshopify.com"
SHOPIFY_PASSWORD = os.getenv('SHOPIFY_PASSWORD', '')


PRESTA_LOCAL_URL="http://localhost:8080/"

SQL_QUERY_CATEGORIES = """SELECT pcl.name, pcl.description
                      FROM ps_category pc
                      JOIN ps_category_lang pcl
                        ON pc.id_category=pcl.id_category
                     WHERE pcl.id_lang=%s
                       AND pcl.name NOT IN (%s, %s)"""

SQL_QUERY_PRODUCTS = f"""SELECT
                            pl.name AS 'Name',
                            p.price AS 'Price tax excl.',
                            p.quantity AS 'Quantity',
                            pl.description AS 'Description',
                            pcl.name,
                            concat('{PRESTA_LOCAL_URL}',
                                    im.id_image,
                                    '-large_default/', 
                                    pl.link_rewrite, 
                                    '.jpg') AS url_image
                        FROM ps_product p
                        INNER JOIN ps_product_lang pl ON p.id_product = pl.id_product
                        LEFT JOIN ps_image im ON p.id_product = im.id_product
                        LEFT JOIN ps_category_lang pcl ON p.id_category_default=pcl.id_category
                        WHERE p.active = %s
                        AND pl.id_lang = %s
                        AND im.position = %s
                        AND pcl.id_lang=%s;"""

