from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

app = FastAPI(title="MomentFlow AI Service", version="1.0.0")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "MomentFlow AI Service",
        "status": "running",
        "model": settings.DOUBAO_MODEL
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model_configured": bool(settings.DOUBAO_API_KEY and settings.DOUBAO_EP)
    }


@app.get("/api/config")
async def get_config():
    """获取配置信息（隐藏敏感数据）"""
    return {
        "model": settings.DOUBAO_MODEL,
        "ep_configured": bool(settings.DOUBAO_EP),
        "api_key_configured": bool(settings.DOUBAO_API_KEY)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=True)

