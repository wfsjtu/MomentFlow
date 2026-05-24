# MomentFlow

短剧互动平台，为短剧场景打造低门槛、高沉浸的即时互动体验。

## 项目简介

MomentFlow 是一个现代化的短剧观看与互动平台，通过创新的互动形式让用户在看剧过程中「情绪即表达、表达即互动」。

## 技术栈

### 前端 (Android)
- **开发语言**: Kotlin
- **最低 SDK 版本**: API 24 (Android 7.0)
- **目标 SDK 版本**: API 34 (Android 14)
- **架构**: MVVM + Clean Architecture
- **UI 框架**: Jetpack Compose
- **视频播放**: ExoPlayer
- **网络请求**: Retrofit + OkHttp
- **依赖注入**: Hilt
- **异步处理**: Kotlin Coroutines + Flow
- **JSON 序列化**: kotlinx.serialization

### 主业务服务 (Backend)
- **框架**: NestJS (Node.js)
- **ORM**: Prisma
- **数据库**: PostgreSQL
- **缓存**: Redis (ioredis)
- **实时通信**: Socket.io (可选)

### AI 分析服务 (AI Service)
- **框架**: FastAPI (Python)
- **Web 服务器**: Uvicorn
- **AI 框架**: PyTorch / HuggingFace Transformers
- **视频处理**: OpenCV + FFmpeg
- **音频处理**: Librosa

### 部署
- **容器化**: Docker + Docker Compose

## 项目结构

```
momentflow-app/
├── android/                    # Android 前端
├── backend/                    # NestJS 主业务服务
├── ai-service/                 # FastAPI AI 分析服务
├── docker-compose.yml
└── README.md
```

## 快速开始

### 环境要求
- Node.js 18+
- Python 3.9+
- Docker 和 Docker Compose
- Android Studio (用于 Android 开发)

### 后端服务启动

1. 进入 backend 目录并安装依赖：
```bash
cd backend
npm install
```

2. 启动 Docker 容器（PostgreSQL + Redis）：
```bash
cd ..
docker-compose up -d
```

3. 配置环境变量并启动后端服务：
```bash
cd backend
cp .env.example .env
# 编辑 .env 文件配置数据库连接
npm run start:dev
```

### AI 服务启动

1. 进入 ai-service 目录并创建虚拟环境：
```bash
cd ai-service
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 启动 AI 服务：
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

### Android 应用开发

1. 使用 Android Studio 打开 android/ 目录
2. 等待 Gradle 同步完成
3. 连接 Android 设备或启动模拟器
4. 点击运行按钮

## 核心功能

- 🎬 **短剧播放** - 流畅的视频播放体验
- 😊 **Emoji Burst** - 高光时刻一键表达情绪
- 🔥 **情绪热力图** - 直观展示观众情绪分布
- 🤖 **AI 高光检测** - 自动识别剧集高光时刻
- 📊 **实时互动** - 即时反馈用户互动数据

## 开发文档

详细的开发规范和技术文档请参考 `.trae/` 目录下的相关文档。

## 许可证

MIT License
