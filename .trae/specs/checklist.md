# MomentFlow 验收清单

## 项目初始化与架构
- [ ] 项目目录结构符合规范（android/、backend/、ai-service/）
- [ ] 三个服务都能独立构建/运行（Android Studio 构建 / npm run dev / uvicorn）
- [ ] docker-compose.yml 可一键启动完整后端环境

## 数据模型与数据库
- [ ] Prisma Schema 定义完整（Drama、Highlight、Interaction）
- [ ] 数据库迁移执行成功
- [ ] 种子数据正确导入
- [ ] Redis 缓存连接正常

## 主业务服务 API
- [ ] GET /api/v1/dramas 返回短剧列表（≥5 条示例数据）
- [ ] GET /api/v1/dramas/:id 返回短剧详情
- [ ] GET /api/v1/dramas/:id/highlights 返回高光点列表
- [ ] POST /api/v1/interactions 成功接收并存储互动数据
- [ ] GET /api/v1/dramas/:id/emotion-heatmap 返回正确格式的热力图数据
- [ ] API 响应时间 < 100ms（P99）

## 前端功能
- [ ] 短剧列表页正常展示，卡片可点击
- [ ] 点击短剧跳转播放页，视频自动播放
- [ ] 播放器基础功能正常（播放/暂停、进度条拖拽、音量、全屏）
- [ ] 高光点到达时，Emoji Burst 组件自动弹出
- [ ] 点击表情有粒子特效动画
- [ ] 表情全局计数正确更新
- [ ] 组件 5 秒后自动消失，不残留 UI
- [ ] 进度条上有情绪热力图渲染
- [ ] 不同表情对应不同颜色
- [ ] 互动数据成功上报，不阻塞播放

## AI 分析服务（可选，MVP 阶段可先跳过）
- [ ] POST /api/analyze-video 接受视频 URL 并返回任务 ID
- [ ] GET /api/tasks/:id 返回任务状态与结果
- [ ] 能输出基础高光点时间戳

## 容器化与部署
- [ ] 所有服务 Dockerfile 构建成功
- [ ] docker-compose up 启动无报错
- [ ] 服务间通信正常（Node.js → Python）

## 文档与交付
- [ ] 技术文档完整（模块分析、技术选型、流程图）
- [ ] 工作项拆分与排期明确
- [ ] GitHub 仓库代码完整，有清晰的 README
- [ ] 项目展示录屏覆盖 MVP 全流程
