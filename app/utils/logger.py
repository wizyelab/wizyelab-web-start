"""日志工具模块"""

import logging
import sys
from config.settings import settings


def setup_logger(name: str = None) -> logging.Logger:
    """
    设置日志记录器
    
    Args:
        name: 日志记录器名称，默认为根记录器
        
    Returns:
        配置好的日志记录器
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, settings.logging_level.upper(), logging.INFO))
    
    # 如果已经有处理器，不重复添加
    if logger.handlers:
        return logger
    
    # 创建控制台处理器
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(getattr(logging, settings.logging_level.upper(), logging.INFO))
    
    # 创建格式器
    formatter = logging.Formatter(settings.logging_format)
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger


