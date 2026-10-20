# ML Project — окружение для ML-проектов

Шаблон проекта с виртуальным окружением, наборами зависимостей и простым FastAPI-сервисом.

## Структура

```
ml-project/
├── app/
│   ├── __init__.py
│   └── main.py                 # FastAPI: GET /ping -> {"status": "ok"}
├── requirements_ML.txt         # numpy, pandas, scikit-learn, seaborn, plotly
├── requirements_service.txt    # fastapi, uvicorn[standard], gradio
├── requirements_jupyter.txt    # jupyter, ipython
├── pyproject.toml              # то же самое, но в одном файле (бонус 7)
├── PYPROJECT_CHEATSHEET.md     # шпаргалка по pyproject.toml
├── screenshots/                # скриншоты для отчёта
├── .gitignore                  # .venv в репозиторий не попадает
└── README.md
```

## Вариант 1: venv + pip

### 1. Создать окружение

```bash
cd ml-project
python -m venv .venv
```

### 2. Активировать

| ОС | Команда |
|---|---|
| Linux / macOS | `source .venv/bin/activate` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |

Проверка: `which python` (Linux/macOS) или `where python` (Windows) должен указывать внутрь `.venv`.
Выход из окружения: `deactivate`.

### 3. Установить зависимости

```bash
python -m pip install --upgrade pip
pip install -r requirements_ML.txt
pip install -r requirements_service.txt
pip install -r requirements_jupyter.txt
```

Или через `pyproject.toml`:

```bash
pip install -e ".[all]"        # всё сразу
pip install -e ".[ml,jupyter]" # выборочно
```

### 4. Запустить сервис

```bash
uvicorn app.main:app --reload
```

Проверка:

```bash
curl http://127.0.0.1:8000/ping
# {"status":"ok"}
```

Документация Swagger: http://127.0.0.1:8000/docs

### 5. Запустить Jupyter

```bash
jupyter notebook
```

## Вариант 2: uv (бонус 6)

[uv](https://docs.astral.sh/uv/) — быстрый менеджер пакетов и окружений.

```bash
# установка uv
pip install uv                                        # или:
curl -LsSf https://astral.sh/uv/install.sh | sh       # Linux/macOS
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"   # Windows

# окружение и зависимости
uv venv                                   # создаёт .venv
source .venv/bin/activate                 # активация (Windows: .venv\Scripts\activate)
uv pip install -r requirements_ML.txt
uv pip install -r requirements_service.txt
uv pip install -r requirements_jupyter.txt

# либо через pyproject.toml
uv sync --all-extras

# запуск без активации окружения
uv run uvicorn app.main:app --reload
```

## Git и GitHub

```bash
git init
git add .
git commit -m "Initial commit: окружение, зависимости, FastAPI /ping"
git branch -M main
git remote add origin https://github.com/Sanzerin/ml-project.git
git push -u origin main
```

Папка `.venv` указана в `.gitignore` и в репозиторий не попадает
