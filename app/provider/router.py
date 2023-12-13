from fastapi import APIRouter, Depends

from app.database import async_session_maker
from app.exceptions import ProviderAlreadyExistsException
from app.provider.dao import ProviderDAO
from app.provider.models import Provider
from app.provider.schemas import SProvider
from app.users.dependencies import get_current_manager_user
from app.users.models import Users


router = APIRouter(
    prefix="/provider",
    tags=["Provider"]
)


@router.get("/get_providers")
async def get_providers():
    return await ProviderDAO.find_all()


@router.get("/{provider_id}")
async def get_provider(provider_id: int, current_user: Users = Depends(get_current_manager_user)):
    if current_user:
        return await ProviderDAO.find_by_id(provider_id)


@router.post("/add_provider")
async def add_provider(provider: SProvider, current_user: Users = Depends(get_current_manager_user)):
    existing_user = await ProviderDAO.find_one_or_none(email=provider.email)
    if current_user:
        if existing_user:
            raise ProviderAlreadyExistsException
        await ProviderDAO.add(name=provider.name, phone=provider.phone,
                              email=provider.email, address=provider.address)
        return "Провайдер добавлен"


@router.put("/{provider_id}")
async def update_provider(provider: SProvider, provider_id: int, current_user: Users = Depends(get_current_manager_user)):
    if current_user:
        await ProviderDAO.update(provider_id, provider)
        return "Провайдер изменён"


@router.delete("/{provider_id)")
async def delete_provider(provider_id: int, current_user: Users = Depends(get_current_manager_user)):
    if current_user:
        await ProviderDAO.delete(provider_id)
        return "Провайдер удалён"
