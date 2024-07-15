from fastapi import FastAPI, Depends
from app.database import create_db_and_tables, get_session
from sqlmodel import Session
from app.models.product import Product
from app.models.additional_products import AdditionalProducts
from app.models.recommended_products import RecommendedProducts
from app.repositories.additional_products_repository import AdditionalProductsRepository
from app.repositories.recommended_products_repository import RecommendedProductsRepository
from app.services.additional_products_service import AdditionalProductsService
from app.services.recommended_products_service import RecommendedProductsService

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/additional-products/")
def add_additional_product(
    primary_id: int, additional_id: int, session: Session = Depends(get_session)
):
    repository = AdditionalProductsRepository(session)
    service = AdditionalProductsService(repository)
    return service.add_additional_product(primary_id, additional_id)

@app.post("/recommended-products/")
def add_recommended_product(
    primary_id: int, recommended_id: int, session: Session = Depends(get_session)
):
    repository = RecommendedProductsRepository(session)
    service = RecommendedProductsService(repository)
    return service.add_recommended_product(primary_id, recommended_id)
