from sqlmodel import Session, select
from typing import List
from app.models.recommended_products import RecommendedProducts

class RecommendedProductsRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, recommended_product: RecommendedProducts):
        self.session.add(recommended_product)
        self.session.commit()
        self.session.refresh(recommended_product)
        return recommended_product

    def update(self, recommended_product: RecommendedProducts):
        self.session.add(recommended_product)
        self.session.commit()
        self.session.refresh(recommended_product)
        return recommended_product

    def delete(self, primary_id: int, recommended_id: int):
        recommended_product = self.session.exec(
            select(RecommendedProducts)
            .where(RecommendedProducts.primary_id == primary_id)
            .where(RecommendedProducts.recommended_id == recommended_id)
        ).first()
        if recommended_product:
            self.session.delete(recommended_product)
            self.session.commit()
        return recommended_product

    def get_all(self, primary_id: int) -> List[RecommendedProducts]:
        return self.session.exec(
            select(RecommendedProducts).where(RecommendedProducts.primary_id == primary_id)
        ).all()
