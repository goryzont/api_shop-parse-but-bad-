from fastapi import FastAPI

from app.users.router import router as router_users
from app.product.router import router as router_product
# from app.provider.router import router as router_provider
from app.orders.router import router as router_orders
from app.orders.router import router_order_states
from app.parser.router import router as router_parser

app = FastAPI(
    title="api_shop"
)

app.include_router(router_users)
app.include_router(router_product)
# app.include_router(router_provider) # Из за спаршенных данных он выглядит некорректно
app.include_router(router_orders)
app.include_router(router_order_states)
app.include_router(router_parser)
