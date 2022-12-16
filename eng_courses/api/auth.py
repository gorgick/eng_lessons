from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from eng_courses.models.auth import Token, UserCreate, User
from eng_courses.services.auth import AuthService, get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=Token)
def register(user_data: UserCreate, service: AuthService = Depends()):
    """
    Just register, and create the new abilities to study a lot of words every day!
    \f
    :param user_data:
    :param service: 
    :return:
    """
    return service.register_new_user(user_data)


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends()):
    return service.authenticate_user(form_data.username, form_data.password)


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user
