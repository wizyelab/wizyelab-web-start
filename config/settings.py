import os
from pathlib import Path
from typing import Any, Dict
import yaml
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """应用配置类，支持从 YAML 文件和环境变量读取配置"""
    
    # 服务器配置
    server_host: str = "0.0.0.0"
    server_port: int = 8000
    server_reload: bool = True
    server_workers: int = 1
    server_log_level: str = "info"
    
    # 应用配置
    app_name: str = "wizzy-web-start"
    app_version: str = "0.1.0"
    app_debug: bool = True
    app_api_prefix: str = "/api"
    
    # 数据库配置
    database_url: str = "sqlite:///./app.db"
    database_echo: bool = False
    
    # LLM 配置
    llm_provider: str = "openai"
    llm_api_key: str = ""
    llm_model: str = "gpt-3.5-turbo"
    
    # 日志配置
    logging_level: str = "INFO"
    logging_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        env_prefix = "WIZZY_"
    
    @classmethod
    def load_from_yaml(cls, yaml_path: str = None) -> "Settings":
        """
        从 YAML 文件加载配置
        
        Args:
            yaml_path: YAML 配置文件路径，默认为 config/config.yaml
            
        Returns:
            Settings 实例
        """
        if yaml_path is None:
            # 获取项目根目录
            current_file = Path(__file__)
            project_root = current_file.parent.parent
            yaml_path = project_root / "config" / "config.yaml"
        else:
            yaml_path = Path(yaml_path)
        
        if not yaml_path.exists():
            # 如果 YAML 文件不存在，返回默认配置
            return cls()
        
        with open(yaml_path, "r", encoding="utf-8") as f:
            yaml_config = yaml.safe_load(f)
        
        # 将 YAML 配置扁平化并转换为环境变量格式
        flat_config = cls._flatten_dict(yaml_config)
        
        # 创建配置字典，优先使用环境变量，其次使用 YAML 配置
        config_dict = {}
        for key, value in flat_config.items():
            env_key = f"WIZZY_{key.upper()}"
            # 环境变量优先级最高
            env_value = os.getenv(env_key)
            if env_value is not None:
                config_dict[key] = cls._parse_env_value(env_value)
            else:
                config_dict[key] = value
        
        return cls(**config_dict)
    
    @staticmethod
    def _flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = "_") -> Dict[str, Any]:
        """
        将嵌套字典扁平化
        
        Args:
            d: 嵌套字典
            parent_key: 父键名
            sep: 分隔符
            
        Returns:
            扁平化后的字典
        """
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(Settings._flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    @staticmethod
    def _parse_env_value(value: str) -> Any:
        """
        解析环境变量值，支持布尔值和数字
        
        Args:
            value: 环境变量值
            
        Returns:
            解析后的值
        """
        if value.lower() in ("true", "1", "yes", "on"):
            return True
        elif value.lower() in ("false", "0", "no", "off"):
            return False
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value


# 全局配置实例
settings = Settings.load_from_yaml()


