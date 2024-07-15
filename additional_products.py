from sqlmodel import SQLModel, Field
from typing import Optional

class AdditionalProducts(SQLModel, table=True):
    primary_id: Optional[int] = Field(default=None, foreign_key="product.id", primary_key=True)
    additional_id: Optional[int] = Field(default=None, foreign_key="product.id", primary_key=True)
