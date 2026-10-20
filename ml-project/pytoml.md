# Шпаргалка по pyproject.toml

`pyproject.toml` — единый файл конфигурации Python-проекта (PEP 518/621). Он заменяет
`setup.py`, `setup.cfg` и набор `requirements*.txt`.

## Основные секции

| Секция | Назначение |
|---|---|
| `[project]` | Имя, версия, описание, версия Python, обязательные зависимости |
| `[project.optional-dependencies]` | Группы дополнительных зависимостей (extras) |
| `[build-system]` | Чем собирать пакет (setuptools, hatchling, poetry-core…) |
| `[tool.<имя>]` | Настройки инструментов: `tool.setuptools`, `tool.ruff`, `tool.pytest.ini_options`, `tool.uv` |

## Пример

```toml
[project]
name = "ml-project"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["requests"]          # ставятся всегда

[project.optional-dependencies]
ml = ["numpy", "pandas"]             # ставятся по запросу: pip install ".[ml]"
service = ["fastapi", "uvicorn[standard]"]
```

## Установка через pip

```bash
pip install .                 # только обязательные зависимости
pip install -e .              # editable-режим: правки кода видны без переустановки
pip install -e ".[ml]"        # + группа ml
pip install -e ".[ml,service]"  # несколько групп
pip install -e ".[all]"       # все группы
```

> В zsh кавычки вокруг `.[ml]` обязательны, иначе квадратные скобки воспринимаются как шаблон.

## Работа через uv

```bash
uv init                       # создать новый проект с pyproject.toml
uv add numpy pandas           # добавить в dependencies
uv add --optional ml seaborn  # добавить в группу ml
uv add --dev pytest           # dev-зависимость ([dependency-groups])
uv remove pandas              # удалить зависимость
uv sync                       # привести .venv в соответствие с pyproject + uv.lock
uv sync --extra ml --extra service   # с нужными группами
uv sync --all-extras          # со всеми группами
uv lock                       # обновить uv.lock (зафиксированные версии)
uv run uvicorn app.main:app   # запуск команды внутри окружения проекта
```

## Указание версий

```toml
"numpy>=1.26"          # не ниже
"pandas>=2.0,<3.0"     # диапазон
"fastapi~=0.110"       # совместимая версия (>=0.110, <1.0)
"scikit-learn==1.5.0"  # строго
```

## Полезно знать

- `requirements.txt` можно получить из pyproject: `uv pip compile pyproject.toml --extra ml -o requirements_ML.txt`.
- Lock-файл (`uv.lock`) коммитят в git — он обеспечивает воспроизводимость.
- Поле `requires-python` защищает от установки на неподходящую версию Python.
