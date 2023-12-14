from entrypoints.categories_router import router as category_router
from entrypoints.health_router import router as health_router


routers = [
    health_router,
    category_router,
]
