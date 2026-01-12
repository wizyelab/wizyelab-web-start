"""FastAPI 应用入口文件"""

import uvicorn
from fastapi import FastAPI
from config.settings import settings
from app.api.router import api_router
from app.middleware.cors import setup_cors
from app.middleware.logging import LoggingMiddleware
from app.utils.logger import setup_logger

# 设置日志
logger = setup_logger(__name__)

# 创建 FastAPI 应用
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.app_debug,
    description="FastAPI backend service for Wizzy Web Start",
)

# 设置中间件
setup_cors(app)
app.add_middleware(LoggingMiddleware)

# 注册 API 路由
app.include_router(api_router, prefix=settings.app_api_prefix)


@app.get("/")
async def root():
    """根路径"""
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
    }


@app.get("/health")
async def health():
    """健康检查"""
    return {"status": "healthy", "service": settings.app_name}


if __name__ == "__main__":
    # 从配置中读取 uvicorn 配置
    uvicorn.run(
        "main:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=settings.server_reload,
        workers=settings.server_workers if not settings.server_reload else 1,
        log_level=settings.server_log_level,
    )


