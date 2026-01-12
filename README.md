# Wizzy Web Start

基于 FastAPI 的后端服务项目

## 项目结构

```
.
├── app/                    # 应用主目录
│   ├── api/               # API 路由
│   │   ├── open/         # 对外 Open API
│   │   ├── internal/     # 内部 API
│   │   └── router.py     # 路由聚合
│   ├── utils/            # 工具函数
│   ├── components/       # 组件模块
│   ├── llm/              # LLM 相关
│   ├── pipeline/         # Pipeline 模块
│   └── middleware/       # 中间件
├── config/               # 配置文件
│   ├── config.yaml       # YAML 配置文件
│   └── settings.py       # 配置读取模块
├── test/                 # 测试文件
├── main.py               # 应用入口
├── pyproject.toml        # Poetry 配置
└── README.md            # 项目说明
```

## 环境要求

- Python >= 3.9
- Poetry (包管理工具)

## 安装

1. 安装 Poetry（如果尚未安装）:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. 安装项目依赖:
```bash
poetry install
```

3. 激活虚拟环境:
```bash
poetry shell
```

## 配置

配置文件位于 `config/config.yaml`，支持以下配置项：

- `server`: 服务器配置（host, port, reload, workers, log_level）
- `app`: 应用配置（name, version, debug, api_prefix）
- `database`: 数据库配置
- `llm`: LLM 相关配置
- `logging`: 日志配置

配置也可以通过环境变量覆盖，环境变量格式：`WIZZY_<配置项>`（大写，下划线分隔）

例如：
- `WIZZY_SERVER_HOST=0.0.0.0`
- `WIZZY_SERVER_PORT=8000`

## 运行

### 开发模式

```bash
python main.py
```

或者使用 uvicorn 直接运行：

```bash
uvicorn main:app --reload
```

### 生产模式

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## API 文档

启动服务后，访问以下地址查看 API 文档：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 路由

- Open API: `/api/open/*`
- Internal API: `/api/internal/*`

## 测试

```bash
poetry run pytest
```

## 开发

### 代码格式化

```bash
poetry run black .
```

### 类型检查

```bash
poetry run mypy .
```

## 许可证

MIT


