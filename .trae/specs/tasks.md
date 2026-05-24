# MomentFlow 任务清单

## 项目结构
```
momentflow-app/
├── android/           # Android 前端
├── backend/           # NestJS 主业务服务
├── ai-service/        # FastAPI AI 分析服务
└── docker-compose.yml
```

---

## 任务列表

### 第一阶段：项目初始化与基础架构
- [ ] 任务 1.1：初始化项目目录结构
  - [ ] 创建 `android/`、`backend/`、`ai-service/` 目录
  - [ ] 创建根目录 `docker-compose.yml`
  - [ ] 创建根目录 `.gitignore`

- [ ] 任务 1.2：初始化 Android 前端项目
  - [ ] 使用 Android Studio 创建 Kotlin 项目
  - [ ] 配置基础依赖（ExoPlayer、Retrofit、Hilt、Jetpack Compose）
  - [ ] 配置项目架构（MVVM + Clean Architecture）

- [ ] 任务 1.3：初始化主业务服务（NestJS）
  - [ ] 使用 Nest CLI 创建项目
  - [ ] 配置 Prisma ORM + PostgreSQL
  - [ ] 配置 Redis 连接
  - [ ] 配置 CORS、环境变量

- [ ] 任务 1.4：初始化 AI 分析服务（FastAPI）
  - [ ] 创建 FastAPI 项目结构
  - [ ] 配置 Python 依赖（FastAPI、Uvicorn、PyTorch、OpenCV、Librosa）
  - [ ] 配置 Dockerfile
  - [ ] 配置环境变量

---

### 第二阶段：数据模型与数据库
- [ ] 任务 2.1：设计并创建 Prisma Schema
  - [ ] Drama（短剧）模型
  - [ ] Highlight（高光点）模型
  - [ ] Interaction（互动记录）模型
  - [ ] 生成数据库迁移并执行

- [ ] 任务 2.2：准备种子数据
  - [ ] 创建示例短剧数据
  - [ ] 创建示例高光点标注数据（用于 MVP 测试）
  - [ ] 编写种子数据脚本

---

### 第三阶段：主业务服务 API 开发
- [ ] 任务 3.1：短剧模块 API
  - [ ] GET /api/v1/dramas - 短剧列表
  - [ ] GET /api/v1/dramas/:id - 短剧详情

- [ ] 任务 3.2：高光点模块 API
  - [ ] GET /api/v1/dramas/:id/highlights - 获取剧集高光点
  - [ ] POST /api/v1/highlights - 创建高光点（管理端）
  - [ ] 实现 Redis 缓存高光点数据

- [ ] 任务 3.3：互动模块 API
  - [ ] POST /api/v1/interactions - 上报用户互动
  - [ ] GET /api/v1/dramas/:id/emotion-heatmap - 获取情绪热力图
  - [ ] 实现按时间窗口聚合统计逻辑

- [ ] 任务 3.4：AI 服务调用集成
  - [ ] 实现 HTTP 客户端调用 Python AI 服务
  - [ ] 实现视频分析任务触发接口
  - [ ] 实现分析结果回调接收与存储

---

### 第四阶段：Android 前端开发
- [ ] 任务 4.1：短剧列表页
  - [ ] 短剧卡片 Composable
  - [ ] 网格布局
  - [ ] 点击跳转播放页

- [ ] 任务 4.2：短剧播放器
  - [ ] 集成 ExoPlayer
  - [ ] 基础播控（播放/暂停、进度条、音量、全屏）
  - [ ] 进度条上叠加情绪热力图组件

- [ ] 任务 4.3：Emoji Burst 互动组件
  - [ ] 高光点到达时自动弹出组件
  - [ ] 表情点击事件处理
  - [ ] Compose 动画特效
  - [ ] 全局计数显示
  - [ ] 组件自动消失逻辑

- [ ] 任务 4.4：情绪热力图可视化
  - [ ] 进度条上方/下方热力条渲染
  - [ ] 颜色映射逻辑
  - [ ] 点击显示详情

- [ ] 任务 4.5：API 集成
  - [ ] 配置 Retrofit 客户端
  - [ ] 互动数据异步上报
  - [ ] 实时更新热力图

---

### 第五阶段：AI 分析服务开发（可选，MVP 阶段可先接入预标注数据）
- [ ] 任务 5.1：视频分析基础接口
  - [ ] POST /api/analyze-video - 提交视频分析任务
  - [ ] GET /api/tasks/:id - 查询任务状态

- [ ] 任务 5.2：多信号融合高光检测（第一阶段先做简单版本）
  - [ ] 音频能量峰值检测（使用 Librosa）
  - [ ] 场景切换检测（使用 OpenCV）
  - [ ] 基础高光点时间戳输出

- [ ] 任务 5.3：场景分类（可选，后续迭代）
  - [ ] 冲突/反转/名场面/撒糖分类模型
  - [ ] 结果输出与主业务服务集成

---

### 第六阶段：容器化与部署
- [ ] 任务 6.1：Docker 配置
  - [ ] 编写 backend/Dockerfile
  - [ ] 编写 ai-service/Dockerfile
  - [ ] 编写 docker-compose.yml（包含 PostgreSQL、Redis）

- [ ] 任务 6.2：本地测试与验证
  - [ ] docker-compose up 本地完整运行
  - [ ] 端到端流程测试

- [ ] 任务 6.3：公有云部署文档
  - [ ] 容器镜像构建与推送
  - [ ] 云服务部署步骤

---

### 第七阶段：文档与交付
- [ ] 任务 7.1：技术文档
  - [ ] 模块分析与拆解
  - [ ] 核心模块技术选型说明
  - [ ] 主要流程图（架构图、数据流程图）

- [ ] 任务 7.2：项目展示
  - [ ] 项目展示录屏
  - [ ] GitHub 仓库整理

---

## 任务依赖关系

```
任务 1.x → 任务 2.x → 任务 3.x → 任务 4.x → 任务 6.x
                  ↘
                   任务 5.x（可选，可并行或后续）
```

## MVP 核心路径（推荐优先级）

1. **阶段 1-4** 是必做 MVP
2. **阶段 5** 可先跳过，用预标注数据跑通流程
3. 完成后再迭代 AI 功能
