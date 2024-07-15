from sqlmodel import SQLModel, Field
from typing import Optional

class RecommendedProducts(SQLModel, table=True):
    primary_id: Optional[int] = Field(default=None, foreign_key="product.id", primary_key=True)
    recommended_id: Optional[int] = Field(default=None, foreign_key="product.id", primary_key=True)
