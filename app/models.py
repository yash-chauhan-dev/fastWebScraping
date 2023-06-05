from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Product(Model):
    # List View -> Detail View
    __keyspace__ = "fast_web_crawler"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default="0")


class ProductScrapeEvent(Model):
    # Detail View for asin
    __keyspace__ = "fast_web_crawler"
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text(default="0")
