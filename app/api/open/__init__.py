"""对外 Open API 路由"""

from fastapi import APIRouter

router = APIRouter(prefix="/open", tags=["open"])


@router.get("/health")
async def health_check():
    """健康检查接口"""
    return {"status": "ok", "message": "Open API is healthy"}


@router.get("/")
async def root():
    """根路径"""
    return {"message": "Welcome to Open API"}


