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
- **AI 模型**: Doubao-Seed-2.0-lite (豆包大模型)
- **视频处理**: OpenCV + FFmpeg
- **音频处理**: Librosa

### 部署
- **容器化**: Docker + Docker Compose

## 项目结构

```
momentflow-app/
├── android/                    # Android 前端
│   ├── app/
│   │   └── src/main/
│   │       ├── java/com/momentflow/
│   │       └── res/
│   └── build.gradle.kts
├── backend/                    # NestJS 主业务服务
│   ├── src/
│   ├── prisma/
│   └── package.json
├── ai-service/                 # FastAPI AI 分析服务
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   ├── main.py
│   │   └── config.py
│   └── requirements.txt
├── docker-compose.yml
├── .env                        # 环境变量（不提交到 Git）
├── .env.example                # 环境变量示例（安全可提交）
└── README.md
```

## 快速开始

### 环境要求
- Node.js 18+
- Python 3.9+
- Docker 和 Docker Compose
- Android Studio (用于 Android 开发)

### 环境配置

#### 1. 配置环境变量

项目使用根目录的 `.env` 文件管理所有环境变量。

**步骤：**
```bash
# 复制环境变量示例文件
cp .env.example .env

# 编辑 .env 文件，填入你的配置（AI 密钥等）
# .env 文件已被 .gitignore 保护，不会提交到 Git
```

**重要的环境变量：**
| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `DATABASE_URL` | PostgreSQL 连接地址 | - |
| `REDIS_HOST` | Redis 主机 | `localhost` |
| `REDIS_PORT` | Redis 端口 | `6379` |
| `PORT` | NestJS 后端端口 | `3000` |
| `DOUBAO_MODEL` | 豆包模型名称 | `Doubao-Seed-2.0-lite` |
| `DOUBAO_EP` | 豆包 EP 地址 | **需配置** |
| `DOUBAO_API_KEY` | 豆包 API Key | **需配置** |

### 后端服务启动

1. 启动 Docker 容器（PostgreSQL + Redis）：
```bash
docker-compose up -d
```

2. 进入 backend 目录并安装依赖：
```bash
cd backend
npm install
```

3. 初始化 Prisma 并生成客户端：
```bash
npx prisma generate
npx prisma migrate dev --name init
```

4. 启动后端服务：
```bash
npm run start:dev
```

后端服务将运行在 `http://localhost:3000`

### AI 服务启动

1. 进入 ai-service 目录并创建虚拟环境：
```bash
cd ai-service
python -m venv venv
```

2. 激活虚拟环境：
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 启动 AI 服务：
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

AI 服务将运行在 `http://localhost:8001`

### 验证服务状态

访问以下地址验证服务是否正常启动：

| 服务 | 健康检查地址 |
|------|-------------|
| NestJS 后端 | `http://localhost:3000/health` |
| AI 服务 | `http://localhost:8001/health` |

### Android 应用开发

1. 使用 Android Studio 打开 `android/` 目录
2. 等待 Gradle 同步完成
3. 连接 Android 设备或启动模拟器
4. 点击运行按钮

## 核心功能

- 🎬 **短剧播放** - 流畅的视频播放体验
- 😊 **Emoji Burst** - 高光时刻一键表达情绪
- 🔥 **情绪热力图** - 直观展示观众情绪分布
- 🤖 **AI 高光检测** - 基于豆包大模型的智能高光识别
- 📊 **实时互动** - 即时反馈用户互动数据

## 安全说明

### 环境变量与密钥

1. **永远不要**将 `.env` 文件提交到 Git
2. `.env` 文件已在 `.gitignore` 中配置忽略
3. 团队协作时只分享 `.env.example`
4. 如果密钥泄露，立即重新生成

### AI 服务密钥安全

豆包模型的 API Key 和 EP 配置在 `.env` 文件中，请注意保护：

```env
# .env 中的敏感配置
DOUBAO_EP="your-ep-here"
DOUBAO_API_KEY="your-api-key-here"
```

## 开发文档

详细的开发规范和技术文档请参考 `.trae/` 目录下的相关文档：

- `.trae/specs/` - 项目需求说明和技术规格
- `.trae/rules/` - 项目开发规范和命名规则

## 常见问题

### Docker 容器无法启动

- 检查 Docker Desktop 是否正在运行
- 检查端口 5432 和 6379 是否被占用

### 环境变量读取失败

- 确认 `.env` 文件在项目根目录
- 确认环境变量格式正确
- 重启服务以加载新配置

### AI 服务无法连接豆包模型

- 检查 `.env` 中的 `DOUBAO_EP` 和 `DOUBAO_API_KEY` 配置
- 访问 `http://localhost:8001/api/config` 查看配置状态
- 检查网络连接

## 许可证

MIT License
