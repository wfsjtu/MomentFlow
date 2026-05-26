"""
MomentFlow AI Service Configuration
读取根目录的 .env 文件
"""
import os
from dotenv import load_dotenv
from pathlib import Path

# 加载根目录的 .env 文件
project_root = Path(__file__).parent.parent.parent  # ai-service/ -> ../ -> ../
load_dotenv(project_root / '.env')


class Settings:
    """AI 服务配置类"""
    
    # 服务基础配置
    HOST: str = "0.0.0.0"
    PORT: int = 8001
    
    # 豆包模型配置
    DOUBAO_MODEL: str = os.getenv("DOUBAO_MODEL", "Doubao-Seed-2.0-lite")
    DOUBAO_EP: str = os.getenv("DOUBAO_EP", "")
    DOUBAO_API_KEY: str = os.getenv("DOUBAO_API_KEY", "")
    
    # 日志配置
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")


settings = Settings()
