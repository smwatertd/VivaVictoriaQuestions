from entrypoints.categories_router import router as category_router
from entrypoints.health_router import router as health_router
from entrypoints.questions_router import router as questions_router


routers = [
    health_router,
    category_router,
    questions_router,
]
