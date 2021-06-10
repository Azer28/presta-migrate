from mysql.connector import connect

import settings
from models import Category, Product


def get_db_connection():
    return connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME
    )


def fetch_categories():
    categories = []
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                settings.SQL_QUERY_CATEGORIES,
                (1, 'Root', 'Home')
            )
            for ctgr in cursor.fetchall():
                categories.append(Category(*ctgr))

    finally:
        conn.close()

    return categories


def fetch_products():
    products = []

    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                settings.SQL_QUERY_PRODUCTS,
                (1, 1, 1, 1)
            )
            for prd in cursor.fetchall():
                products.append(Product(*prd))

    finally:
        conn.close()

    return products
