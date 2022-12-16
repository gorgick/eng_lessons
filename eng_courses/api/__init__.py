from fastapi import APIRouter
from .words import router as words_router
from .courses import router as courses_router
from .auth import router as auth_router

router = APIRouter()

router.include_router(words_router)
router.include_router(courses_router)
router.include_router(auth_router)
