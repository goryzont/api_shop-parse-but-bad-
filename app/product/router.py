from fastapi import APIRouter, Depends

from app.exceptions import ProductAlreadyExistsException
from app.product.dao import ProductDAO
from app.product.schemas import SProduct
from app.users.dependencies import get_current_manager_user
from app.users.models import Users

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.get("/get_products")
async def get_products():
    return await ProductDAO.find_all()


@router.get("/{product_id}")
async def get_product(product_id: int, current_user: Users = Depends(get_current_manager_user)):
    if current_user:
        return await ProductDAO.find_by_id(product_id)


@router.post("/add_product")
async def add_product(product: SProduct, current_user: Users = Depends(get_current_manager_user)):
    existing_user = await ProductDAO.find_one_or_none(name=product.name)
    if current_user:
        if existing_user:
            raise ProductAlreadyExistsException
        await ProductDAO.add(name=product.name, provider=product.provider, price=product.price,
                             quantity=product.quantity)
        return "Продукт добавлен"


@router.put("/{product_id}")
async def update_product(provider: SProduct, product_id: int, current_user: Users = Depends(get_current_manager_user)):
    if current_user:
        await ProductDAO.update(product_id, provider)
        return "Продукт изменён"


@router.delete("/{product_id)")
async def delete_product(product_id: int, current_user: Users = Depends(get_current_manager_user)):
    if current_user:
        await ProductDAO.delete(product_id)
        return "Продукт удалён"
