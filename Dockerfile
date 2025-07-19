FROM python:3.11-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY requirements.txt ./

RUN uv init

RUN uv venv

RUN uv pip install -r requirements.txt

COPY bot.py ./

CMD ["uv", "run", "bot.py"] 