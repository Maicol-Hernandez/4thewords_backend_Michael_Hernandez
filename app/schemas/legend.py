from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime, date


class LegendCreate(BaseModel):
    name: str
    category: str
    description: str
    legend_date: date
    province: str
    canton: str
    district: str


class LegendResponse(LegendCreate):
    id: int
    image_url: str
    created_at: datetime
    updated_at: Optional[datetime]
    # deleted_at: Optional[datetime]

    @validator("image_url", pre=True)
    def add_prefix(cls, v):
        return f"http://localhost:8080{v}"
