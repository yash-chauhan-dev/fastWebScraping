from typing import Any, Optional
from uuid import UUID

from pydantic import BaseModel, root_validator

from app import utils


class ProductSchema(BaseModel):
    asin: str
    title: str


class ProductScrapeEventSchema(BaseModel):
    uui: UUID
    asin: str
    title: Optional[str]


class ProductListSchema(BaseModel):
    asin: str
    title: str


class ProductScrapeEventDetailSchema(BaseModel):
    asin: str
    title: Optional[str]
    created: Optional[Any] = None

    @root_validator(pre=True)
    def extra_create_time_from_uuid(cls, values):
        values['created'] = utils.uuid1_time_to_datetime(values['uuid'].time)
        return values
