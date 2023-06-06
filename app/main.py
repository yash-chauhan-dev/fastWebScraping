from typing import List

from cassandra.cqlengine.management import sync_table
from fastapi import FastAPI

from app import config, crud, db, models
from app.schema import schema

settings = config.get_settings()
Product = models.Product
ProductScrapeEvent = models.ProductScrapeEvent

app = FastAPI()

session = None


@app.on_event("startup")
def on_startup():
    global session
    session = db.get_session()
    sync_table(Product)
    sync_table(ProductScrapeEvent)


@app.get("/products", response_model=List[schema.ProductListSchema])
def products_list_view():
    return list(Product.objects.all())


@app.post("/events/scrape")
def event_scrape_create_view(data: schema.ProductListSchema):
    product, scrape_obj = crud.add_scrape_event(data.dict())
    return product


@app.get("/products/{asin}")
def products_detail_view(asin):
    data = dict(Product.objects().get(asin=asin))
    events = list(ProductScrapeEvent.objects().filter(asin=asin).limit(5))
    events = [schema.ProductScrapeEventDetailSchema(**x) for x in events]
    data["events"] = events
    return data


@app.get("products/{asin}/events",
         response_model=List[schema.ProductScrapeEventDetailSchema])
def products_scrapes_list_view(asin):
    return List(ProductScrapeEvent.objects().filter(asin=asin))
