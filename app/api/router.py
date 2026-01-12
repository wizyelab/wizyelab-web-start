"""API 路由聚合模块"""

from fastapi import APIRouter
from app.api.open import router as open_router
from app.api.internal import router as internal_router

# 创建主路由
api_router = APIRouter()

# 注册子路由
api_router.include_router(open_router)
api_router.include_router(internal_router)


