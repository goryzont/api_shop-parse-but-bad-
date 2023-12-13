from fastapi import APIRouter, Response, Depends

from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user, get_current_manager_user
from app.users.models import Users
from app.users.schemas import SUserAuth, SUser
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException, UserIsNotManager

router = APIRouter(
    prefix="/auth",
    tags=["Registration & Auth"]
)


@router.post("/register")
async def register_user(user_data: SUser):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password, role=user_data.role)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")


@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user


@router.post("/create_user")
async def create_user(user: SUser, current_user: Users = Depends(get_current_manager_user)):
    if not current_user:
        raise UserIsNotManager
    hashed_password = get_password_hash(user.password)
    await UsersDAO.add(email=user.email, hashed_password=hashed_password, role=user.role)


