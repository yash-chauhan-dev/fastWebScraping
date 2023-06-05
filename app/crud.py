import uuid

from app.models import Product, ProductScrapeEvent


def create_entry(data: dict):
    return Product.create(**data)


def create_scrape_entry(data: dict):
    data["uuid"] = uuid.uuid1()
    return ProductScrapeEvent.create(**data)


def add_scrape_entry(data: dict):
    product = create_entry(data)
    scrape_obj = create_scrape_entry(data)
    return product, scrape_obj
