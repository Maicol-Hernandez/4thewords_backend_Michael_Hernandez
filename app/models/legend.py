from sqlmodel import SQLModel, Field, Relationship
from datetime import date, datetime
from typing import Optional, List

class LegendBase(SQLModel):
    name: str = Field(index=True, max_length=100)
    category: str = Field(index=True, max_length=50)
    description: str = Field(max_length=500)
    image_url: str
    legend_date: date
    province: str = Field(max_length=50)
    canton: str = Field(max_length=50)
    district: str = Field(max_length=50)
    
class Legend(LegendBase, table=True):
    __tablename__ = "legends"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.today)
    updated_at: Optional[datetime] = Field(default_factory=datetime.today)
    deleted_at: Optional[datetime] = Field(default=None)