from typing import List
from app.repositories.additional_products_repository import AdditionalProductsRepository
from app.models.additional_products import AdditionalProducts

class AdditionalProductsService:
    def __init__(self, repository: AdditionalProductsRepository):
        self.repository = repository

    def add_additional_product(self, primary_id: int, additional_id: int) -> AdditionalProducts:
        additional_product = AdditionalProducts(primary_id=primary_id, additional_id=additional_id)
        return self.repository.add(additional_product)

    def update_additional_product(self, primary_id: int, additional_id: int) -> AdditionalProducts:
        additional_product = AdditionalProducts(primary_id=primary_id, additional_id=additional_id)
        return self.repository.update(additional_product)

    def delete_additional_product(self, primary_id: int, additional_id: int):
        return self.repository.delete(primary_id, additional_id)

    def get_all_additional_products(self, primary_id: int) -> List[AdditionalProducts]:
        return self.repository.get_all(primary_id)
