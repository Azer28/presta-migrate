from dataclasses import dataclass

@dataclass
class Category:
    name: str
    html_descr: str


@dataclass
class Product:
    name: str
    price: float
    quantity: int
    html_descr: str
    category_name: str
    img_url: str
