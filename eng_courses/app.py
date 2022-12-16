from fastapi import FastAPI
from .api import router

tags_metadata = [
    {
        "name": "auth",
        'description': "Авторизация и регистрация"
    },
{
        "name": "words",
        'description': "Незнакомые слова"
    },
{
        "name": "courses",
        'description': "Наши курсы незнакомых слов"
    },
]

app = FastAPI(
    title="Your english course for every day!",
    description="Незнакомые слова и их перевод",
    openapi_tags=tags_metadata
)

app.include_router(router)
