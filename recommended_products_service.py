from typing import List
from app.repositories.recommended_products_repository import RecommendedProductsRepository
from app.models.recommended_products import RecommendedProducts

class RecommendedProductsService:
    def __init__(self, repository: RecommendedProductsRepository):
        self.repository = repository

    def add_recommended_product(self, primary_id: int, recommended_id: int) -> RecommendedProducts:
        recommended_product = RecommendedProducts(primary_id=primary_id, recommended_id=recommended_id)
        return self.repository.add(recommended_product)

    def update_recommended_product(self, primary_id: int, recommended_id: int) -> RecommendedProducts:
        recommended_product = RecommendedProducts(primary_id=primary_id, recommended_id=recommended_id)
        return self.repository.update(recommended_product)

    def delete_recommended_product(self, primary_id: int, recommended_id: int):
        return self.repository.delete(primary_id, recommended_id)

    def get_all_recommended_products(self, primary_id: int) -> List[RecommendedProducts]:
        return self.repository.get_all(primary_id)
