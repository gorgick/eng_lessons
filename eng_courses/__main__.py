import uvicorn
from .settings import settings

uvicorn.run(
    'eng_courses.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)
