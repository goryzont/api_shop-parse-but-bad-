from app.dao.base import BaseDAO
from app.orders.models import Orders, OrderStates


class OrdersDAO(BaseDAO):
    model = Orders


class OrderStatesDAO(BaseDAO):
    model = OrderStates
