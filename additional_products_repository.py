from sqlmodel import Session, select
from typing import List
from app.models.additional_products import AdditionalProducts

class AdditionalProductsRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, additional_product: AdditionalProducts):
        self.session.add(additional_product)
        self.session.commit()
        self.session.refresh(additional_product)
        return additional_product

    def update(self, additional_product: AdditionalProducts):
        self.session.add(additional_product)
        self.session.commit()
        self.session.refresh(additional_product)
        return additional_product

    def delete(self, primary_id: int, additional_id: int):
        additional_product = self.session.exec(
            select(AdditionalProducts)
            .where(AdditionalProducts.primary_id == primary_id)
            .where(AdditionalProducts.additional_id == additional_id)
        ).first()
        if additional_product:
            self.session.delete(additional_product)
            self.session.commit()
        return additional_product

    def get_all(self, primary_id: int) -> List[AdditionalProducts]:
        return self.session.exec(
            select(AdditionalProducts).where(AdditionalProducts.primary_id == primary_id)
        ).all()
