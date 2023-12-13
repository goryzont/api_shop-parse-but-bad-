from fastapi import APIRouter, Depends

from app.exceptions import ProductAlreadyExistsException
from app.orders.dao import OrdersDAO, OrderStatesDAO
from app.orders.schemas import SOrderStates, SOrders
from app.users.dependencies import get_current_manager_user
from app.users.models import Users

router = APIRouter(
    prefix="/order",
    tags=["Orders"]
)

router_order_states = APIRouter(
    prefix="/order_state",
    tags=["Order_states"]
)


@router.get("/get_orders")
async def get_orders(current_user: Users = Depends(get_current_manager_user)):
    if current_user:
        return await OrdersDAO.find_all()


@router.get("/{order_id}")
async def get_order(order_id: int, current_user: Users = Depends(get_current_manager_user)):
    if current_user:
        return await OrdersDAO.find_by_id(order_id)


@router_order_states.post("/add_product")
async def add_orders_states(order_states: SOrderStates, current_user: Users = Depends(get_current_manager_user)):
    if current_user:
        await OrderStatesDAO.add(name=order_states.name)
        return "Статус добавлен"

